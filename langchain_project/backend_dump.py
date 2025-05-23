from fastapi import FastAPI , Request , Depends 
from typing import Union
# from pydantic import BaseModel

from models import GeneratedDB , SQLALCHEMY_DATABASE_URL , engine , SessionLocal , Session
from schemas import Generate , GenerateCreate , GenerateResponse 
from utils import Ollama

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate" , response_model=GenerateResponse)
def create_item(item: GenerateCreate , db: Session = Depends(get_db)):
    generate = Ollama()
    generated = generate.generate(item.prompt)
    item.inference = generated

    db_item = GeneratedDB(**item.model_dump()) 
    db.add(db_item)
    db.commit() 
    db.refresh(db_item)
    # print(item.name , item.price)
    return db_item 

# @app.get("/")
# def first_page(): 
#     return {"message": "Hello, World! Eiei"} 

# @app.get("/test/{id}")
# def test(id: int , q: Union[str, None] = None):
#     return {"ID": id , 'query': q}
 

# @app.put("/test/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item_body  ": item}
 