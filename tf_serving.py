from io import BytesIO
import numpy as np
import requests
import uvicorn
from PIL import Image
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

endpoint = "http://localhost:8501/v1/models/kavin:predict"
CLASS_NAMES = ['Leaf Blight', 'Brown Spot', 'Leaf Smut']

@app.get("/ping")
async def ping():
    return "hi , i am kavin"

def read_file_as_image(data) -> np.ndarray:
    img = Image.open(BytesIO(data)).convert('RGB')
    img = img.resize((224, 224))
    image = np.array(img)
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    json_data = {
        "instances": img_batch.tolist()
    }
    response = requests.post(endpoint, json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)
    return {
        'class': predicted_class,
        'confidence': confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8500)
