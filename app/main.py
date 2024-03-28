import uvicorn
from database import Model, engine
from fastapi import FastAPI
from models import TaskModel
from fastapi.staticfiles import StaticFiles
from routers import tasks_router
from urls import task_temp_url

app = FastAPI(
    title="TodoList",
    version="0.0.1"
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(tasks_router)
app.include_router(task_temp_url)






if __name__ == '__main__':
    #Model.metadata.create_all(engine)
    TaskModel.metadata.create_all(engine)
    print('Starting server')
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
    print('Server stopped')