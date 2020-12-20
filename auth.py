import os
import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')


# AuthError Exception
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header
def get_token_auth_header():
    # Optains the Access Token from authorization Header
    auth = request.headers.get('Authorization', None)

    # Check if thier is an auth header
    if not auth:
        raise AuthError({
           'code': 'authorization_header_missing',
           'description': 'Authorization header is expected'
           }, 401)

    # Check if it is strt with a Bearer
    parts = auth.split()
    if parts[0].lower() != 'bearer':
        raise AuthError({
           'code': 'invalid_header',
           'description': 'Authorization header must start with "Bearer".'
           }, 401)

    # Check the Token
    elif len(parts) == 1:
        raise AuthError({
           'code': 'invalid_header',
           'description': 'Token not found'
           }, 401)

    # Check if is a Bearer
    elif len(parts) > 2:
        raise AuthError({
           'code': ' invaid_header',
           'desription': 'Authorization header must be bearer token.'
           }, 401)

    token = parts[1]
    return token


def check_permissions(permission, payload):
    # Check if permmsion not in Token
    if 'permissions' not in payload:
        abort(400)

    # Check if user have a premissions to access
    if permission not in payload['permissions']:
        abort(401)

    return True


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)

    res_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
           'code': 'invalid_header',
           'description': 'Authorization malformed'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )
            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invslid_claims',
                'descriotion': 'Incorrect claimss,' +
                               'Please, check the audience ans issuer.'
                }, 401)

        except Exception:
            raise AuthError({
               'code': 'invalid_heaser',
               'description': 'Unable to parse authentication token.'
            }, 400)

    raise AuthError({
            'code': 'invalid_header',
            'description': 'Unavle to find the appropriate key.'
            }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Get token from header
            token = get_token_auth_header()
            # Decode token
            payload = verify_decode_jwt(token)
            # Check if token have permission
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
