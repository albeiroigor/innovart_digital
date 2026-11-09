from Models.BaseModel import BaseModel


class Respuesta(BaseModel):
    table = "respuestas"
    columns = ("id", "uuid", "hora", "descripcion", "fecha")
    required_fields = ("hora", "descripcion", "fecha")
