from src.static.message import FIELD_NOT_BLANK
from flask_restx import fields, Namespace

# Namespaces
auth_ns = Namespace(
    "auth", description="Route for authentication: login, logout and confirm login"
)

# payloads
login_fields = auth_ns.model(
    "AuthLoginFields",
    {
        "login": fields.String(required=True, help=FIELD_NOT_BLANK), 
        "password": fields.String(required=True, help=FIELD_NOT_BLANK)
    },
    strict=True,
)

# Headers
token_header = auth_ns.parser()
token_header.add_argument("Authorization", location="headers")
