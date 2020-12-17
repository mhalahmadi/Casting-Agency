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

postman GET https://castingagen88.herokuapp.com/actors

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

postman PATCH https://castingagen88.herokuapp.com/actors/1


{
    "actor": [
        {
            "age": "30",
            "gender": "Female",
            "id": 1,
            "name": "Emma Roberts"
        }
    ],
    "success": true,
    "total_actor": 1,
    "updated": 1
}

DELETE/Actor
delete actor based on ID

postman DELETE https://castingagen88.herokuapp.com/actors/1

{
    "delete": 1,
    "success": true
}

POST/Actor
add new actore in the list


postman POST  https://castingagen88.herokuapp.com/artors/create

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

postman GET https://castingagen88.herokuapp.com/movies

{
    "movie": [
        {
            "id": 2,
            "relase_date": "Mon, 01 Oct 2012 12:12:12 GMT",
            "title": "Wild Child"
        }
    ],
    "success": true,
    "total_movie": 1
}

PATCH/Movies
update movie information bassed on ID

Postman PATCH https://castingagen88.herokuapp.com/movies/4

{
    "movie": [
        {
            "id": 4,
            "relase_date": "Mon, 01 Oct 2012 12:12:12 GMT",
            "title": "New Wild Child"
        }
    ],
    "success": true,
    "updated": "4"



DELETE/Movie
Delete movie bassed on ID

Postman DELETE https://castingagen88.herokuapp.com/movies/1


{
    "delete": 1,
    "success": true
}


POST/Movie
add new movie in the list

Postman POST https://castingagen88.herokuapp.com/movies/create

{
    "movie": [
        {
            "id": 1,
            "relase_date": "Mon, 01 Oct 2012 12:12:12 GMT",
            "title": "Wild Child"
        }
    ],
    "success": true
}



Error Type

return error in JSoN  as the following formate:

{
    "error": 422,
    "message": "unprocessable",
    "success": false
}

{
    "error": 404,
    "message": "Not Found",
    "success": false
}

the API will return error as 

422:Uunprocessable
404: Not Found

Auther
Mona Alahmadi

