# Step by step of how to run an API: campus_emissions_api

Step one: You need to clone the repository url:

```
git clone git@github.com:Enniacastello/campus_emissions_api.git
```

After the clone, you need to create your new enviroment with:
```
pyenv virtualenv backend
```

Once you have the enviroment you need to install the libraries:

```
pip install -r requirements.txt
```

## How to run the app

### Endpoints
```
make run_api
``````
Emissions per square foot at campus 2 (chart)
```
campuses_year_info
```

Overview metrics for campuses
```
campuses_info
```
Api to know what a influences the consumption

```
shap
```


## To run de predictions you need to download the "Model" folder from drive

URL: https://drive.google.com/drive/folders/1TAD9ISqjb7S0tMk7DDaLQ2autvV4YxI9?usp=drive_link

## How to deploy in docker (wip)
First you need to create your Dockerfile with all the necessary elements
```
Dockerfile
```
This is an example of how it should look:
```
ROM python:3.10.6-buster
COPY . campus_emissions_api      #The folder where is located all the documents
WORKDIR campus_emissions_api     #The folder where is located all the documents
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api:app --host 0.0.0.0 --port $PORT
```

Also, you need to create two more files ```.env``` and  ```.envrc```.

Your ```.env``` should look like this:
```
GAR_IMAGE=campus_emissions_api  #The folder where is located all the documents
PORT=8002                       #The number or the port you're working
```
For the ```.envrc``` you should add this code:
```
dotenv
```

This code helps you to deploy your API in Docker
```
docker build --tag=$GAR_IMAGE:dev .
```

This is the code to run the API in your terminal
```
run -it -e PORT=$PORT -p $PORT:$PORT $GAR_IMAGE:dev
```
