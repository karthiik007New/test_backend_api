from fastapi import FastAPI 

app = FastAPI()

@app.get("/home")
@app.post("/home")
def home():
    return "Welcome to API app!"