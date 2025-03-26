import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)


@app.route('/home')
def home():
    debug_mode = os.getenv('FLASK_DEBUG', 'False')
    return f"Hello from Flask behind Nginx! Debug Mode: {debug_mode}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
