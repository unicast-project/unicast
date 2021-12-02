FROM python:3.8

WORKDIR /unicast

COPY requirements.txt .
COPY src /unicast/src

RUN pip install -r requirements.txt


ENV PYTHONPATH "${PYTHONPATH}:/unicast"
EXPOSE 8000
CMD ["python", "src/models/main.py"]
