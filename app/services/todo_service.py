from app.crud.crud_todo import CRUDTodo

class TodoService:
    
    @staticmethod
    async def create_todo(todo):
        return await CRUDTodo.create(todo.dict())
    
    @staticmethod
    async def list_todos():
        return await CRUDTodo.get_all()
    
    @staticmethod
    async def get_todo(todo_id):
        return await CRUDTodo.get_by_id(todo_id)
    
    @staticmethod
    async def update_todo(todo_id, todo):
        return await CRUDTodo.update(todo_id, todo.dict(exclude_unset=True))
    
    @staticmethod
    async def delete_todo(todo_id):
        return await CRUDTodo.delete(todo_id)