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

```
make run_api
``````

### Endpoints


```
campuses_year_info
```
Emissions per square foot at campus 2 (chart)

```
campuses_info
```
Overview metrics for campuses

```
shap
```
Api to know what a influences the consumption

## How to deploy in docker (wip)
