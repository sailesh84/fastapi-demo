from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI application is running successfully!"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!", "status": "success"}