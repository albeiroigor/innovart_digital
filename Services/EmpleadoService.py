from flask import current_app
from Models.Empleado import Empleado


class EmpleadoService:
    def list(self):

        sql = "SELECT EMP_ID, EMP_UUID, EMP_ROL_ID, EMP_RES_ID, EMP_PER_ID, EMP_SER_ID FROM t_empleado"

        c = current_app.mysql.connection.cursor()
        c.execute(sql)

        data = c.fetchall()

        lista_l = []

        for u in data:

            objeto = Empleado(
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

        sql = "SELECT EMP_ID, EMP_UUID, EMP_ROL_ID, EMP_RES_ID, EMP_PER_ID, EMP_SER_ID FROM t_empleado WHERE EMP_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))

        data = c.fetchone()

        c.close()

        if data is None:
            return None

        objeto = Empleado(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5]
        )

        return objeto.to_dict()


    def create(self, data):

        sql = "INSERT INTO t_empleado (EMP_UUID, EMP_ROL_ID, EMP_RES_ID, EMP_PER_ID, EMP_SER_ID) VALUES (%s, %s, %s, %s, %s)"

        values = (data.get('uuid'), data.get('rol_id'), data.get('res_id'), data.get('per_id'), data.get('ser_id'),)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return self.getById(new_id)


    def update(self, id, data):

        sql = "UPDATE t_empleado SET EMP_UUID = %s, EMP_ROL_ID = %s, EMP_RES_ID = %s, EMP_PER_ID = %s, EMP_SER_ID = %s WHERE EMP_ID = %s"

        values = (data.get('uuid'), data.get('rol_id'), data.get('res_id'), data.get('per_id'), data.get('ser_id'), id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        if affected == 0:
            return None

        return self.getById(id)


    def delete(self, id):

        sql = "DELETE FROM t_empleado WHERE EMP_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        return affected > 0
