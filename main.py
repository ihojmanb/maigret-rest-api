import json
from typing import Union
from fastapi import FastAPI, Response
from maigret_wrapper import getJSONreportForUsername
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/username/{username}")
async def get_username_report(username: str):
    data = await getJSONreportForUsername(username)
    return data