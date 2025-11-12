from pydantic import BaseModel

class Get_bli(BaseModel):
    client:str

class Create_bli(BaseModel):
    client:str
    message:str
    

