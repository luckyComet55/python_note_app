from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from uuid import uuid4

class Task(BaseModel):
    id: str = Field(default_factory=lambda:uuid4())
    name: str
    description: str | None = None
    time_start: datetime = Field(default_factory=lambda:datetime.today())
    parent_id: str | None = None
    child_task_list: List['Task'] = []