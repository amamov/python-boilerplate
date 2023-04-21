from uvicorn import Config, Server
from app.main import app

if __name__ == "__main__":
    config = Config(
        app=app,
        reload=True,
        host="localhost",
        port=8000,
    )
    server = Server(config)
    server.run()
