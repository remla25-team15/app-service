import os

from src.app import create_app

app = create_app()

if __name__ == "__main__":
    # Use environment config instead of hardcoded debug mode
    debug = app.config["DEBUG"]
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))

    app.run(host=host, port=port, debug=debug)
