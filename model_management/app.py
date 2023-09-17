import logging

from fastapi import FastAPI

from model_management.controllers.tenant_pipelines import TenantPipelinesController
from model_management.controllers.health_check import HealthCheckController
from model_management.singleton.singleton import (
    tenant_pipelines_service,
    pipeline_service
)
from model_management.controllers.pipeline import PipelineController

app = FastAPI()
logger = logging.getLogger(__name__)

app.include_router(TenantPipelinesController(tenant_pipelines_service).router)
app.include_router(PipelineController(pipeline_service).router)
app.include_router(HealthCheckController().router)
