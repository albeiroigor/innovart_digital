from flask import current_app
from Models.Persona import Persona
import uuid

class PersonaService:
    def list(self):

        sql = """SELECT PER_ID, PER_UUID, PER_CEDULA, PER_DOCUMENTO, PER_PRIMER_NOMBRE, PER_SEGUNDO_NOMBRE, 
        PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO, PER_CORREO, PER_DIRECCION, PER_TELEFONO, PER_FECHA_NACIMIENTO FROM 
        t_persona"""

        c = current_app.mysql.connection.cursor()
        c.execute(sql)

        data = c.fetchall()

        lista_l = []

        for u in data:

            objeto = Persona(
                    u[0],
                    u[1],
                    u[2],
                    u[3],
                    u[4],
                    u[5],
                    u[6],
                    u[7],
                    u[8],
                    u[9],
                    u[10],
                    u[11]
            )

            lista_l.append(objeto.to_dict())

        c.close()

        return lista_l


    def getById(self, id):

        sql = """SELECT PER_ID, PER_UUID, PER_CEDULA, PER_DOCUMENTO, PER_PRIMER_NOMBRE, 
        PER_SEGUNDO_NOMBRE, PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO,
          PER_CORREO, PER_DIRECCION, PER_TELEFONO, PER_FECHA_NACIMIENTO FROM t_persona WHERE PER_ID = %s"""

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))

        data = c.fetchone()

        c.close()

        if data is None:
            return None

        objeto = Persona(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11]
        )

        return objeto.to_dict()


    def create(self, data):
        UUID_P = uuid.uuid4().hex  # Generar un UUID único para la persona
        sql = """INSERT INTO t_persona (PER_UUID, PER_CEDULA, PER_DOCUMENTO, PER_PRIMER_NOMBRE, PER_SEGUNDO_NOMBRE,
          PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO, PER_CORREO, PER_DIRECCION, PER_TELEFONO, PER_FECHA_NACIMIENTO) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (UUID_P, data.get('cedula'), 
                  data.get('documento'), data.get('primer_nombre'), data.get('segundo_nombre'), data.get('primer_apellido'), 
                  data.get('segundo_apellido'), data.get('correo'), data.get('direccion'), data.get('telefono'), data.get('fecha_nacimiento'),)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return self.getById(new_id)


    def update(self, id, data):

        sql = """UPDATE t_persona SET PER_UUID = %s, PER_CEDULA = %s, PER_DOCUMENTO = %s, PER_PRIMER_NOMBRE = %s, PER_SEGUNDO_NOMBRE = %s,
          PER_PRIMER_APELLIDO = %s, PER_SEGUNDO_APELLIDO = %s, PER_CORREO = %s, PER_DIRECCION = %s, PER_TELEFONO = %s, PER_FECHA_NACIMIENTO = %s 
          WHERE PER_ID = %s"""

        values = (data.get('uuid'), data.get('cedula'), data.get('documento'), data.get('primer_nombre'), data.get('segundo_nombre'),
                   data.get('primer_apellido'), data.get('segundo_apellido'), data.get('correo'), data.get('direccion'), data.get('telefono'), 
                   data.get('fecha_nacimiento'), id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, values)
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        if affected == 0:
            return None

        return self.getById(id)


    def delete(self, id):

        sql = "DELETE FROM t_persona WHERE PER_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        affected = c.rowcount

        c.close()

        return affected > 0
