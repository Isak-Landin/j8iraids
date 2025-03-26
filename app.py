import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)


@app.route('/home')
def home():
    debug_mode = False
    return f"Hello from Flask behind Nginx! Debug Mode: {debug_mode}"
