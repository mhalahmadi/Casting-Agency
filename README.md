# Introduction:

The web is Casting Agency that will let user to retrive information about Actore and Movie, and some user special have a primmesion to add , update and delate actore and Movie

on this project it challenge me that i put all the knowledge that i grant from the course of Full Stack Developer by udacity I found out that I get good experience with the course , I practice alot and that why i can make a backend programs eaiser then before

## Getting started:

pre-requirments and local development: developer using the project should alrady installed Python3 and PIP on thie local machines

Backend: please run requirments file for all required pakages need for thre web please run the below

`pip3 install requirments.txt`

for run the application in server

On linux : `export`

On Windows : `set`

```
export FLASK_APP=app

export FLASK_ENV=development

flask run
```


## Base URL: 

The APP will be run locally at ``http://127.0.0.:5000/``

The APP will be run in internet at `https://castingagen88.herokuapp.com`


## Authentication: 

This version of application dose require authentication

Three type of authintaction

### 1-Casting assistant

Get/Actore

Get/Movie

### 2-Casting diractore

Get/Actor 

Get/Movie 

Patch/Actor 

Post/Actor 

Patch/Actor 

Delete/Actor

### 3-Casting Executive

Get/Actor

Get/Movie
 
Post/Actor

Post/Movie

Patch/Actor

Patch/Movie

Delete/Actor 

Delete/Movie

If token is expired please use as below

### log-in:
```
dev-mirai.us.auth0.com/authorize?audience=CastingAgency& response_type=token& client_id=qN6cyNfqsPreqoQWhvYDx6AcCtigXMv6& redirect_uri=http://127.0.0.1:5000/results
```

### Log-out:
```
https://dev-mirai.us.auth0.com/v2/logout?client_id=U8XDu4EKfy8wihkNq35EWTZC2UOphmTT
```

### Account:


* Casting assistant
````
 Email: castingassistant120@gmail.com

 Password: Ca12345678 
````

* Casting director 
````
Email: castingdirector28@gmail.com

Password: Cd12345678
````
* Casting Executive
````
Email: castingexecutive70@gmail.com

Password: Ca12345678
````

In order to use the token in code add token in `setup_example.sh`

run in GIT BASH

`source setup_exapmle.sh`

## Testing

Testing by postman 

`import Casting Agency Local.postman_collection`


## Endpoint:



GET/Actor return all the actors information

Postman `GET https://castingagen88.herokuapp.com/actors`

**Permissions:**

 Casting assistant - Casting director - Casting Executive

**Result:**
````
 {
 "actore":[{ 

          "age": "29",

          "gender": "Female", 

          "id": 1, 
 
          "name": "Emma Roberts"

        }], 

    "success": true, 

    "total_actor": 1
}
````


PATCH/Actor update actor information based on ID


postman `PATCH https://castingagen88.herokuapp.com/actors/1`

**Permissions:**

Casting director - Casting Executive

**Result:**
```` 
{ "actor": [ {

 "age": "30", 

"gender": "Female", 

"id": 1, "name": "Emma Roberts"

 } ], 
"success": true,

 "total_actor": 1,

 "updated": 1
 }
````

DELETE/Actor delete actor based on ID


postman `DELETE https://castingagen88.herokuapp.com/actors/1`


**Permissions:**

Casting director - Casting Executive


**Result:**
````
{
 "delete": 1,

 "success": true

 }
````

POST/Actor add new actor in the list


postman `POST https://castingagen88.herokuapp.com/artors/create`


**Permissions:**

Casting director - Casting Executive


**Result:**
````
{ "actors": [ {

 "age": "29",

 "gender": "Female", 

"id": 1,

 "name": "Emma Roberts"

 } ],

 "success": true 
}
````

GET/Movies return all movies

postman `GET https://castingagen88.herokuapp.com/movies`


**Permissions:**

Casting Assistant - Casting Director - Casting Executive


**Result:**

````
{ 
"movie": [ { 

"id": 2,

"relase_date":

"Mon, 01 Oct 2012 12:12:12 GMT",


"title": "Wild Child" 
} 
], 
"success": true, 

"total_movie": 1 
}
````

PATCH/Movies update movie information based on ID


Postman `PATCH https://castingagen88.herokuapp.com/movies/4`


**Permissions:**

Casting Executive


**Result:**

```` 
{ "movie":
 [
 { 
"id": 4,
"relase_date": "Mon, 01 Oct 2012 12:12:12 GMT",
"title": "New Wild Child"
 } ],
"success": true,
"updated": "4"
}
````

DELETE/Movie Delete movie bassed on ID


Postman `DELETE https://castingagen88.herokuapp.com/movies/1`

**Permissions:** 

````
Casting Executive

**Result:** 
{ 
"delete": 1,

 "success": true 
}
````

POST/Movie add new movie in the list

Postman `POST https://castingagen88.herokuapp.com/movies/create`

**Permissions:**

Casting Executive

**Result:**
````
{ "movie": [ {
 "id": 1,
 "relase_date": "Mon, 01 Oct 2012 12:12:12 GMT",
 "title": "Wild Child" 
} ], 
"success": true 
}
````

**Error Type**


Return error in JSON as the following format:

````
{ 
"error": 422, 

"message": "unprocessable",
 
"success": false
 }
````
````
{ 
"error": 404, 

"message": "Not Found",

 "success": false 
}
````

The API will return error as


422:Uunprocessable


404: Not Found


**Testing:**


Restore database by using command


Move to PostgreSQL file folder cd "C:\ProgramFiles\PostgreSQL\9.6\bin"

Enter Command for restore

`./psql.exe -U postgres -d castibg_agency_test -f D:\Backup\casting_agency_test.sql`


Auther: Mona Alahmadi
