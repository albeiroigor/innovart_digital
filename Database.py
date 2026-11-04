import pymysql
from flask import current_app, g


class MySQL:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MYSQL_HOST", "localhost")
        app.config.setdefault("MYSQL_PORT", 3306)
        app.config.setdefault("MYSQL_USER", "root")
        app.config.setdefault("MYSQL_PASSWORD", "")
        app.config.setdefault("MYSQL_DB", "")
        app.teardown_appcontext(self._close)

    @property
    def connection(self):
        if "mysql_conn" not in g:
            cfg = current_app.config
            cursorclass = (
                pymysql.cursors.DictCursor
                if cfg.get("MYSQL_CURSORCLASS") == "DictCursor"
                else pymysql.cursors.Cursor
            )
            g.mysql_conn = pymysql.connect(
                host=cfg["MYSQL_HOST"],
                port=int(cfg["MYSQL_PORT"]),
                user=cfg["MYSQL_USER"],
                password=cfg["MYSQL_PASSWORD"],
                database=cfg["MYSQL_DB"],
                cursorclass=cursorclass,
                charset="utf8mb4",
            )
        return g.mysql_conn

    def _close(self, exception=None):
        conn = g.pop("mysql_conn", None)
        if conn is not None:
            conn.close()
