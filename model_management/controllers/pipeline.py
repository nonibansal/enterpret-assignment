import logging

from fastapi import APIRouter, Response

from model_management.config.config import get_settings
from model_management.logic.pipeline import PipelineService
from model_management.models.models import (
    PipelineRequest,
    Pipeline,
)


class PipelineController:
    router = APIRouter(prefix="/v1/pipeline")

    def __init__(self, pipeline_service):
        self.logger = logging.getLogger(__name__)
        self.router = APIRouter(prefix="/v1/pipeline")
        self.settings = get_settings()
        self.pipeline_service: PipelineService = pipeline_service
        self.router.add_api_route(
            path="/",
            endpoint=self.add,
            name="Add Pipeline",
            methods=["POST"],
            response_model=Pipeline
        )
        self.router.add_api_route(
            path="/{pipeline_id}",
            endpoint=self.get,
            name="Get Pipeline",
            methods=["GET"],
            response_model=Pipeline
        )
        self.router.add_api_route(
            path="/{pipeline_id}/inactive",
            endpoint=self.mark_inactive,
            name="Mark Inactive",
            methods=["PUT"]
        )
        self.router.add_api_route(
            path="/{pipeline_id}/active",
            endpoint=self.mark_active,
            name="Mark Inactive",
            methods=["PUT"]
        )

    async def add(self, pipeline_request: PipelineRequest):
        try:
            return self.pipeline_service.add(pipeline_request)
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")

    async def get(self, pipeline_id: int):
        try:
            return self.pipeline_service.get(pipeline_id)
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")

    async def mark_inactive(self, pipeline_id: int):
        try:
            self.pipeline_service.mark_inactive(pipeline_id)
            return Response(status_code=200, content="Marked Inactive")
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")

    async def mark_active(self, pipeline_id: int):
        try:
            self.pipeline_service.mark_active(pipeline_id)
            return Response(status_code=200, content="Marked Active")
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")
