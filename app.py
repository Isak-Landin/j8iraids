import os
from flask import Flask
from dotenv import load_dotenv
from home import blueprint as home_bp

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='static/templates', static_folder='static')
app.register_blueprint(home_bp)
