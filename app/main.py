from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json
from pydantic import BaseModel

app = FastAPI() # <- Создаем экземпляр класса FastAPI
templates = Jinja2Templates(directory="templates")

def database(name_db, mode, data=None):
    if mode == 'r':
        with open(name_db, mode, encoding='utf-8') as db:
            return json.load(db)
    elif mode == 'w':
        with open(name_db, mode, encoding='utf-8') as db:
            json.dump(data, db)

@app.get('/tasks/')
def get_tasks(request:Request):
    data = database('database.json', 'r')
    return templates.TemplateResponse(request=request, name='tasks.html', context=data)

class Task(BaseModel):
    title:str
    description:str


@app.post('/tasks/')
def post_task(request:Request, task:Task):
    print(task)

    data = database('database.json', 'r')
    return templates.TemplateResponse(request=request, name='tasks.html', context=data)


# uvicorn main:app --reload