from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def add():
    return {"result": 2 + 2, "my name is Aaradhy Srivastava.. I am Btech studnet... and i am learning AIML "}

