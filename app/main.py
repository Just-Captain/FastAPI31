from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json

from pydantic import BaseModel

app = FastAPI() # <- Создаем экземпляр класса FastAPI
templates = Jinja2Templates(directory="templates")
"comment"
@app.get('/')
def task_list(request: Request):
    with open('database.json', 'r', encoding='utf-8') as db:
        db:dict = json.load(db)
        print(db)
        context = db
    return templates.TemplateResponse(request=request,
                                    name='task_list.html',
                                    context=context)


class Task(BaseModel):
    title:str
    description:str

@app.get('/task_create/')
def task_create(request:Request):
    return templates.TemplateResponse(request=request, name='task_create.html')

@app.post('/task_create/')
def task_create(request:Request, task:Task):
    print(task)
    return task
"""
{"detail":[{"type":"model_attributes_type","loc":["body"],
"msg":"Input should be a valid dictionary or object to extract fields from",
"input":"title=sadasd&description=asdsad",
"url":"https://errors.pydantic.dev/2.6/v/model_attributes_type"}]}
"""

# uvicorn main:app --reload