from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World2"}

"""
uvicorn src.api:app --reload
"""