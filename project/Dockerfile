FROM python:3.11-slim

WORKDIR /usr/share/caddy/project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Caddyfile /etc/caddy/Caddyfile
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]