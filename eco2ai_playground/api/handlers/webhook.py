from fastapi import APIRouter, Depends, Response, status
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from eco2ai_playground.api.schemas import (
    ConsumptionIn,
    ConsumptionListStrIn,
)
from eco2ai_playground.db.models import Consumption, Project
from eco2ai_playground.db.session import get_session

webhook_router = APIRouter()


@webhook_router.post("/", response_model=dict)
async def webhook(
    consumption_list_str_in: ConsumptionListStrIn,
    db: AsyncSession = Depends(get_session),
):
    raw_dict = consumption_list_str_in.convert_to_dict()
    try:
        consumption_in = ConsumptionIn(**raw_dict)
    except ValidationError as ex:
        return Response(
            content=ex.json(), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    project = (
        (
            await db.execute(
                select(Project).filter(
                    Project.project_id == str(consumption_in.id)
                )
            )
        )
        .scalars()
        .first()
    )
    if project is None:
        project = Project(
            project_id=str(consumption_in.id),
            name=consumption_in.project_name,
            description=consumption_in.experiment_description,
            start_time=consumption_in.start_time,
            cpu=consumption_in.cpu_name,
            gpu=consumption_in.gpu_name,
            os=consumption_in.os,
            region=consumption_in.region,
        )
        db.add(project)
    consumption = Consumption(
        project=project,
        epoch_str=consumption_in.epoch,
        duration=consumption_in.durations,
        power=consumption_in.power_consumption,
        co2=consumption_in.co2_emissions,
    )
    db.add(consumption)
    await db.commit()
    return {}
