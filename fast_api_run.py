from fast_app import app as app 
if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app,host="0.0.0.0",port =8000,timeout_keep_alive=200)