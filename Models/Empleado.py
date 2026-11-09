from Models.BaseModel import BaseModel


class Empleado(BaseModel):
    table = "empleados"
    columns = (
        "id",
        "uuid",
        "roles_id",
        "res_id",
        "personas_id",
        "servicios_id",
    )
    required_fields = ("roles_id", "res_id", "personas_id", "servicios_id")
