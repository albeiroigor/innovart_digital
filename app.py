import os

from flask import Flask, current_app
from flask_cors import CORS

from Config import Config
from Database import mysql


def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)
    app.mysql = mysql
    mysql.initialize_schema(
        app,
        retries=app.config["MYSQL_INIT_RETRIES"],
        delay=app.config["MYSQL_INIT_DELAY"],
    )

    CORS(app)

    from Routes import loadRoutes

    loadRoutes(app)

    @app.route("/")
    def home():
        return {"mensaje": "API Innovart Digital funcionando"}, 200

    @app.route("/health")
    def health():
        try:
            with current_app.mysql.connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return {"status": "ok", "database": "connected"}, 200
        except Exception as error:
            return {
                "status": "error",
                "database": "disconnected",
                "detail": str(error),
            }, 503

    return app


app = createApp()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, host="0.0.0.0", port=port)
