from flask import jsonify, request
from Services.AgendaService import AgendaService
from App import mysql
import uuid

class AgendaController:

    service = AgendaService()

    def list(self):  #listar la agenda

        cursor = mysql.connection.cursor()

        sql = """
            SELECT
                AGE_ID,
                AGE_UUID,
                AGE_FECHA,
                AGE_HORA,
                AGE_USU_ID,
                AGE_SER_ID,
                AGE_PAG_ID
            FROM T_AGENDA
        """

        cursor.execute(sql)

        agendas = cursor.fetchall()

        cursor.close()

        resultado = []

        for agenda in agendas:

            resultado.append({
                "id": agenda[0],
                "uuid": agenda[1],
                "fecha":agenda[2],
                "hora": agenda[3],
                "usuario_id": agenda[4],
                "servicio_id": agenda[5],
                "pago_id":agenda[6]
            })

        return jsonify(resultado), 200


    def get(self, id):     #obtener una agenda
        cursor = mysql.connection.cursor()

        sql = """
            SELECT
                AGE_ID,
                AGE_UUID,
                AGE_FECHA,
                AGE_HORA,
                AGE_USU_ID,
                AGE_SER_ID
            FROM T_AGENDA
            WHERE AGE_ID = %s
        """

        cursor.execute(sql, (id,))

        agenda = cursor.fetchone()

        cursor.close()

        if agenda is None:

            return jsonify({
                "mensaje": "Agenda no encontrada"
            }), 404

        resultado = {
            "id": agenda[0],
            "uuid": str(agenda[1]),
            "fecha": str(agenda[2]),
            "hora": str(agenda[3]),
            "usuario_id": agenda[4],
            "servicio_id": agenda[5]
        }

        return jsonify(resultado), 200


    def create(self):  #Crear una agenda
        data = request.get_json()

        if not data:

            return jsonify({
                "mensaje": "No se recibieron datos"
            }), 400

        fecha = data.get("fecha")
        hora = data.get("hora")
        usuario_id = data.get("usuario_id")
        servicio_id = data.get("servicio_id")

        if not fecha or not hora or not usuario_id or not servicio_id:

            return jsonify({
                "mensaje": "Todos los campos son obligatorios"
            }), 400

        agenda_uuid = str(uuid.uuid4())

        cursor = mysql.connection.cursor()

        sql = """
            INSERT INTO T_AGENDA
            (
                AGE_UUID,
                AGE_FECHA,
                AGE_HORA,
                AGE_USU_ID,
                AGE_SER_ID
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                agenda_uuid,
                fecha,
                hora,
                usuario_id,
                servicio_id
            )
        )

        mysql.connection.commit()

        nuevo_id = cursor.lastrowid

        cursor.close()

        return jsonify({
            "mensaje": "Agenda creada correctamente",
            "id": nuevo_id,
            "uuid": agenda_uuid
        }), 201


    def update(self, id):
        data = request.get_json()

        if not data:

            return jsonify({
                "mensaje": "No se recibieron datos"
            }), 400

        fecha = data.get("fecha")
        hora = data.get("hora")
        usuario_id = data.get("usuario_id")
        servicio_id = data.get("servicio_id")

        cursor = mysql.connection.cursor()

        sql = """
            UPDATE T_AGENDA
            SET
                AGE_FECHA = %s,
                AGE_HORA = %s,
                AGE_USU_ID = %s,
                AGE_SER_ID = %s
            WHERE AGE_ID = %s
        """

        cursor.execute(
            sql,
            (
                fecha,
                hora,
                usuario_id,
                servicio_id,
                id
            )
        )

        mysql.connection.commit()

        filas = cursor.rowcount

        cursor.close()

        if filas == 0:

            return jsonify({
                "mensaje": "Agenda no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Agenda actualizada correctamente"
        }), 200



    def delete(self, id):

        cursor = mysql.connection.cursor()

        sql = """
            DELETE FROM T_AGENDA
            WHERE AGE_ID = %s
        """

        cursor.execute(sql, (id,))

        mysql.connection.commit()

        filas = cursor.rowcount

        cursor.close()

        if filas == 0:

            return jsonify({
                "mensaje": "Agenda no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Agenda eliminada correctamente"
        }), 200
