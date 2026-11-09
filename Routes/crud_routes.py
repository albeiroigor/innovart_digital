from flask import Blueprint


def crud_blueprint(name, controller):
    blueprint = Blueprint(name, __name__)
    blueprint.add_url_rule(
        "/",
        "list",
        controller.list,
        methods=["GET"],
        strict_slashes=False,
    )
    blueprint.add_url_rule("/<int:id>", "get", controller.get, methods=["GET"])
    blueprint.add_url_rule(
        "/",
        "create",
        controller.create,
        methods=["POST"],
        strict_slashes=False,
    )
    blueprint.add_url_rule("/<int:id>", "update", controller.update, methods=["PUT"])
    blueprint.add_url_rule("/<int:id>", "delete", controller.delete, methods=["DELETE"])
    return blueprint
