import logging
from typing import List

from model_management.config.config import get_settings
from model_management.models.models import (
    PipelineRequest,
    Pipeline,
)


class PipelineService:
    def __init__(self):
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)

        self.objects: List[Pipeline] = []
        self.id = 0

    def add(self, pipeline_request: PipelineRequest) -> Pipeline:
        """
        Adding a pipeline.
        :param pipeline_request:
        :return:
        """
        logging.info(f"Adding pipeline: {pipeline_request}")

        pipeline = Pipeline(
            id=self.id,
            **pipeline_request.model_dump()
        )

        self.id += 1
        self.objects.append(pipeline)

        logging.info(f"Added pipeline: {pipeline}")
        return pipeline

    def get(self, pipeline_index: int) -> Pipeline:
        """
        Getting a pipeline from db against an id.
        :param pipeline_index:
        :return:
        """
        logging.info(f"Getting pipeline: {pipeline_index}")
        output = self.objects[pipeline_index]
        logging.info(f"Got pipeline: {output}")
        return output

    def mark_inactive(self, index: int):
        """
        Marking a pipeline inactive.
        :param index:
        :return:
        """
        logging.info(f"Marking pipeline number : {index} as inactive")
        self.objects[index].is_active = False
        logging.info(f"Marked pipeline number : {index} as inactive")

    def mark_active(self, index: int):
        """
        Marking a pipeline active.
        :param index:
        :return:
        """
        logging.info(f"Marking pipeline number : {index} as active")
        self.objects[index].is_active = True
        logging.info(f"Marked pipeline number : {index} as active")
