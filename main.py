import uvicorn
from fastapi import FastAPI, staticfiles
from app.routers.users import users_router
from a2wsgi import ASGIMiddleware
    
app = FastAPI()
app.include_router(users_router, tags=["Users"])
app.mount("/", staticfiles.StaticFiles(directory="app/public", html=True), name="/static")

wsgi_app = ASGIMiddleware(app) #type: ignore

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)