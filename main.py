import json
from typing import List, Union
from fastapi import FastAPI, Response, Query
from typing_extensions import Annotated
from maigret_wrapper import getJSONreportForUsername, searchMultipleUsernames
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/username/{username}")
async def get_username_report(username: str):
    data = await getJSONreportForUsername(username)
    return data
@app.get("/usernames/")
async def get_usernames_report(username: Annotated[Union[List[str], None], Query()] = None):
    username_list = list(set(username))
    data = await searchMultipleUsernames(username_list)
    return data