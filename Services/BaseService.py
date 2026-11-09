import uuid

import pymysql
from flask import current_app


class ConflictError(Exception):
    pass


def _conflict_message(error):
    code = error.args[0] if error.args else None
    if code == 1062:
        return "El registro ya existe"
    if code == 1451:
        return "El registro tiene datos relacionados y no se puede eliminar"
    if code == 1452:
        return "El registro referenciado no existe"
    return "El registro no se pudo guardar por una restricción de la base de datos"


class CrudService:
    model = None

    @property
    def connection(self):
        return current_app.mysql.connection

    def list(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"SELECT {self.model.select_columns()} FROM {self.model.table}"
            )
            rows = cursor.fetchall()
        return [self.model.from_row(row).to_dict() for row in rows]

    def getById(self, id):
        record = self._find(id)
        return record.to_dict() if record else None

    def create(self, data):
        values = self.model.create_payload(data)
        values["uuid"] = str(uuid.uuid4())
        values = self.prepare_create(values)
        columns = ", ".join(values)
        placeholders = ", ".join(["%s"] * len(values))

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(
                    f"INSERT INTO {self.model.table} ({columns}) VALUES ({placeholders})",
                    tuple(values.values()),
                )
                self.connection.commit()
                new_id = cursor.lastrowid
            except pymysql.err.IntegrityError as error:
                self.connection.rollback()
                raise ConflictError(_conflict_message(error)) from error
            except Exception:
                self.connection.rollback()
                raise

        return self.getById(new_id)

    def update(self, id, data):
        if self._find(id) is None:
            return None

        values = self.prepare_update(self.model.update_payload(data))
        if not values:
            return self.getById(id)

        assignments = ", ".join(f"{name} = %s" for name in values)
        parameters = tuple(values.values()) + (id,)

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(
                    f"UPDATE {self.model.table} SET {assignments} "
                    f"WHERE {self.model.primary_key} = %s",
                    parameters,
                )
                self.connection.commit()
            except pymysql.err.IntegrityError as error:
                self.connection.rollback()
                raise ConflictError(_conflict_message(error)) from error
            except Exception:
                self.connection.rollback()
                raise

        return self.getById(id)

    def delete(self, id):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(
                    f"DELETE FROM {self.model.table} "
                    f"WHERE {self.model.primary_key} = %s",
                    (id,),
                )
                self.connection.commit()
                return cursor.rowcount > 0
            except pymysql.err.IntegrityError as error:
                self.connection.rollback()
                raise ConflictError(_conflict_message(error)) from error
            except Exception:
                self.connection.rollback()
                raise

    def prepare_create(self, values):
        return values

    def prepare_update(self, values):
        return values

    def _find(self, id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"SELECT {self.model.select_columns()} FROM {self.model.table} "
                f"WHERE {self.model.primary_key} = %s",
                (id,),
            )
            row = cursor.fetchone()
        return self.model.from_row(row) if row else None
