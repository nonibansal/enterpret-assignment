import logging
from fastapi import APIRouter, Response

from commons.models import Tenant
from model_management.config.config import get_settings
from model_management.logic.tenant_pipelines import TenantPipelinesService
from model_management.models.models import (
    TenantPipelinesRequest,
    TenantPipelines,
)


class TenantPipelinesController:
    router = APIRouter(prefix="/v1/tenant-pipelines")

    def __init__(self, tenant_pipelines_service):
        self.logger = logging.getLogger(__name__)
        self.router = APIRouter(prefix="/v1/tenant-pipelines")
        self.settings = get_settings()
        self.tenant_pipelines_service: TenantPipelinesService = tenant_pipelines_service
        self.router.add_api_route(
            path="/",
            endpoint=self.add,
            name="Add Tenant Pipelines",
            methods=["POST"],
            response_model=TenantPipelines
        )
        self.router.add_api_route(
            path="/{tenant_pipelines_id}",
            endpoint=self.get,
            name="Get Tenant Pipelines",
            methods=["GET"],
            response_model=TenantPipelines
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.put,
            name="Update Tenant Pipelines",
            methods=["PUT"],
            response_model=TenantPipelines
        )
        self.router.add_api_route(
            path="/",
            endpoint=self.search,
            name="Search Tenant Pipelines by Tenant",
            methods=["GET"],
            response_model=TenantPipelines
        )

    async def add(self, tenant_pipelines_request: TenantPipelinesRequest):
        try:
            return self.tenant_pipelines_service.add(tenant_pipelines_request)
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")

    async def get(self, tenant_pipelines_id: int):
        try:
            return self.tenant_pipelines_service.get(tenant_pipelines_id)
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")

    async def put(self, tenant_pipelines_request: TenantPipelinesRequest):
        try:
            return self.tenant_pipelines_service.put(tenant_pipelines_request)
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")

    async def search(self, tenant: Tenant):
        try:
            return self.tenant_pipelines_service.search(tenant.value)
        except Exception as e:
            self.logger.error(f"{e}")
            Response(status_code=500, content=f"{e}")




