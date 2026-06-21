import uvicorn, os
from fastapi import FastAPI, Cookie
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from app.routers.users import users_router
    
app = FastAPI()
app.include_router(users_router, tags=["Users"])

PATH = "app/public/index.html"

if os.path.exists("public"):
    app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/")
async def root(last_visit: str | None = Cookie(default=None)):
    if not os.path.exists(PATH):
        return {"error": f"File {PATH} is not found!"}
    if last_visit is None:
        now = datetime.now().isoformat()
        response = FileResponse(PATH)
        response.set_cookie(key="last_visit", value=now)
        return response
    else:
        return FileResponse(PATH)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)