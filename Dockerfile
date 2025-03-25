FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Ensure Flask environment is loaded
CMD ["sh", "-c", "export $(cat .env | xargs) && gunicorn --bind 0.0.0.0:5005 app:app"]
