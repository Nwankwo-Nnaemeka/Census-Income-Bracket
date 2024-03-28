
import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist

# Initialize FastAPI
app = FastAPI(title="Predicting income class")

class Income(BaseModel):
    age: float
    workclass: float
    fnlwgt: float
    education: float
    education_num: float
    marital_status: float
    occupation: float
    relationship: float
    race: float
    sex: float
    capital_gain: float
    capital_loss: float
    hours_per_week: float
    native_country: float

    
@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:8000/docs."


@app.on_event('startup')
def load_clf():
    # Load classifier from pickle file
    with open("income.pkl", "rb") as file:
        global clf
        clf = pickle.load(file)

@app.post("/predict")
def predict(income:Income):
    data_point = np.array(
        [
            [
                income.age,
                income.workclass,
                income.fnlwgt,
                income.education,
                income.education_num,
                income.marital_status,
                income.occupation,
                income.relationship,
                income.race,
                income.sex,
                income.capital_gain,
                income.capital_loss,
                income.hours_per_week,
                income.native_country
            ]
        ]
    )

    pred = clf.predict(data_point).tolist()
    pred = pred[0]
    print(pred)
    return {"Prediction": pred}

