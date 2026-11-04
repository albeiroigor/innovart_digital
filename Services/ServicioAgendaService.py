from flask import current_app
from Models.ServicioAgenda import ServicioAgenda


class ServicioAgendaService:
    def list(self):

        sql = "SELECT SER_AGE_ID, SER_AGE_UUID, SER_AGE_SER_ID, SER_AGE_AGE_ID FROM t_servicio_agenda"

        c = current_app.mysql.connection.cursor()
        c.execute(sql)

        data = c.fetchall()

        lista_l = []

        for u in data:

            objeto = ServicioAgenda(
                    u[0],
                    u[1],
                    u[2],
                    u[3]
            )

            lista_l.append(objeto.to_dict())

        c.close()

        return lista_l


    def getById(self, id):

        sql = "SELECT SER_AGE_ID, SER_AGE_UUID, SER_AGE_SER_ID, SER_AGE_AGE_ID FROM t_servicio_agenda WHERE SER_AGE_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))

        data = c.fetchone()

        c.close()

        if data is None:
            return None

        objeto = ServicioAgenda(
                data[0],
                data[1],
                data[2],
                data[3]
        )

        return objeto.to_dict()


    def create(self, data):

        sql = "INSERT INTO t_servicio_agenda (SER_AGE_UUID, SER_AGE_SER_ID, SER_AGE_AGE_ID) VALUES (%s, %s, %s)"

        values = (data.get('uuid'), data.get('ser_id'), data.get('age_id'),)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return self.getById(new_id)


    def update(self, id, data):

        sql = "UPDATE t_servicio_agenda SET SER_AGE_UUID = %s, SER_AGE_SER_ID = %s, SER_AGE_AGE_ID = %s WHERE SER_AGE_ID = %s"

        values = (data.get('uuid'), data.get('ser_id'), data.get('age_id'), id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        if affected == 0:
            return None

        return self.getById(id)


    def delete(self, id):

        sql = "DELETE FROM t_servicio_agenda WHERE SER_AGE_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        return affected > 0
