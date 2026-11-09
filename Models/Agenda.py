from Models.BaseModel import BaseModel


class Agenda(BaseModel):
    table = "agendas"
    columns = (
        "id",
        "uuid",
        "fecha",
        "hora",
        "usuarios_id",
        "servicios_id",
        "pagos_id",
    )
    required_fields = ("fecha", "hora", "usuarios_id", "servicios_id")
