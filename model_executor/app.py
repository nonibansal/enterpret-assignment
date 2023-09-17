import logging

from fastapi import FastAPI

from model_executor.controllers.health_check import HealthCheckController
from model_executor.controllers.insights import InsightsController

from model_executor.singleton.singleton import (
    insights_service
)

app = FastAPI()
logger = logging.getLogger(__name__)

app.include_router(HealthCheckController().router)
app.include_router(InsightsController(insights_service).router)
