from typing import Optional

from fastapi import FastAPI, Request
from auth import main as auth_main
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

app.include_router(auth_main.router, prefix="/api/v1")