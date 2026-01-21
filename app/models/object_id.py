from bson import ObjectId
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema

class PyObjectId(ObjectId):
    
    @classmethod
    def __get_pydantic_core_schema(
        cls, source_type, handler:GetCoreSchemaHandler
    ):
        return core_schema.union_schema([
            core_schema.is_instance_schema(ObjectId),
            core_schema.no_info_plain_validator_function(ObjectId),
        ], serialization=core_schema.to_string_ser_schema())
    
    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)