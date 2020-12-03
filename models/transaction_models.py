from pydantic import BaseModel
from datetime import datetime

#Definición de los modelos de estado
class TransactionIn(BaseModel): #Datos que necesito al iniciar la transacción
    username: str
    value: int

class TransactionOut(BaseModel): #Datos que necesito al finalizar la transacción
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int