""" 
    Model for the tasks
"""

from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, datetime
from enum import Enum

class Status(Enum):
    TODO = "todo"
    INPROGRESS = "doing"
    DONE = "done"

class TaskBase(BaseModel):
    title : str
    description: str
    created: datetime = datetime.now()
    due_date: Optional[datetime]
    status : Status = Status.TODO

class TaskCreate(TaskBase):

    @validator("due_date", pre=True, always=True)
    def end_date_must_be_after_start_date(cls, due_date, values):
        """Ensure the end date of the sprint is after the start date."""
        start_date = values.get("start_date")
        
        if isinstance(start_date, str):
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        else:
            start_date_obj = start_date

        # Ensure end_date is a datetime.date object
        if isinstance(due_date, str):
            end_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            end_date_obj = due_date

        if start_date and end_date_obj <= start_date_obj:
            raise ValueError("end_date must be after start_date")
        return end_date_obj

