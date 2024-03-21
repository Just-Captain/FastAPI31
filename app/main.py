from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from pydantic import BaseModel
import uvicorn
from fastapi.responses import RedirectResponse

app = FastAPI() # <- Создаем экземпляр класса FastAPI
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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
    data['host'] = HOST
    return templates.TemplateResponse(request=request, name='tasks.html', context=data)

@app.get('/tasks/create/')
def task_form_create(request:Request):
    return templates.TemplateResponse(request=request, name='task_create.html')

class Task(BaseModel):
    title:str
    description:str

@app.post('/tasks/create/')
def task_create(request:Request, task:Task):
    tasks = database.read()
    tasks['count_action']['action_tasks'] += 1
    new_task = {
        "id": tasks['count_action']['action_tasks'],
        "title": task.title,
        "description": task.description
    }
    tasks['tasks'].append(new_task)
    database.write(tasks)
    return RedirectResponse(url='/tasks/', status_code=status.HTTP_302_FOUND)



HOST = '127.0.0.1'

if __name__ == '__main__':
    print('Starting server')
    uvicorn.run('main:app', port=8000, host=HOST, reload=True)
    print('Server stopped')