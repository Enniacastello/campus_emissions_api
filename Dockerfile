FROM python:3.10.6-buster
COPY . campus_emissions_api
WORKDIR campus_emissions_api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api:app --host 0.0.0.0 --port $PORT
