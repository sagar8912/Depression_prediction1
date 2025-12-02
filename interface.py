from pydantic import BaseModel

class StudentInput(BaseModel):
    Gender: int
    Age: float
    Academic_Pressure: float
    Work_Pressure: float
    CGPA: float
    Study_Satisfaction: float
    Job_Satisfaction: float
    Sleep_Duration: str
    Dietary_Habits: str
    Degree: str
    Suicidal_Thoughts: int
    Work_Study_Hours: float
    Financial_Stress: float
    Family_History: int
