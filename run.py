import os

from dotenv import load_dotenv
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from app import create_app

load_dotenv()

app = create_app()
application = DispatcherMiddleware(Flask("dummy"), {"/app": app})
if __name__ == "__main__":

    debug = app.config["DEBUG"]
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))

    run_simple(host, port, application, use_reloader=debug, use_debugger=debug)
