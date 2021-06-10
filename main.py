from fastapi import FastAPI, Request

app = FastAPI(title="Fast API on Linux")


@app.get("/")
async def root():
    return {"message": "Hello FAst API "}

@app.get("/get")
async def get_name(name:str):
    return {"name": name}