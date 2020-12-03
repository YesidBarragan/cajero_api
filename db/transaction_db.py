from datetime import datetime
from pydantic import BaseModel

#Definición de TransactionInDB
class TransactionInDB(BaseModel): #TransactionInDB extiende de BaseModel
    id_transaction: int = 0 #Se define id_transaction como int
    username: str #Se define username como str
    date: datetime = datetime.now() #Se define date como datetime     ATRIBUTOS
    value: int #Se define value como int
    actual_balance: int #Se define id_transaction como int

#Definición de la base de datos ficticia
database_transactions = [] #Lista vacia
generator = {"id":0} #Diccionario, inicia en 1, autoincremental

#Definición de una funcion sobre la base de datos ficticia
def save_transaction(transaction_in_db: TransactionInDB): #Guarda cada una de las transacciones
    generator["id"] = generator["id"] + 1 #Guarda un nuevo ID
    transaction_in_db.id_transaction = generator["id"] #Pone un ID a la transacción
    database_transactions.append(transaction_in_db) 
    return transaction_in_db