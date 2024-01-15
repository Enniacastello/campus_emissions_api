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
    df = pd.read_csv("data/merged_emissions_prices.csv")
    #Replacing 'campus_id' by the campus name
    mapping = {1: 'Bundoora', 2: 'Albury-Wodonga'}

    # Aplica el reemplazo utilizando el método replace
    df['campus_id'] = df['campus_id'].replace(mapping)
    campuses_info= df.groupby(['campus_id'])['building_id','consumption', 'gross_floor_area', 'emissions_per_sqft_yearly'].agg(
            {
            'building_id': 'nunique',
            'consumption' : 'sum',
            'gross_floor_area' : 'sum',
            'emissions_per_sqft_yearly' :'sum'
            }
        ).round(1)
    output = campuses_info.rename(columns={"building_id": "n_build", "gross_floor_area" : "floor_area", "emissions_per_sqft_yearly" :"emissions_sqft_yr" }).to_dict(orient='index')
    return output















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
