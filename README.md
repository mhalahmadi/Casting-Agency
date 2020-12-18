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


Base URL:
The APP will be run locally at http://127.0.0.:5000/
and in internet on https://castingagen88.herokuapp.com

Authentication:
This version of application dose require authentication
three type of authintaction

1-Castong assistant
-get/Actore
-Get/Movie

2-Casting diractore
-Get/Actor
-Get/Movie
-Patch/Actor
-Post/Actor
-Patch/Actor
-Delete/Actor

3-Casting Executive
-Get?Actor
-Get/Movie
-Post/Actor
-Post/Movie
-Patch/Actor
-Patch/Movie
-Delete/Actor
-Delete/Movie


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

Testing:
Restore database by using command

move to PostgreSQL file folder
cd "C:\ProgramFiles\PostgreSQL\9.6\bin"

Enter Command for restore
./psql.exe -U postgres -d castibg_agency_test -f D:\Backup\casting_agency_test.sql

Auther
Mona Alahmadi

