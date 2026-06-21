from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from app.database.database import people
from app.functions.functions import find_person
from app.models.models import Person

users_router = APIRouter()

@users_router.get("/api/users")
def get_people():
    return people

@users_router.get("/api/users/{id}")
def get_person(id):
    person = find_person(id)
    print(person)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "User not found"}
        )
    return person

@users_router.post("/api/users")
def create_person(data = Body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person

@users_router.put("/api/users")
def edit_person(data = Body()):
    person = find_person(data["id"])
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "User not found"}
        )
    person.age = data["age"]
    person.name = data["name"]
    return person

@users_router.delete("/api/users/{id}")
def delete_person(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            content={"message": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND
        )
    people.remove(person)
    return person
