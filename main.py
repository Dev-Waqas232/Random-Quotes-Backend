from fastapi import FastAPI
from typing import Optional

app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
