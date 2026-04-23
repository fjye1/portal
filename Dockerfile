FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git

# Clone the main repo + all submodules in one shot
RUN git clone --recurse-submodules https://github.com/fjye1/Portal .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]