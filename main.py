from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def add():
    return {"result": "my name isAaradhy Srivastava and I am from India.. pursuing B.Tech from GL bajaj institute of technology and management..I love coding and problem solving.. "}
