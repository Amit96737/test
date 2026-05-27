from typing import Optional

from fastapi import FastAPI

from auth import main as auth_main

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

app.include_router(auth_main.router, prefix="/api/v1")