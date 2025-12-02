import pickle
import numpy as np
import pandas as pd

# Load model
with open("log_reg.pkl", "rb") as f:
    model = pickle.load(f)

# Categorical encoders (create mapping same as used in training)
sleep_map = {
    "Less than 5 hours": 0,
    "5-6 hours": 1,
    "7-8 hours": 2,
    "More than 8 hours": 3,
    "Others": 4
}

diet_map = {
    "Healthy": 0,
    "Moderate": 1,
    "Unhealthy": 2
}

degree_map = {
    "Bachelors": 0,
    "Masters": 1,
    "PhD": 2,
    "Diploma": 3
}

def preprocess(data_dict):
    df = pd.DataFrame([data_dict])

    # Apply encoding
    df['Sleep_Duration'] = df['Sleep_Duration'].map(sleep_map)
    df['Dietary_Habits'] = df['Dietary_Habits'].map(diet_map)
    df['Degree'] = df['Degree'].map(degree_map)

    return df.values  # return numpy array for prediction

def predict_depression(data_dict):
    processed = preprocess(data_dict)
    prediction = model.predict(processed)
    return int(prediction[0])
