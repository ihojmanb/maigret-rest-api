import json
from typing import List, Union
from fastapi import FastAPI, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from maigret_wrapper import getJSONreportForUsername, searchMultipleUsernames
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify your frontend's address like ['http://127.0.0.1:5173']
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


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