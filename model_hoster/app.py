import logging

from fastapi import FastAPI

from model_hoster.controllers.health_check import HealthCheckController
from model_hoster.controllers.prediction import PredictionController
from model_hoster.logic.process import TextPipeline
from model_hoster.utils.object_pool import ObjectPool

app = FastAPI()
logger = logging.getLogger(__name__)

app.include_router(HealthCheckController().router)
app.include_router(PredictionController().router)
