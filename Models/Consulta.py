from Models.BaseModel import BaseModel


class Consulta(BaseModel):
    table = "consultas"
    columns = ("id", "uuid", "hora", "fecha", "mensaje", "usuarios_id")
    required_fields = ("hora", "fecha", "mensaje", "usuarios_id")
