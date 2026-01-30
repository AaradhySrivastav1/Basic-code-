from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def add():
    return {"result": 2 + 2}


