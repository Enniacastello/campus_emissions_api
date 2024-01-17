import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def root():
    return{
    'greeting': 'H'
}

@app.get("/campuses_info")
def campuses_info():
    df = pd.read_csv("data/campuses_info.csv")

    campuses_info= df.groupby(['campus_id', "building_id"]).agg(
    {
     #'building_id': 'nunique',
     'gross_floor_area': 'mean',
     'co2_from_electric': 'sum',
     }
).reset_index()\
    .groupby(['campus_id']).agg(
    {
     'building_id': 'nunique',
     'gross_floor_area': 'sum',
     'co2_from_electric': 'sum',
     }
    ).round(1)
    output = campuses_info.rename(columns={"building_id": "n_build", "gross_floor_area" : "total_sq_ft", "co2_from_electric" :"years_of_emissions" }).to_dict(orient='index')
    return output

@app.get("/campuses_year_info")
def campuses_year_info():
    df = pd.read_csv("data/campus_overview.csv")
    return df.rename(columns={"building_id": "n_build"}).to_dict(orient='index')


@app.get("/shap")
def shap():
    df = pd.read_csv("data/shap_means_combined.csv")
    return df.rename(columns={"building_id": "n_build"}).to_dict(orient='index')












# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
"""
@app.get("/predict")
def predict(
        pickup_datetime: str,  # 2013-07-06 17:18:00
        pickup_longitude: float,    # -73.950655
        pickup_latitude: float,     # 40.783282
        dropoff_longitude: float,   # -73.984365
        dropoff_latitude: float,    # 40.769802
        passenger_count: int
    ):      # 1

    #Make a single course prediction.
    #Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    #Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)

    return{
    'fare_amount': 5.93
}
"""
