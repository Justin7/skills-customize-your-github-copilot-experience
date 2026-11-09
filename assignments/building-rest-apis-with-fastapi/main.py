from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task Tracker API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_task_id = 1

# Add the endpoints described in the assignment.
# FastAPI's interactive API documentation is available at /docs when the app is running.
