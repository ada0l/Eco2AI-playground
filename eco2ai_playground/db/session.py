from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from eco2ai_playground.core.settings import settings

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=False)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_session() -> AsyncSession:  # type: ignore
    async with async_session() as session:
        yield session
