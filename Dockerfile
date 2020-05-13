FROM python:3

RUN pip install mysql-connector-python fastapi uvicorn

WORKDIR /app
COPY main.py .

EXPOSE 8000 

CMD uvicorn main:app --host 0.0.0.0