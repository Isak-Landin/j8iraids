import os
from flask import Flask
from dotenv import load_dotenv
from home.home import home_bp

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.register_blueprint(home_bp)