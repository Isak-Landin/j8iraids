from flask import Blueprint

blueprint = Blueprint(
    'boosts_blueprint',
    __name__,
    url_prefix='/boosts'
)