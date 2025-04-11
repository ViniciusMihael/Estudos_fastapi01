from enum import Enum
from fastapi import Query
from pydantic import BaseModel
from typing import Union


class Model_Name(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Union[str,None] = Query(default="Esta e a descrição")
    price: float
    tax: Union[float,None] = Query(default=None)