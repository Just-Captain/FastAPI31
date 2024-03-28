from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


task_temp_url = APIRouter(tags=["task"])
template = Jinja2Templates(directory='templates')


@task_temp_url.get(path='/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='index.html',
    )
