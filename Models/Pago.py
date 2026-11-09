from Models.BaseModel import BaseModel


class Pago(BaseModel):
    table = "pagos"
    columns = (
        "id",
        "uuid",
        "hora",
        "fecha",
        "monto",
        "metodo_pago",
        "servicios_id",
        "usuarios_id",
    )
    required_fields = (
        "hora",
        "fecha",
        "monto",
        "metodo_pago",
        "servicios_id",
        "usuarios_id",
    )
