from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import json
from pydantic import BaseModel
import uvicorn

app = FastAPI() # <- Создаем экземпляр класса FastAPI
templates = Jinja2Templates(directory="templates")

class DatabaseJson:
    def __init__(self, name_db) -> None:
        self.__name_db = name_db
    
    def name_db(self) -> str:
        return self.__name_db
    
    def read(self) -> dict:
        with open(self.__name_db, 'r', encoding='utf-8') as db:
            return json.load(db)
    
    def write(self, data:dict) -> None:
        with open(self.__name_db, 'w', encoding='utf-8') as db:
            json.dump(data, db, ensure_ascii=False)

database = DatabaseJson('database.json')


@app.get('/tasks/')
def get_tasks(request:Request):
    data = database.read()
    return templates.TemplateResponse(request=request, name='tasks.html', context=data)

@app.get('/tasks/create/')
def task_form_create(request:Request):
    return templates.TemplateResponse(request=request, name='task_create.html')

class Task(BaseModel):
    title:str
    description:str


@app.post('/tasks/')
def post_task(request:Request, task:Task):
    print(task)
    data = database('database.json', 'r')
    return templates.TemplateResponse(request=request, name='tasks.html', context=data)


# uvicorn main:app --reload

if __name__ == '__main__':
    print('Starting server')
    uvicorn.run('main:app', port=8000, reload=True)
    print('Server stopped')