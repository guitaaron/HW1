from pydantic import BaseModel
from typing import List

class PredictionResponse(BaseModel):
    filename: str
    predicted_ages: List[int]
    faces_detected: int
