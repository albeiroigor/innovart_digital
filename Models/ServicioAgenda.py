from Models.BaseModel import BaseModel


class ServicioAgenda(BaseModel):
    table = "servicios_agenda"
    columns = ("id", "uuid", "servicios_id", "agendas_id")
    required_fields = ("servicios_id", "agendas_id")
