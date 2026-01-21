from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.services.todo_service import TodoService

router=APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=TodoResponse)
async def create(todo:TodoCreate):
    return await TodoService.create_todo(todo)

@router.get("/", response_model=list[TodoResponse])
async def get_all():
    return await TodoService.list_todos()

@router.get("/{todo_id}", response_model=TodoResponse)
async def get(todo_id:str):
    todo=await TodoService.get_todo(ObjectId(todo_id))
    if not todo:
        raise HTTPException(404, "Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
async def update(todo_id:str, todo:TodoUpdate):
    updated=await TodoService.update_todo(ObjectId(todo_id), todo)
    if not updated:
        raise HTTPException(404, "Todo not found")
    return updated

@router.delete("/{todo_id}")
async def delete(todo_id:str):
    await TodoService.delete_todo(ObjectId(todo_id))
    return {"message":"Todo deleted"}