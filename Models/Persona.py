from Models.BaseModel import BaseModel


class Persona(BaseModel):
    table = "personas"
    columns = (
        "id",
        "uuid",
        "cedula",
        "documento",
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "correo",
        "direccion",
        "telefono",
        "fecha_nacimiento",
    )
    required_fields = (
        "cedula",
        "documento",
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "correo",
        "direccion",
        "telefono",
        "fecha_nacimiento",
    )
