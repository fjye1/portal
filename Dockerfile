FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY . .

RUN git submodule update --init --recursive

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]