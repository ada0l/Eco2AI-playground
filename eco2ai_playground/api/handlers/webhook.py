import logging

from fastapi import APIRouter, Response, status
from pydantic import ValidationError

from eco2ai_playground.api.schemas import (
    ConsumptionInPydantic,
    ConsumptionListStrInPydantic,
)

webhook_router = APIRouter()


@webhook_router.post("/")
async def webhook(consumption_list_str_in: ConsumptionListStrInPydantic):
    raw_dict = consumption_list_str_in.convert_to_dict()
    try:
        consumption_in = ConsumptionInPydantic(**raw_dict)
    except ValidationError as ex:
        return Response(
            content=ex.json(), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    logger = logging.getLogger("uvicorn.info")
    logger.info(consumption_in)
    return {}
