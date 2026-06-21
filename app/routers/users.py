from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from app.database.database import people
from app.functions.functions import find_person
from app.models.models import Person

router = APIRouter()

@router.get("/api/users")
async def get_people():
    return people

@router.get("/api/users/{id}")
async def get_person(id):
    person = find_person(id)
    print(person)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "User not found"}
        )
    return person

@router.post("/api/users")
async def create_person(data = Body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person

@router.put("/api/users")
async def edit_person(data = Body()):
    person = find_person(data["id"])
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "User not found"}
        )
    person.age = data["age"]
    person.name = data["name"]
    return person

@router.delete("/api/users/{id}")
async def delete_person(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            content={"message": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND
        )
    people.remove(person)
    return person
