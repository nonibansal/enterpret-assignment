from pydantic import BaseModel
from enum import Enum


class Record(BaseModel):
    id: str
    text: str = ""


class Tenant(str, Enum):
    phonepay = "phonepay"
    curefit = "curefit"
    common = "common"
    epifi = "epifi"
