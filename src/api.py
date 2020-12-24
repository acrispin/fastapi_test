from enum import Enum
from typing import Optional
from fastapi import FastAPI
from src.log import setup_custom_logger

logger = setup_custom_logger(__name__)


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logger.info("startup_event.")


@app.get("/")
async def root():
    logger.info("root.")
    return {"message": "Hello World."}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    /items/832
    """
    logger.info(f"items: {item_id}")
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    /users/user348
    """
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    /models/resnet
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    /files//home/path/code
    """
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item_array(skip: int = 0, limit: int = 10):
    """
    /items/?skip=0&limit=10
    """
    return fake_items_db[skip: skip + limit]


@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: Optional[str] = None):
    """
    /items2/item123?q=other
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items3/{item_id}")
async def read_item3(item_id: str, q: Optional[str] = None, short: bool = False):
    """
    /items3/foo?short=1
    /items3/foo?short=True
    /items3/foo?short=true
    /items3/foo?short=on
    /items3/foo?short=yes
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    """
    /users/9000/items/item1200?q=other&short=false
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items/detail/{item_id}")
async def read_user_item2(
        item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    """
    /items/detail/item1200?needy=sooooneedy
    /items/detail/item1200?needy=sooooneedy&skip=15&limit=10

    :param item_id: item id
    :param needy: a required str
    :param skip: an int with a default value of 0
    :param limit: an optional int
    :return: item detail
    """
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


"""
# No usar flag --reload por problemas de archivos logs, 
# Solo usar --reload-dir en desarrollo
uvicorn src.api:app --reload-dir src/ --debug
uvicorn src.api:app --debug --reload-dir src/
"""
