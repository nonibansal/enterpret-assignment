import logging
from typing import List

from commons.models import Tenant
from model_executor.config.config import get_settings
from model_executor.logic.model_hoster import ModelHosterService
from model_executor.logic.tenant_pipelines import TenantPipelinesService
from model_executor.models.models import GetInsightsRequest, GetInsightsResponse, PipelineResponse


class InsightsService:
    def __init__(
            self, tenant_pipelines_service: TenantPipelinesService,
            model_hoster_service: ModelHosterService
    ):
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)
        self.model_hoster_service: ModelHosterService = model_hoster_service
        self.tenant_pipelines_service: TenantPipelinesService = tenant_pipelines_service

    def get_insights(self, tenant: Tenant, get_insights_request: GetInsightsRequest) -> GetInsightsResponse:
        """
        This function gets insights against record.

        :param tenant:
        :param get_insights_request:
        :return:
        """
        pipeline_response_list: List[PipelineResponse] = []

        tenant_pipelines = self.tenant_pipelines_service.get_pipelines(tenant)

        for pipeline in tenant_pipelines.pipelines:

            pipeline_name = pipeline.name
            pipeline_id = pipeline.id

            prediction = self.model_hoster_service.get_prediction(
                pipeline_id=pipeline_id,
                url=pipeline.url,
                record=get_insights_request.record
            )

            pipeline_response_list.append(
                PipelineResponse(
                    name=pipeline_name,
                    insights=prediction.output
                )
            )

        output = GetInsightsResponse(
            record=get_insights_request.record,
            pipeline_response_list=pipeline_response_list
        )
        return output
