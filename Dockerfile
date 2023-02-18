FROM python:3.8-alpine
WORKDIR /app
COPY rest_app.py /app
RUN pip install flask
EXPOSE 5000
VOLUME /app/logs
CMD python3 rest_app.py
