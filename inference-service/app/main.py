from fastapi import FastAPI
from .model import ModelService
from .metrics import Metrics
import logging

app = FastAPI(title="AI Inference Service")
model_service = ModelService()
metrics = Metrics()

@app.on_event("startup")
async def startup_event():
    logging.info("Starting up...")
    model_service.load_model()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: dict):
    metrics.increment_request_count()
    result = model_service.predict(data)
    return {"result": result}
