from Models.BaseModel import BaseModel


class Servicio(BaseModel):
    table = "servicios"
    columns = (
        "id",
        "uuid",
        "nombre",
        "descripcion",
        "precio",
        "tipo",
        "estado",
    )
    required_fields = ("nombre", "descripcion", "precio", "tipo", "estado")
