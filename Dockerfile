FROM python:3.8-alpine
WORKDIR /app
COPY rest_app.py db_connector.py /app
RUN pip install flask pymysql datetime
EXPOSE 5000
VOLUME /app/logs
CMD python3 rest_app.py
