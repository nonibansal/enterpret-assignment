import logging
from typing import List

from model_management.config.config import get_settings
from model_management.logic.pipeline import PipelineService
from model_management.models.models import (
    TenantPipelinesRequest,
    TenantPipelines,
    Pipeline,
)


class TenantPipelinesService:
    def __init__(self, pipeline_service):
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)
        self.pipeline_service: PipelineService = pipeline_service
        self.objects: List[TenantPipelines] = []
        self.id = 0

    def check_eligible(self, pipeline_index_list: List[int]) -> List[Pipeline]:
        """
        This function gets eligibility of all pipelines against a tenant.
        Checks:
        1. All active
        # TO DO
        2. Check if pipeline od another tenant is not getting used.

        :param pipeline_index_list:
        :return:
        """
        pipelines: List[Pipeline] = []
        for index in pipeline_index_list:
            pipeline = self.pipeline_service.get(index)

            if not pipeline.is_active:
                raise Exception(f"Pipeline number : {index} is inactive please mark as active")

            pipelines.append(pipeline)
        return pipelines

    def add(self, tenant_pipelines_request: TenantPipelinesRequest) -> TenantPipelines:
        """
        Add all the pipelines against a tenant.
        :param tenant_pipelines_request:
        :return:
        """
        logging.info(f"Adding tenant pipelines: {tenant_pipelines_request}")

        pipelines = self.check_eligible(tenant_pipelines_request.pipelines)

        # Getting object to map
        tenant_pipelines = TenantPipelines(
            id=self.id,
            tenant=tenant_pipelines_request.tenant,
            pipelines=pipelines
        )
        self.id += 1
        self.objects.append(tenant_pipelines)

        logging.info(f"Added tenant pipelines pipeline: {tenant_pipelines}")
        return tenant_pipelines

    def get(self, tenant_pipelines_index: int) -> TenantPipelines:
        """
        Get all the pipelines against an id.
        :param tenant_pipelines_index:
        :return:
        """
        logging.info(f"Getting tenant pipelines: {tenant_pipelines_index}")
        output = self.objects[tenant_pipelines_index]
        logging.info(f"Got tenant pipelines pipeline: {output}")
        return output

    def search(self, tenant_name: str) -> TenantPipelines:
        """
        Get all the pipelines against a tenant name.
        """
        logging.info(f"Search tenant pipelines with tenant name: {tenant_name}")

        for tenant_pipeline in self.objects:
            if tenant_pipeline.tenant == tenant_name:
                return tenant_pipeline

        raise Exception(f"Not found tenant pipelines with tenant name: {tenant_name}")

    def put(self, tenant_pipelines_request: TenantPipelinesRequest) -> TenantPipelines:
        """
        Updating pipelines against a tenant.
        :param tenant_pipelines_request:
        :return:
        """
        logging.info(f"Updating tenant pipelines")
        try:
            # Searching for existing against tenant name
            tenant_pipeline = self.search(tenant_pipelines_request.tenant)

            # Getting pipeline info
            pipelines = self.check_eligible(tenant_pipelines_request.pipelines)

            # Updating
            tenant_pipeline.pipelines = pipelines

            logging.info(f"Updates tenant pipelines: {tenant_pipeline}")
            return tenant_pipeline
        except Exception as e:
            logging.info(f"Tenant not found so creating one: {e}")
            return self.add(tenant_pipelines_request)




