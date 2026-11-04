from flask import current_app
from Models.Pago import Pago


class PagoService:
    def list(self):

        sql = "SELECT PAG_ID, PAG_UUID, PAG_HORA, PAG_FECHA, PAG_MONTO, PAG_METODO_PAGO, PAG_SER_ID, PAG_USU_ID FROM t_pago"

        c = current_app.mysql.connection.cursor()
        c.execute(sql)

        data = c.fetchall()

        lista_l = []

        for u in data:

            hora = str(u[2]) if u[2] is not None else None

            objeto = Pago(
                    u[0],
                    u[1],
                    hora,
                    u[3],
                    u[4],
                    u[5],
                    u[6],
                    u[7]
            )

            lista_l.append(objeto.to_dict())

        c.close()

        return lista_l


    def getById(self, id):

        sql = "SELECT PAG_ID, PAG_UUID, PAG_HORA, PAG_FECHA, PAG_MONTO, PAG_METODO_PAGO, PAG_SER_ID, PAG_USU_ID FROM t_pago WHERE PAG_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))

        data = c.fetchone()

        c.close()

        if data is None:
            return None

        hora = str(data[2]) if data[2] is not None else None

        objeto = Pago(
                data[0],
                data[1],
                hora,
                data[3],
                data[4],
                data[5],
                data[6],
                data[7]
        )

        return objeto.to_dict()


    def create(self, data):

        sql = "INSERT INTO t_pago (PAG_UUID, PAG_HORA, PAG_FECHA, PAG_MONTO, PAG_METODO_PAGO, PAG_SER_ID, PAG_USU_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        values = (
            data.get('uuid'),
            data.get('hora'),
            data.get('fecha'),
            data.get('monto'),
            data.get('metodo_pago'),
            data.get('ser_id'),
            data.get('usu_id')
        )

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return self.getById(new_id)


    def update(self, id, data):

        sql = "UPDATE t_pago SET PAG_UUID = %s, PAG_HORA = %s, PAG_FECHA = %s, PAG_MONTO = %s, PAG_METODO_PAGO = %s, PAG_SER_ID = %s, PAG_USU_ID = %s WHERE PAG_ID = %s"

        values = (
            data.get('uuid'),
            data.get('hora'),
            data.get('fecha'),
            data.get('monto'),
            data.get('metodo_pago'),
            data.get('ser_id'),
            data.get('usu_id'),
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

        sql = "DELETE FROM t_pago WHERE PAG_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        return affected > 0