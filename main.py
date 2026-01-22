from app.api import app
import uvicorn

if __name__ == "__main__":
    #ASGI webserver
    uvicorn.run(
        "app.api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )