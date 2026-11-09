from werkzeug.security import check_password_hash, generate_password_hash

from Models.Usuario import Usuario
from Services.BaseService import ConflictError, CrudService


class UsuarioService(CrudService):
    model = Usuario

    def prepare_create(self, values):
        if self.buscar_por_correo(values["correo"]):
            raise ConflictError("El correo ya está registrado")
        values["contrasena"] = generate_password_hash(values["contrasena"])
        return values

    def prepare_update(self, values):
        contrasena = values.get("contrasena")
        if contrasena:
            values["contrasena"] = generate_password_hash(contrasena)
        else:
            values.pop("contrasena", None)
        return values

    def update(self, id, data):
        correo = data.get("correo")
        if correo:
            existente = self.buscar_por_correo(correo)
            if existente is not None and existente.id != id:
                raise ConflictError("El correo ya está registrado")
        return super().update(id, data)

    def buscar_por_correo(self, correo):
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"SELECT {self.model.select_columns()} FROM {self.model.table} "
                "WHERE correo = %s",
                (correo,),
            )
            row = cursor.fetchone()
        return self.model.from_row(row) if row else None

    def validar_login(self, correo, contrasena):
        usuario = self.buscar_por_correo(correo)
        if usuario is None:
            return None
        if not check_password_hash(usuario.contrasena, contrasena):
            return None
        return usuario
