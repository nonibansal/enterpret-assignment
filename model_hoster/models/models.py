from pydantic import BaseModel
from typing import List

from commons.models import Record


class ModelRequest(BaseModel):
    input: Record


class ModelResponse(BaseModel):
    output: List[str]
