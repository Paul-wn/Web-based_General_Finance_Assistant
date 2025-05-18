from fastapi import FastAPI , Request
from typing import Union

app = FastAPI()

@app.get("/")
def first_page():
    return {"message": "Hello, World! Eiei"} 

@app.get("/test/{id}")
def test(id: int , q: Union[str, None] = None):
    return {"ID": id , 'query': q}

@app.post("/test")
async def create_item(request: Request):
    body = await request.json()
    return {"data": body}