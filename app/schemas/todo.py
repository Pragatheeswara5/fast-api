from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from app.models.object_id import PyObjectId

class TodoCreate(BaseModel):
    title:str
    description:Optional[str]=None
    
class TodoUpdate(BaseModel):
    title:Optional[str]
    description:Optional[str]
    completed:Optional[bool]
    
class TodoResponse(BaseModel):
    id:PyObjectId=Field(alias="_id")
    title:str
    description:str | None
    completed:bool
    
    model_config={
        "populate_by_name":True,
        "json_encoders":{ObjectId:str},
        "arbitrary_types_allowed": True
    }
