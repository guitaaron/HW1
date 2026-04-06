import cv2
import numpy as np
from deepface import DeepFace

class AgePredictorService:
    @staticmethod
    def predict_age(image_bytes: bytes) -> list:
        try:
            # Convert incoming bytes to a numpy array
            nparr = np.frombuffer(image_bytes, np.uint8)
            
            # Decode the numpy array into an OpenCV image (BGR format)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is None:
                raise ValueError("Could not decode the provided image.")

            # Analyze the image to predict age.
            results = DeepFace.analyze(
                img_path=img, 
                actions=['age'], 
                enforce_detection=True
            )
            
            if isinstance(results, list):
                ages = [res.get('age') for res in results if 'age' in res]
            else:
                ages = [results.get('age')]
                
            return ages
            
        except ValueError as ve:
            print(f"Validation Error: {ve}")
            raise ve
        except Exception as e:
            print(f"Error in ML model prediction: {e}")
            raise ValueError("No face detected or image is invalid.")
