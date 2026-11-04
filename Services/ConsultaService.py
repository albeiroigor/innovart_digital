from flask import current_app
from Models.Consulta import Consulta


class ConsultaService:
    def list(self):

        sql = "SELECT CON_ID, CON_UUID, CON_HORA, CON_FECHA, CON_MENSAJE, CON_USU_ID FROM t_consulta"

        c = current_app.mysql.connection.cursor()
        c.execute(sql)

        data = c.fetchall()

        lista_l = []

        for u in data:

            objeto = Consulta(
                    u[0],
                    u[1],
                    u[2],
                    u[3],
                    u[4],
                    u[5]
            )

            lista_l.append(objeto.to_dict())

        c.close()

        return lista_l


    def getById(self, id):

        sql = "SELECT CON_ID, CON_UUID, CON_HORA, CON_FECHA, CON_MENSAJE, CON_USU_ID FROM t_consulta WHERE CON_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))

        data = c.fetchone()

        c.close()

        if data is None:
            return None

        objeto = Consulta(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5]
        )

        return objeto.to_dict()


    def create(self, data):

        sql = "INSERT INTO t_consulta (CON_UUID, CON_HORA, CON_FECHA, CON_MENSAJE, CON_USU_ID) VALUES (%s, %s, %s, %s, %s)"

        values = (data.get('uuid'), data.get('hora'), data.get('fecha'), data.get('mensaje'), data.get('usu_id'),)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return self.getById(new_id)


    def update(self, id, data):

        sql = "UPDATE t_consulta SET CON_UUID = %s, CON_HORA = %s, CON_FECHA = %s, CON_MENSAJE = %s, CON_USU_ID = %s WHERE CON_ID = %s"

        values = (data.get('uuid'), data.get('hora'), data.get('fecha'), data.get('mensaje'), data.get('usu_id'), id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        if affected == 0:
            return None

        return self.getById(id)


    def delete(self, id):

        sql = "DELETE FROM t_consulta WHERE CON_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        return affected > 0
