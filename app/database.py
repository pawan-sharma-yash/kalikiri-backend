from fastapi import FastAPI
# Create an instance of the FastAPI class
app = FastAPI(
    title="My First FastAPI App",
    description="This is a simple FastAPI application for learning purposes.",
    version="1.0.0"
)
# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}