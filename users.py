from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    

users_list = [User(id=1, name="Carlo",surname="Carlitos",url="https://youtube.com", age="24"),User(id=2, name="Jose manuel",surname="Josema",url="https://youtube.com", age="244"),User(id=3,name="David",surname="Darbi",url="https://youtube.com", age="64")]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Carlo","surname":"Carlitos","url":"https://youtube.com", "age":"24"},
            {"name": "Jose manuel","surname":"Josema","url":"https://youtube.com","age":"44"},
            {"name": "David","surname":"Darbi","url":"https://youtube.com","age":"64"}]
    
@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado ningun usuario"}
    

    
@app.get("/user/")
async def user(id: int):
    return user_search

@app.post("/user/")
async def user(user: User):
    if type(user_search(user.id)) is not None:
        return {"Error": "Este usuarion ya esxiste"}
    
    users_list.append(user)
    return user 
    
    
@app.put("/user/")
async def update_user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        
        print(saved_user)
        print(type(saved_user))
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
            
    if not found:
        return {"error":"No se ha encontrado ningun usuario"}
    
    return user
            
        
    


def user_search(id: int):
    users = filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return None
    
