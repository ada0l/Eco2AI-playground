from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import joinedload

from eco2ai_playground.api.schemas import ProjectDB
from eco2ai_playground.core.dependencies import Pagination, get_pagination
from eco2ai_playground.db.models import Project
from eco2ai_playground.db.session import get_session

project_router = APIRouter()


@project_router.get("/", response_model=list[ProjectDB])
async def get_projects(
    pag: Pagination = Depends(get_pagination),
    db: AsyncSession = Depends(get_session),
):
    query = await db.execute(
        select(Project)
        .limit(pag.limit)
        .offset(pag.offset)
        .options(joinedload(Project.consumptions))
        .order_by(Project.start_time.desc())
    )

    return query.scalars().unique().all()


@project_router.get("/<id>", response_model=ProjectDB)
async def get_project(
    id: str,
    db: AsyncSession = Depends(get_session),
):
    query = await db.execute(
        select(Project)
        .filter(Project.project_id == id)
        .options(joinedload(Project.consumptions))
    )
    return query.scalars().first()
