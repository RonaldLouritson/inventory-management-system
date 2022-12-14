FROM python:3.7-slim-buster

WORKDIR /inventory-management-system

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]