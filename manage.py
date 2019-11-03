from app import app


if __name__ == "__main__":
    app.run(
        host=app.config.get('host', None) or app.config["APP_HOST"],
        port=app.config.get('port', None) or app.config["APP_PORT"],
        debug=app.config["APP_DEBUG"],
        ssl=app.config["APP_SSL"],
        workers=app.config["APP_WORKERS"],
    )