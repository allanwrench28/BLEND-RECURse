from fastapi import FastAPI

app = FastAPI(title="Recur API", description="Universal Programming Interface for council-driven automation.")

@app.get("/")
def read_root():
    return {"message": "Welcome to Recur API!"}
