from Models.BaseModel import BaseModel


class Rol(BaseModel):
    table = "roles"
    columns = ("id", "uuid", "tipo")
    required_fields = ("tipo",)
