from fastapi import FastAPI, HTTPException, status
import requests

from config import settings

app = FastAPI()


@app.get("/")
async def home():
    return {"message": f"Server is running on {settings.settings.PORT}"}


@app.get("/quote")
async def get_quote():
    api_url = settings.settings.QUOTE_URL
    if not api_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="API url for quotes API is not found",)

    try:
        response = requests.get(settings.settings.QUOTE_URL)
        # Raise an exception for bad status if API returned a bad response
        response.raise_for_status()

        data = response.json()

        return {"ok": True, "data": data}

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data {e}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port={
                settings.settings.PORT | 8000})
