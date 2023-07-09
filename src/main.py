from fastapi import FastAPI
from typing import List
from src.model.task import Task

app = FastAPI()

@app.get('/')
async def root():
    return 'Ok'

@app.post('/set-new-task/')
async def set_new_task(task: Task) -> List[Task]:
    task_list: List[Task] = []

    def extract_nested(inner_task: Task):
        for inner_child in inner_task.child_task_list:
            inner_child.parent_id = inner_task.id
            task_list.append(extract_nested(inner_child))
        
        inner_task.child_task_list = None
        return inner_task

    task_list.append(extract_nested(task))
    task_list.sort(key=lambda t: t.time_start)
    return task_list