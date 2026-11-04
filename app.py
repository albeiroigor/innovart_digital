import os

from Database import MySQL
from flask import Flask, current_app, jsonify
from flask_cors import CORS

from Config import Config

mysql = MySQL()


def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)
    app.mysql = mysql

    CORS(app)

    from Routes import loadRoutes

    loadRoutes(app)

    @app.route("/")
    def home():
        return {"mensaje": "API Innovart Digital funcionando"}, 200

    @app.route("/health")
    def health():
        try:
            cur = current_app.mysql.connection.cursor()
            cur.execute("SELECT 1")
            cur.close()
            return {"status": "ok", "database": "connected"}, 200
        except Exception as e:
            return {
                "status": "error",
                "database": "disconnected",
                "detail": str(e)
            }, 503

    return app


app = createApp()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, host="0.0.0.0", port=port)
