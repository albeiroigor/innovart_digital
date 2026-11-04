class Pago:

    def __init__(
        self,
        id,
        uuid,
        hora,
        fecha,
        monto,
        metodo_pago,
        ser_id,
        usu_id
    ):

        self.pag_id = id
        self.pag_uuid = uuid
        self.pag_hora = hora
        self.pag_fecha = fecha
        self.pag_monto = monto
        self.pag_metodo_pago = metodo_pago
        self.pag_ser_id = ser_id
        self.pag_usu_id = usu_id

    def to_dict(self):

        return {
            "id": self.pag_id,
            "uuid": self.pag_uuid,
            "hora": self.pag_hora,
            "fecha": self.pag_fecha,
            "monto": self.pag_monto,
            "metodo_pago": self.pag_metodo_pago,
            "ser_id": self.pag_ser_id,
            "usu_id": self.pag_usu_id
        }
