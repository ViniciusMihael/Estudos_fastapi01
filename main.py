from typing import Union
from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum
from http import HTTPStatus
from schemas import Model_Name,Item


app = FastAPI()# app será uma instancia da class fastapi



#Aqui estou trabalhando com variaveis de rota
@app.get("/models/{models_name}", status_code=HTTPStatus.OK)
async def get_model(model_name:Model_Name):
    """_summary_

    Args:
        model_name (Model_Name): _description_

    Returns:
        _type_: _description_
    """
    if model_name is Model_Name.alexnet:
        return {"model_name": model_name, "Message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name":model_name, "Message":"LeCNN all the imagens"}
    
    return{"model_name":model_name, "Message":"Have some residuals"}


@app.get("/teste/",status_code=HTTPStatus.OK) # /teste/ e uma rota
async def read_root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"Message":"Deu certo"}


#Declarando um valor padrão para a variavel "q"
@app.get("/teste/{nome}")
async def teste (q : str = Query(default=10, description="Valor predefinido")):
    return {f"O valor de q = {q}"}

#Aqui a variavel item e obrigatoria e ela herda o corpo da class Item
@app.post("/items/",status_code=HTTPStatus.CREATED)
async def create_item(item:Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.tax + item.price
        item_dict.update({
            "price_with_tax": price_with_tax
            })
    return item_dict


#Aqui a variavel "q" recebe uma lista de parametros de consulta e tem como valor padrão "None"
@app.get("/items/lista_parametros")
async def read_item(q: Union[list[str], None] = Query(default=None)):
    query_items = {"q":q}
    return query_items


#Aqui ele recebe uma lista diretamente porém não valida os dados 
@app.get("/items/lista_vazia")
async def read_items(q: list =  Query(default=[])):
    """_summary_

    Args:
        q (list, optional): _description_. Defaults to Query(default=[]).

    Returns:
        _type_: _description_
    """
    query_items = {"q": q}
    return query_items


@app.get("/items")
async def read_items(
    q: Union[str,None] = Query(
        default=None,
        alias="item-query",
        title="Query String",
        description="Query string for items to search in the database that have a good match",
        min_length=3,
        deprecated=True,
        ),
    ):
    """_summary_

    Args:
        q (Union[str,None], optional): _description_. Defaults to Query( default=None, title="Query String", description="Query string for items to search in the database that have a good match", min_length=3 ).

    Returns:
        _type_: _description_
    """
    results = {"items"[{"items_id":"Foo"},{"items_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results
   
#Teste de commit