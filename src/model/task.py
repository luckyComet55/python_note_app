from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from uuid import uuid4, UUID

class Task(BaseModel):
    id: UUID = Field(default_factory=lambda:uuid4())
    name: str
    description: str | None = None
    time_start: datetime
    parent_id: UUID | None = None
    child_task_list: List['Task'] | None = []