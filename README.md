# Maigret REST API

## Description

A minimal REST API for making queries with Maigret OSINT library.

It currently support one query at a time for one username.

## TODO
* add querying multiple usernames 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ihojmanb/maigret-rest-api
    ```

2. Navigate to the project directory:

    ```bash
    cd maigret-rest-api
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the rest application:

    ```bash
    uvicorn main:app --reload
    ```
    This should run the app on http://127.0.0.1:8000
2. to get a username information:
```bash
GET http://127.0.0.1:8000/username/some_username
```

