from fastapi import FastAPI
from interface import StudentInput
from model import predict_depression

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Depression Prediction API Running!"}

@app.post("/predict")
def predict(data: StudentInput):
    data_dict = data.dict()
    result = predict_depression(data_dict)
    return {
        "Prediction": int(result),
        "Meaning": "Depressed" if result == 1 else "Not Depressed"
    }
