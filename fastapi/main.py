from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "LOLO"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/Gaya/{age}")
def read_item(age: int, classe: Union[str, None] = None):
    return {"age": age, "classe": classe}
