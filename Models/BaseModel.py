from datetime import date, datetime, time, timedelta
from decimal import Decimal


def _serialize(value):
    if isinstance(value, timedelta):
        seconds = int(value.total_seconds())
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    if isinstance(value, (datetime, date, time)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return float(value)
    return value


class BaseModel:
    table = ""
    primary_key = "id"
    columns = ()
    required_fields = ()
    hidden_fields = ()

    def __init__(self, **values):
        for name in self.columns:
            setattr(self, name, values.get(name))

    @classmethod
    def select_columns(cls):
        return ", ".join(cls.columns)

    @classmethod
    def writable_fields(cls):
        return [name for name in cls.columns if name not in ("id", "uuid")]

    @classmethod
    def create_payload(cls, data):
        return {name: data.get(name) for name in cls.writable_fields()}

    @classmethod
    def update_payload(cls, data):
        return {
            name: data[name]
            for name in cls.writable_fields()
            if name in data
        }

    @classmethod
    def from_row(cls, row):
        return cls(**dict(zip(cls.columns, row)))

    def to_dict(self):
        return {
            name: _serialize(getattr(self, name))
            for name in self.columns
            if name not in self.hidden_fields
        }
