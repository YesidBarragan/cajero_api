from pydantic import BaseModel

#Definición de los modelos de estado
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    balance: int