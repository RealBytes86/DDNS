FROM python:3.11

WORKDIR /DDNS_UPDATE
COPY ./ /DDNS_UPDATE/

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
