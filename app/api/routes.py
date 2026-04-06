from fastapi import APIRouter, File, UploadFile, HTTPException
from app.schemas.prediction import PredictionResponse
from app.services.age_predictor import AgePredictorService

router = APIRouter()

@router.get("/")
def health_check():
    """
    Health check endpoint to ensure the API is running.
    """
    return {"status": "ok", "message": "Age Prediction API is up and running."}

@router.post("/predict/age", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    """
    Endpoint to upload an image and receive age predictions for the faces found.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")
    
    try:
        contents = await file.read()
        ages = AgePredictorService.predict_age(contents)
        
        return PredictionResponse(
            filename=file.filename,
            predicted_ages=ages,
            faces_detected=len(ages)
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")
