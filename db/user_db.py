from typing import Dict
from pydantic import BaseModel

#Definición de UserInDB
class UserInDB(BaseModel): #UserInDB extiende de BaseModel
    username: str #Se define username como str
    password: str #Se define password como str   ATRIBUTOS
    balance: int #Se define balance como int

#Definición de la base de datos ficticia
database_users = Dict[str, UserInDB] #Diccionario Key=str, Value=UserInDB
# **Mapeo de los usuarios
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),

    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000})
}
#Definición de funciones sobre la base de datos ficticia
def get_user(username: str):#Funcion para obtener los datos del usuario al recibir un str username
    if username in database_users.keys():#.keys() me trae las Keys del diccionario
        return database_users[username]#Retorna el Value con la Key de database_users
    else:
        return None#Retorna nada

def update_user(user_in_db: UserInDB):#Se recibe un dato user_in_db de tipo UserInDB
    database_users[user_in_db.username] = user_in_db
    return user_in_db