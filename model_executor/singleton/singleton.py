from model_executor.logic.tenant_pipelines import TenantPipelinesService
from model_executor.logic.model_hoster import ModelHosterService
from model_executor.logic.insights import InsightsService


model_hoster_service = ModelHosterService()
tenant_pipelines_service = TenantPipelinesService()
insights_service = InsightsService(tenant_pipelines_service, model_hoster_service)
