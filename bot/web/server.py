from flask import Flask, render_template
from uvicorn import Config as uvicorn_config, Server as uvicorn_server
from uvicorn.middleware.wsgi import WSGIMiddleware

from bot import main_loop, config
from bot.log_config import setup_logging

flask_app = Flask(__name__)

@flask_app.route('/')
def homepage():
    return render_template("status.html")

async def run_server():
    asgi_flask_app = WSGIMiddleware(flask_app)
    server_config = uvicorn_config(
        asgi_flask_app,
        host='0.0.0.0',
        port=config.PORT,
        log_level=config.LOG_LEVEL,
        access_log=False
    )
    server = uvicorn_server(server_config)
    setup_logging()
    await server.serve()