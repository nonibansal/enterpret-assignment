from pydantic import BaseModel
from typing import List

from commons.models import Record


class PipelineResponse(BaseModel):
    name: str
    insights: List[str]


class GetInsightsRequest(BaseModel):
    record: Record


class GetInsightsResponse(BaseModel):
    record: Record
    pipeline_response_list = List[PipelineResponse]
