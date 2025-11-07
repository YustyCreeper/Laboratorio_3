from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}


@app.get("/hello")
def hello():
    return {"message": "Hello world"}


@app.get("/test")
def hola():
    return {"message": "test endpoint"}
