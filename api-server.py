from fastapi import FastAPI

app = FastAPI(title="My FastAPI App")

@app.get("/")
def read_root():
    return {"message": "404"}
