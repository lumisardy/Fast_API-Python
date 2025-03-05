from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Palabra": "Hola mundo"}

@app.get("/url")
async def root():
    return {"Palabra": "Hola mundo"}