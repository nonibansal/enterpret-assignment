from model_management.logic.tenant_pipelines import TenantPipelinesService
from model_management.logic.pipeline import PipelineService

pipeline_service = PipelineService()
tenant_pipelines_service = TenantPipelinesService(pipeline_service)
