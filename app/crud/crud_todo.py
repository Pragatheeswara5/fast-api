from app.core.database import get_db

class CRUDTodo:
    
    @staticmethod
    async def create(todo_data:dict):
        db=get_db()
        todo_data["completed"]=False
        result=await db.todos.insert_one(todo_data)
        return await db.todos.find_one({"_id":result.inserted_id})
    
    @staticmethod
    async def get_all():
        db=get_db()
        return await db.todos.find().to_list(100)
    
    @staticmethod
    async def get_by_id(todo_id):
        db=get_db()
        return await db.todos.find_one({"_id":todo_id})
    
    @staticmethod
    async def update(todo_id, data:dict):
        db=get_db()
        await db.todos.update_one(
            {"_id":todo_id},
            {"$set":data}
        )
        return await db.todos.find_one({"_id":todo_id})
    
    @staticmethod
    async def delete(todo_id):
        db=get_db()
        return await db.todos.delete_one({"_id":todo_id})