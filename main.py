from fastapi import FastAPI
from typing import Optional

from config import settings

app = FastAPI()


@app.get("/")
async def home():
    return {"message": f"Server is running on {settings.settings.PORT}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port={
                settings.settings.PORT | 8000})
