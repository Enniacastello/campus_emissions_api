import pandas as pd
import pickle
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

# CAMPUSES INITIAL METRICS
@app.get("/campuses_info")
def campuses_info():
    df = pd.read_csv("data/campuses_info.csv").round(1).set_index('campus_id')
    output = df.rename(columns={"building_id": "n_build", "gross_floor_area" : "total_sq_ft", "co2_from_electric" :"total_missions" }).to_dict(orient='index')
    return output

@app.get("/campuses_year_info")
def campuses_year_info():
    df = pd.read_csv("data/campus_overview.csv").round(1)
    return df.rename(columns={"building_id": "n_build"}).to_dict(orient='index')

# SHAP MODEL
@app.get("/shap")
def shap():
    df = pd.read_csv("data/shap_means_combined.csv")
    return df.rename(columns={"building_id": "n_build"}).to_dict(orient='index')


# CONSUMPTION PREDICTIONS
@app.get("/predictions")
def predictions(campus_id=1, end_date_prediction = "2022-03-04"):
    with open(f'models/sarimax_model_campus{campus_id}.pkl', 'rb') as file:
        model = pickle.load(file)
    with open(f'models/seasonal_one_year_campus{campus_id}.pkl', 'rb') as file:
        seasonal_one_year = pickle.load(file)
    prediction_start = pd.to_datetime("2021-12-27", format="%Y-%m-%d")#Fixed
    prediction_end = pd.to_datetime(end_date_prediction, format="%Y-%m-%d")


    # Predictions
    preds = model.get_prediction(start=prediction_start, end=prediction_end, dynamic=False)
    preds_df = preds.conf_int()
    preds_df.columns = ['lower', 'upper']
    preds_df['preds'] = preds.predicted_mean

    preds_df["day"] = preds_df.index.weekday
    preds_df = pd.merge(preds_df,seasonal_one_year, on = "day", how = "left")
    preds_df["full_preds"] = preds_df["preds"] * preds_df["seasonal_component"]
    preds_df["lower_conf"] = preds_df["lower"] * preds_df["seasonal_component"]
    preds_df["upper_conf"] = preds_df["upper"] * preds_df["seasonal_component"]
    date_range = pd.date_range(start=prediction_start, end=prediction_end, freq='D')

    # Set the date range as the index of preds_df
    preds_df.index = date_range
    preds_df.index.name = 'timestamp'

    preds_df = preds_df.drop(columns=['lower',
        'upper',
        'preds',
        'day',
        'seasonal_component'])

    predictions_dict = preds_df.to_dict('index')
    predictions_dict = {str(key): value for key, value in predictions_dict.items()}
    predictions_json = {}
    predictions_json['building_id'] = "all"
    predictions_json['campus_id'] = campus_id
    predictions_json['predictions'] = predictions_dict
    return predictions_json
    #df = pd.read_csv("data/shap_means_combined.csv")
    #return df.rename(columns={"building_id": "n_build"}).to_dict(orient='index')












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
