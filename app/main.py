import uvicorn
from database import Model, engine
from fastapi import FastAPI
from models import TaskModel

app = FastAPI(
    title="TodoList",
    version="0.0.1"
)


if __name__ == '__main__':
    #Model.metadata.create_all(engine)
    TaskModel.metadata.create_all(engine)
    print('Starting server')
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
    print('Server stopped')