import logging
import os.path
from typing import List

from model_hoster.config.config import get_settings
from model_hoster.models.models import ModelResponse
from model_hoster.utils.object_pool import ObjectPool


class Model1:
    def __init__(self):
        self.settings = get_settings()

        # Object pool for each model to handle thread safe operations
        self.model_pool = ObjectPool(
            [self._load_model() for _ in range(2)]
        )
        self.logger = logging.getLogger(__name__)

    def _load_model(self):
        """
        Loading model
        :return:
        """
        model_path = os.path.join(
            self.settings.MODEL_PATH,
            self.settings.PIPELINE_NAME,
            self.settings.PIPELINE_VERSION,
            "model1"
        )
        return object

    def process_text(self, text: str) -> List[str]:
        """
        Preprocessing according to model and using model to predict output.
        :param text:
        :return:
        """

        logging.info("Getting model 1")
        model = self.model_pool.acquire()
        logging.info("model 1 acquired")

        logging.info(f"Processing request : {text}")
        try:
            pass
            # To model something
        except Exception as e:
            self.logger.error(f"Error : {e}")
            raise Exception(e)
        finally:
            self.model_pool.release(model)
        logging.info(f"Processed request : {text}")

        if "quality" in text:
            return ["Quality", "Audio"]
        else:
            return ["No tags"]


class TextPipeline:
    """
    This is the main pipeline for a particular insight.
    Could contain one model or multiple models
    """
    def __init__(self):
        self.settings = get_settings()

        self.model_1 = Model1()
        # self.model_2 = TextProcessor2()

    def process(self, text: str) -> ModelResponse:
        logging.info(f"Starting text processing with pipeline: {self.settings.PIPELINE_NAME}")

        output = ModelResponse(
            output=self.model_1.process_text(text)
        )

        logging.info(f"Finished pipeline: {self.settings.PIPELINE_NAME} with response: {output}")
        return output
