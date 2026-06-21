from app.database.database import people

def find_person(id):
    for person in people:
        if person.id == id:
            return person
    return None