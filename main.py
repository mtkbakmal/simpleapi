import uvicorn, os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.users import router as users_router
from app.routers.pages import router as pages_router
    
app = FastAPI()
app.include_router(pages_router, tags=["Pages"])
app.include_router(users_router, tags=["Users"])

if os.path.exists("app/public"):
    app.mount("/public", StaticFiles(directory="app/public"), name="public")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)