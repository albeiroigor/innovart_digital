import os
import re
import time

import pymysql
from flask import current_app, g

from Config import Config


class MySQL:
    def __init__(self, app=None):
        self.schema_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "schema.sql",
        )
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MYSQL_HOST", Config.MYSQL_HOST)
        app.config.setdefault("MYSQL_PORT", Config.MYSQL_PORT)
        app.config.setdefault("MYSQL_USER", Config.MYSQL_USER)
        app.config.setdefault("MYSQL_PASSWORD", Config.MYSQL_PASSWORD)
        app.config.setdefault("MYSQL_DB", Config.MYSQL_DB)
        app.config.setdefault("MYSQL_CHARSET", Config.MYSQL_CHARSET)
        app.config.setdefault("MYSQL_INIT_RETRIES", Config.MYSQL_INIT_RETRIES)
        app.config.setdefault("MYSQL_INIT_DELAY", Config.MYSQL_INIT_DELAY)
        app.teardown_appcontext(self._close)

    @property
    def connection(self):
        if "mysql_conn" not in g:
            g.mysql_conn = self._connect(current_app.config, current_app.config["MYSQL_DB"])
        return g.mysql_conn

    def initialize_schema(self, app, retries=30, delay=2):
        last_error = None

        for attempt in range(1, retries + 1):
            try:
                self._ensure_database(app.config)
                self._run_schema(app.config)
                app.logger.info("Esquema de base de datos verificado")
                return
            except pymysql.err.OperationalError as error:
                last_error = error
                app.logger.warning(
                    "MySQL no disponible (intento %s/%s): %s",
                    attempt,
                    retries,
                    error,
                )
                if attempt < retries:
                    time.sleep(delay)

        app.logger.error("No se pudo inicializar la base de datos: %s", last_error)

    def _connect(self, config, database=None):
        return pymysql.connect(
            host=config["MYSQL_HOST"],
            port=int(config["MYSQL_PORT"]),
            user=config["MYSQL_USER"],
            password=config["MYSQL_PASSWORD"],
            database=database,
            charset=config["MYSQL_CHARSET"],
        )

    def _ensure_database(self, config):
        database = config["MYSQL_DB"]
        if not re.fullmatch(r"[A-Za-z0-9_]+", database):
            raise ValueError(f"Nombre de base de datos inválido: {database}")

        try:
            connection = self._connect(config, database)
        except pymysql.err.OperationalError as error:
            if error.args[0] != 1049:
                raise
            connection = self._connect(config)
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"CREATE DATABASE IF NOT EXISTS `{database}` "
                        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                    )
            finally:
                connection.close()
            return

        connection.close()

    def _run_schema(self, config):
        with open(self.schema_path, encoding="utf-8") as schema:
            statements = self._split_statements(schema.read())

        connection = self._connect(config, config["MYSQL_DB"])
        try:
            with connection.cursor() as cursor:
                for statement in statements:
                    cursor.execute(statement)
        finally:
            connection.close()

    def _split_statements(self, script):
        lines = [
            line
            for line in script.splitlines()
            if line.strip() and not line.strip().startswith("--")
        ]
        return [
            statement.strip()
            for statement in "\n".join(lines).split(";")
            if statement.strip()
        ]

    def _close(self, exception=None):
        connection = g.pop("mysql_conn", None)
        if connection is not None:
            connection.close()


mysql = MySQL()
