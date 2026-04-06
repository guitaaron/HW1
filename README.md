# Age Prediction API (MLOps Pipeline Base)

This project is a simple backend server using FastAPI designed as the starting point for an MLOps pipeline. It leverages `DeepFace` for lightweight, out-of-the-box face recognition and age prediction.

## Project Structure

```text
HW2/
│
├── main.py                    # Entry point for the application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── app/                       # Main application codebase
    ├── __init__.py            
    ├── core/                  # Core settings and configuration
    │   └── config.py          
    ├── schemas/               # Pydantic schemas/models for request/response validation
    │   └── prediction.py      
    ├── services/              # Business logic and ML inferences
    │   └── age_predictor.py   
    └── api/                   # API routes and controllers
        └── routes.py          
```

## Setup Instructions

1. **Create and activate a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/MacOS:
   source venv/bin/activate
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Upon the first prediction, DeepFace will automatically download the necessary pre-trained weights for the age prediction model).*

3. **Run the API server:**
   ```bash
   python main.py
   # Or explicitly with uvicorn: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Testing the Pipeline:**
   - FastAPI automatically generates interactive documentation. Once the server is running, visit:
     - **Swagger UI:** http://localhost:8000/docs
     - **ReDoc:** http://localhost:8000/redoc
   - You can easily test the **`/predict/age`** endpoint directly from the Swagger UI interface by uploading an image.
