Introduction:

The web is Casting Agency that will let user to retrive information about Actore and Movie,
and some user special have a primmesion to add , update and delate actore and Movie

Getting started:

pre-requirments and local development:
developer using the project should alrady installed Python3 and PIP on thie local machines

Backend:
please run requirments file for all required pakages need for thre web please run the below
 
pip install requirments.txt 

for run the application in server

export FLASK_APP=app
export FLASK_ENV=development
flask run

the application will run as default on http://127.0.0.1:5000

Base URL:
The APP will be run locally at http://127.0.0.:5000/

Authentication:
This version of applocation dose  require authentication or API keys
castingassistant120@gmail.com
Ca12345678
castingdirector28@gmail.com
Cd12345678
castingexecutive70@gmail.com
Ca12345678

response codes

Endpoint:
GET/Actor
return all the actors information

postman GET http://127.0.0.1:5000/actors

{
    "actore": [
        {
            "age": "29",
            "gender": "Female",
            "id": 1,
            "name": "Emma Roberts"
        }
    ],
    "success": true,
    "total_actor": 1
}


PATCH/Actor
update actor information based on ID

postman PATCH http://127/0/0/1:5000/actores/1

DELETE/Actor
delete actor based on ID

postman DELETE http://127.0.0.1:5000/actors/1

POST/Actor
add new actore in the list

postman POST  http://127.0.0.1:5000/artors/create

Result:
{
    "actors": [
        {
            "age": "29",
            "gender": "Female",
            "id": 1,
            "name": "Emma Roberts"
        }
    ],
    "success": true
}


GET/Movies
return all movies

postman GET http://127.0.0.1:5000/movies

PATCH/Movies
update movie information bassed on ID

Postman PATCH http://127.0.0.1:5000/1


DELETE/Movie
Delete movie bassed on ID

Postman DELETE http://127.0.0.1/1


POST/Movie
add new movie in the list

Postman POST http://127.0.0.1:5000/movies/create



Error Type

return error in JSIN obkects in the followinf formate:

{
    success: False,
    error: 422,
    message: Unprocessable
}

{
    success: False,
    error: 404,
    message: Not Found
}

the API will return error as 

422:Uunprocessable
404: Not Found

Auther
Mona Alahmadi

