import logging
import requests

from commons.models import Record
from model_executor.config.config import get_settings

from model_hoster.models.models import (
    ModelRequest,
    ModelResponse,
)


class ModelHosterService:
    def __init__(self):
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)

    def get_prediction(self, pipeline_id: int, record: Record) -> ModelResponse:
        """
        Get model output

        :param pipeline_id:
        :param record:
        :return:
        """
        model_request = ModelRequest(
            input=record
        )

        response = requests.request(
            method="POST",
            url=f"http://{self.settings.MODEL_HOSTER_URL}/v1/{pipeline_id}",
            json=model_request.model_dump()
        )

        value = ModelResponse(**response.json())
        return value
