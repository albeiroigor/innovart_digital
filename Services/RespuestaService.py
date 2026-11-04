from flask import current_app
from Models.Respuesta import Respuesta


class RespuestaService:
    def list(self):

        sql = "SELECT RES_ID, RES_UUID, RES_HORA, RES_DESCRIPCION, RES_FECHA FROM t_respuesta"

        c = current_app.mysql.connection.cursor()
        c.execute(sql)

        data = c.fetchall()

        lista_l = []

        for u in data:

            objeto = Respuesta(
                    u[0],
                    u[1],
                    u[2],
                    u[3],
                    u[4]
            )

            lista_l.append(objeto.to_dict())

        c.close()

        return lista_l


    def getById(self, id):

        sql = "SELECT RES_ID, RES_UUID, RES_HORA, RES_DESCRIPCION, RES_FECHA FROM t_respuesta WHERE RES_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))

        data = c.fetchone()

        c.close()

        if data is None:
            return None

        objeto = Respuesta(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
        )

        return objeto.to_dict()


    def create(self, data):

        sql = "INSERT INTO t_respuesta (RES_UUID, RES_HORA, RES_DESCRIPCION, RES_FECHA) VALUES (%s, %s, %s, %s)"

        values = (
            data.get('uuid'),
            data.get('hora'),
            data.get('descripcion'),
            data.get('fecha')
        )

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return self.getById(new_id)


    def update(self, id, data):

        sql = "UPDATE t_respuesta SET RES_UUID = %s, RES_HORA = %s, RES_DESCRIPCION = %s, RES_FECHA = %s WHERE RES_ID = %s"

        values = (
            data.get('uuid'),
            data.get('hora'),
            data.get('descripcion'),
            data.get('fecha'),
            id
        )

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        if affected == 0:
            return None

        return self.getById(id)


    def delete(self, id):

        sql = "DELETE FROM t_respuesta WHERE RES_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        return affected > 0
