import uvicorn
from fastapi import FastAPI, staticfiles
from app.routers.users import users_router
    
app = FastAPI()
app.include_router(users_router, tags=["Users"])
app.mount("/", staticfiles.StaticFiles(directory="app/public", html=True), name="/static")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)