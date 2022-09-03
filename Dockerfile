FROM python:3.10-alpine
WORKDIR /sybib

COPY requirements.txt .
RUN apk add --no-cache gcc libressl-dev musl-dev libffi-dev build-base git curl mariadb-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "entrypoint.sh"]