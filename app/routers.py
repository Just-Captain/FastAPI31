from fastapi import APIRouter, Request
from schemas import TaskCreateSchema
from models import TaskModel
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select

tasks_router = APIRouter(prefix='/api/v1/tasks')


@tasks_router.post(path='/create/')# full path = /api/v1/tasks/create/
def create_task_point(request: Request, task: TaskCreateSchema):
    new_task = TaskModel(
        title=task.title,
        description=task.description,
    )
    session = Session(engine) # <- создаю сессию с БД
    session.add(new_task) # <- записывает обьект в БД
    session.commit() # <- делает сохрание
    session.close() # <- закрывает сессию
    return {"task": task}

@tasks_router.get('/list/')
def list_tasks_point(request:Request):
    session = Session(engine)
    stmt = select(TaskModel)
    print(stmt)
    """
    SELECT tasks_table.id, tasks_table.title, tasks_table.description, tasks_table.status     
    FROM tasks_table
    """
    tasks:list = session.scalars(stmt).all()
    return tasks

