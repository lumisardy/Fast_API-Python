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
    
@app.get("/userclass")
async def userclass():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado ningun usuario"}
    
@app.get("/userquery/")
async def user(id: int):
    return user_search
    
def user_search(id: int):
    users = filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado ningun usuario"}