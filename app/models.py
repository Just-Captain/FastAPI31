from sqlalchemy import Boolean
from database import Model
from sqlalchemy.orm import Mapped, mapped_column

class TaskModel(Model):

    __tablename__ = 'tasks_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(Boolean(),default=False)

    def __repr__(self) -> str:
        return f"Task title='{self.title}'"

