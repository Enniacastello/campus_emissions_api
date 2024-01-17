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
