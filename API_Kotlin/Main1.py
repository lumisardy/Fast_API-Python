from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
import cv2
import numpy as np
from io import BytesIO
from PIL import Image as PILImage

app = FastAPI()
model = YOLO("yolo11n.pt")

@app.post("/transformImage")
async def transform_image(file: UploadFile = File(...)):
    contents = await file.read()

    # Decodificar imagen
    np_arr = np.frombuffer(contents, np.uint8)
    img_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Procesar con YOLO
    results = model.predict(img_np)
    processed = results[0].plot()  # np.ndarray

    # Convertir a imagen JPEG
    img_pil = PILImage.fromarray(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
    buffer = BytesIO()
    img_pil.save(buffer, format="JPEG")
    buffer.seek(0)

    # Devolver imagen como archivo
    return StreamingResponse(buffer, media_type="image/jpeg")
