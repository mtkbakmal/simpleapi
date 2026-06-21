from fastapi import APIRouter, Body, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.database import get_db
from app.models.models import Person

router = APIRouter(prefix="/api/users")

# Получить всех пользователей
@router.get("")
async def get_people(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person))
    people = result.scalars().all()
    return people

# Получить пользователя по ID
@router.get("/{id}")
async def get_person(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person).where(Person.id == id))
    person = result.scalar_one_or_none()
    
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return person

# Создать пользователя
@router.post("")
async def create_person(data = Body(), db: AsyncSession = Depends(get_db)):
    new_person = Person(name=data["name"], age=data["age"])
    db.add(new_person)
    await db.commit()       # Сохраняем в БД
    await db.refresh(new_person) # Загружаем сгенерированный id из БД
    return new_person

# Редактировать пользователя
@router.put("")
async def edit_person(data = Body(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person).where(Person.id == data["id"]))
    person = result.scalar_one_or_none()
    
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
    person.age = data["age"]
    person.name = data["name"]
    await db.commit()
    return person

# Удалить пользователя
@router.delete("/{id}")
async def delete_person(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person).where(Person.id == id))
    person = result.scalar_one_or_none()
    
    if person is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
    await db.delete(person)
    await db.commit()
    return {"message": f"User {id} deleted successfully"}