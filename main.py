import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1",
                port=8000, reload=True)
    # we will run app.py, and "app.app:app" we set app.py to be run as the main app
    # reload= True is only for development, in production we set it to false

