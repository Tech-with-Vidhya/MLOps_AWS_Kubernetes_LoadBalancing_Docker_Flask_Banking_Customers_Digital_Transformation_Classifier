FROM python:3.8
COPY FlaskApplication/requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /bank_classification
COPY FlaskApplication .
WORKDIR /bank_classification/src
RUN mkdir -p logs
RUN ["chmod", "+x", "gunicorn.sh"]
EXPOSE 5000
ENTRYPOINT ["./gunicorn.sh"]