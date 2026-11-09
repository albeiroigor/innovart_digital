import os

from flask import Blueprint, render_template_string, send_from_directory

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

documentacion_bp = Blueprint("documentacion", __name__)


@documentacion_bp.route("/swagger.json")
def swagger_json():
    return send_from_directory(BASE_DIR, "swagger.json")


@documentacion_bp.route("/")
def swagger_ui():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
      <title>Innovart Digital API</title>
      <link href="/static/swagger-ui/swagger-ui.css" rel="stylesheet" />
    </head>
    <body>
      <div id="swagger-ui"></div>
      <script src="/static/swagger-ui/swagger-ui-bundle.js"></script>
      <script>
        SwaggerUIBundle({
          url: "./swagger.json",
          dom_id: "#swagger-ui",
        });
      </script>
    </body>
    </html>
    """)
