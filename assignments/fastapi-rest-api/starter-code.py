from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_input: TaskInput):
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    raise HTTPException(status_code=501, detail="Implement this endpoint")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    raise HTTPException(status_code=501, detail="Implement this endpoint")