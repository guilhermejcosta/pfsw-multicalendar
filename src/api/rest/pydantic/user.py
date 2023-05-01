from pydantic import BaseModel
from typing import Union
from datetime import datetime

class UserItem(BaseModel):
    full_name: str 
    display_name: str 
    email: str
    contact_phone: Union[int, None]
    # created_at: datetime | None = None
    # deleted_at: datetime | None = None
    # updated_at: datetime | None = None