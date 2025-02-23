FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

CMD ["fastapi", "run", "app/main.py", "--port", "80"]