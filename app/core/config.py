import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME="Todo API"
    MONGODB_URI=os.getenv("MONGODB_URI")
    DATABASE_NAME=os.getenv("DATABASE_NAME")
    
    
settings=Settings()

#ptwkarl_db_user
#