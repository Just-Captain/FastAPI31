from fastapi import APIRouter, Request
from schemas import TaskCreateSchema

tasks_router = APIRouter(prefix='/api/v1/tasks')


@tasks_router.post(path='/create/')# full path = /api/v1/tasks/create/
def create_task_point(request: Request, task: TaskCreateSchema):
    return {"message": "end-pont work"}