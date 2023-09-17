import logging
from fastapi import APIRouter, Response

from model_hoster.config.config import get_settings
from model_hoster.logic.process import TextPipeline
from model_hoster.utils.object_pool import ObjectPool
from model_hoster.models.models import ModelResponse, ModelRequest


class PredictionController:
    router = APIRouter(prefix="/v1")

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.router = APIRouter(prefix="/v1")
        self.settings = get_settings()
        self.predictors = ObjectPool(
            [TextPipeline() for _ in range(1)]
        )
        self.router.add_api_route(
            path=f"/{self.settings.PIPELINE_ID}",
            endpoint=self.get_prediction,
            name="Get Prediction",
            methods=["POST"],
            response_model=ModelResponse
        )

    async def get_prediction(self, request: ModelRequest):
        pipeline: TextPipeline = self.predictors.acquire()
        try:
            return pipeline.process(request.input.text)
        except Exception as e:
            return Response(status_code=500, content=f"{e}")
        finally:
            self.predictors.release(pipeline)
