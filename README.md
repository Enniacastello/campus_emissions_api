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

## How to deploy in Docker


You need to create the file ```.env```:
```
GAR_IMAGE=APIs_NAME
PORT=  #The number or the port you're working
GCP_PROJECT= # Your personal GCP project for this bootcamp

GCP_REGION= REGION_PROJECT

# Cloud Storage
GAR_MEMORY=2Gi
```


This code helps you to deploy your API in Docker
```
docker build --tag=$GAR_IMAGE:dev .
```

This is the code to run the API in your terminal
```
docker run -it -e PORT=$PORT -p $PORT:$PORT $GAR_IMAGE:dev
```
## Deploy your API to GoogleCloud

First, let’s make sure to enable the Google Artifact Registry API for your project in GCP.

Once this is done, let’s allow the docker command to push an image to GCP within our region.
```
gcloud auth configure-docker $GCP_REGION-docker.pkg.dev
```

Lets create a repo in that region as well!
```
gcloud artifacts repositories create emissions --repository-format=docker \ --location=$GCP_REGION --description="Repository for storing emissions images"
```

Lets build our image ready to push to that repo
```
docker build -t  $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/emissions/$GAR_IMAGE:prod .
```

Again, let’s make sure that our image runs correctly, so as to avoid wasting time pushing a broken image to the cloud.
```
docker run -e PORT=$PORT -p $PORT:$PORT --env-file .env.yaml $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/emissions/$GAR_IMAGE:prod
```
Your file ```.env.yaml``` should look like this:
```
GAR_IMAGE: PROJECT_NAME
GCP_PROJECT: ID_PROJECT
GCP_REGION: REGION_PROJECT
GAR_MEMORY: "2Gi"
```
Visit ```http://localhost:$PORT/ ``` and check whether the API is running as expected.

We can now push our image to Google Artifact Registry.
```
docker push $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/emissions/$GAR_IMAGE:prod
```
The image should be visible in the GCP console.
