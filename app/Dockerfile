FROM python:3.9

WORKDIR /app

COPY main.py .
COPY classifier.py .

RUN pip install --upgrade pip
RUN pip install flask mysql-connector-python transformers torch

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD ["flask", "run", "--reload"]
