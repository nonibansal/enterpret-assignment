import logging
from typing import Annotated

from fastapi import APIRouter, Response, Header

from commons.models import Tenant
from model_executor.config.config import get_settings
from model_executor.logic.insights import InsightsService
from model_executor.models.models import GetInsightsRequest, GetInsightsResponse


class InsightsController:
    router = APIRouter(prefix="/v1/insights")

    def __init__(self, insights_service: InsightsService):
        self.logger = logging.getLogger(__name__)
        self.settings = get_settings()
        self.router = APIRouter(prefix="/v1/insights")
        self.insights_service: InsightsService = insights_service
        self.router.add_api_route(
            path="/",
            endpoint=self.get_insights,
            name="Get Insights",
            methods=["POST"],
            response_model=GetInsightsResponse
        )

    async def get_insights(
            self, get_insights_request: GetInsightsRequest,
            tenant: Annotated[Tenant, Header()] = "default",
    ):
        try:
            return self.insights_service.get_insights(
                tenant=tenant,
                get_insights_request=get_insights_request
            )
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")
