from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de Usuario
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Lista simulada de usuarios
users_list = [
    User(id=1, name="Carlo", surname="Carlitos", url="https://youtube.com", age=24),
    User(id=2, name="Jose manuel", surname="Josema", url="https://youtube.com", age=244),
    User(id=3, name="David", surname="Darbi", url="https://youtube.com", age=64)
]

# Obtener todos los usuarios (JSON)
@app.get("/usersjson")
async def usersjson():
    return [
        {"name": "Carlo", "surname": "Carlitos", "url": "https://youtube.com", "age": 24},
        {"name": "Jose manuel", "surname": "Josema", "url": "https://youtube.com", "age": 44},
        {"name": "David", "surname": "Darbi", "url": "https://youtube.com", "age": 64}
    ]

# Obtener todos los usuarios
@app.get("/users")
async def users():
    return users_list

# Buscar un usuario por ID (Ruta con ID)
@app.get("/user/{id}")
async def get_user_by_id(id: int):
    user = user_search(id)
    if user:
        return user
    else:
        return {"error": "No se ha encontrado ningún usuario"}

# Buscar un usuario por ID (Query Param)
@app.get("/user/")
async def get_user(id: int):
    user = user_search(id)
    if user:
        return user
    else:
        return {"error": "No se ha encontrado ningún usuario"}

# Crear un nuevo usuario
@app.post("/user/")
async def create_user(user: User):
    if user_search(user.id) is not None:
        return {"Error": "Este usuario ya existe"}

    users_list.append(user)
    return user

# Actualizar un usuario existente
@app.put("/user/")
async def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return {"message": "Usuario actualizado exitosamente", "user": user}

    return {"error": "No se ha encontrado ningún usuario"}


# Borrar usuarios segun el id introducido

@app.delete("/user/{id}")
async def user(id: int):
    
    borrado = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            
            borrado = True

    if not borrado:
        return {"Error":"No ha podido eliminarse el usuario"}

# Función para buscar usuarios por ID
def user_search(id: int):
    users = filter(lambda user: user.id == id, users_list)
    users = list(users)
    if users:
        return users[0]
    return None
