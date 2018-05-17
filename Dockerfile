FROM python:2

ENV FLASK_APP app.py
ENTRYPOINT ["python","-m","flask","run","--host=0.0.0.0"]

WORKDIR /usr/src/app

COPY . .

RUN pip install flask
RUN pip install flask_httpauth


EXPOSE 5000
EXPOSE 587

# CMD ["python", "./app.py"]
