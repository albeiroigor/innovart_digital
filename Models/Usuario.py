from Models.BaseModel import BaseModel


class Usuario(BaseModel):
    table = "usuarios"
    columns = ("id", "uuid", "correo", "contrasena", "personas_id")
    required_fields = ("correo", "contrasena", "personas_id")
    hidden_fields = ("contrasena",)
