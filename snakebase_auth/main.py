from typing import Any
from pydantic import BaseModel, Field
from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel, Field as SQLField

app = FastAPI()
engine = create_engine("sqlite:///db.sqlite")


class Settings(BaseModel):
    autoconfirm: bool = False
    disable_signup: bool = False
    external: dict[str, bool] = {}


@app.get("/settings")
async def settings() -> Settings:
    return Settings()


class Invite(BaseModel):
    email: str


@app.post("/invite")
async def invite(data: Invite):
    pass


class Signup(BaseModel):
    email: str
    password: str


@app.post("/signup")
async def signup(data: Signup):
    pass


@app.post("/token")
async def token(grant_type: str, username: str | None = None, password: str | None = None, refresh_token: str | None = None, code: str | None = None):
    pass


class Recover(BaseModel):
    email: str


@app.post("/recover")
async def recover(data: Recover):
    pass


class Verify(BaseModel):
    type: str
    token: str
    password: str | None = None


@app.post("/verify")
async def verify(data: Verify):
    pass


@app.post("/logout")
async def logout():
    pass


@app.get("/user")
async def get_user():
    pass


class UpdateUser(BaseModel):
    email: str | None = None
    password: str | None = None
    data: dict | None = None


@app.put("/user")
async def update_user(data: UpdateUser):
    pass
