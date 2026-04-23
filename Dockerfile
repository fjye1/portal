FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

# Copy your local project (this fixes your run.py issue)
COPY . .

# If you still use submodules, initialise them
RUN git submodule update --init --recursive

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]