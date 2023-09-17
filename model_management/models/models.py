from pydantic import BaseModel
from typing import List

from commons.models import Tenant


class PipelineRequest(BaseModel):
    name: str
    version: int
    tenant: Tenant
    is_active: bool = True
    url: str


class Pipeline(PipelineRequest):
    id: int


class TenantPipelinesRequest(BaseModel):
    tenant: Tenant
    pipelines: List[int]


class TenantPipelines(TenantPipelinesRequest):
    id: int
    pipelines: List[Pipeline]
