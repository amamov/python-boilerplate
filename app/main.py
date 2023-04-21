from fastapi import FastAPI
from .database import wks
from . import schema
from .lib import convert_dict_to_row
from .table import UserTable
from uuid import uuid4

app = FastAPI()


@app.get("/")
def read_root():
    return wks.get_all_records()


@app.get("/users/{user_id}")
def get_user(user_id: str):
    users = wks.get_all_records()
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "user not found"}


@app.post("/users/")
def create_user(user: schema.UserCreate):
    row = convert_dict_to_row(
        {**user.dict(), "id": str(uuid4()), "is_active": True}, UserTable
    )
    wks.append_row(row)
    return {"success": True}
