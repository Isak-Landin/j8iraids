from flask import Blueprint
from home import home


blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)
