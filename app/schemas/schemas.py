from pydantic import BaseModel, Field

class PersonCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        json_schema_extra={"error_msg": "Name should be from 3 to 30 symbols"})
    age: int = Field(
        ..., 
        ge=18, 
        lt=111,
        json_schema_extra={"error_msg": "Age should be from 18 to 110"})