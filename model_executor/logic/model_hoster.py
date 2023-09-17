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

    def get_prediction(self, pipeline_id: int, url: str, record: Record) -> ModelResponse:
        """
        Get model output

        :param pipeline_id:
        :param url:
        :param record:
        :return:
        """
        self.logger.info(f"Getting prediction against pipeline id: {pipeline_id} wit url: {url}")
        model_request = ModelRequest(
            input=record
        )

        response = requests.request(
            method="POST",
            url=url,
            json=model_request.model_dump()
        )

        value = ModelResponse(**response.json())
        return value
