import os
from fastapi import APIRouter, Cookie
from fastapi.responses import FileResponse
from datetime import datetime

router = APIRouter()

PATH = "app/public/index.html"

@router.get("/")
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