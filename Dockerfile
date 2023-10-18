FROM python:3.9-slim-buster
WORKDIR /app
ENV PORT 8080
ENV HOST 0.0.0.0
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]