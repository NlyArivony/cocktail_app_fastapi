from app.main import app

if __name__ == "__main__":
    # Do anything you want with the FastAPI app instance, or run the app using uvicorn.
    # For example, you can run it with uvicorn like this:
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
