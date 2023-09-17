import logging

from fastapi import APIRouter, Response


class HealthCheckController:
    router = APIRouter(prefix="/v1")

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.router = APIRouter(prefix="/v1")
        self.router.add_api_route(
            path="/status",
            endpoint=self.get_status,
            name="Get Status",
            methods=["GET"]
        )

    @staticmethod
    async def get_status():
        return Response("Status OK", status_code=200)
