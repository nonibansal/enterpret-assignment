import logging
import requests

from commons.models import Tenant
from model_executor.config.config import get_settings

from model_management.models.models import (
    TenantPipelines,
)


class TenantPipelinesService:
    def __init__(self):
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)

    def get_pipelines(self, tenant: Tenant) -> TenantPipelines:
        """
        Get pipelines for a tenant

        :param tenant: Tenant
        :return:
        """
        self.logger.info(f"Getting pipelines for tenant: {tenant}")
        response = requests.request(
            method="GET",
            url=f"http://{self.settings.MODEL_MANAGEMENT_URL}/v1/tenant-pipelines/?tenant={tenant.value}"
        )

        self.logger.info(f"Got response: {response.json()}")

        value = TenantPipelines(**response.json())
        return value
