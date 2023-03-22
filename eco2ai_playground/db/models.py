from datetime import datetime

from sqlalchemy import ForeignKey, MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

convention = {
    "all_column_names": lambda constraint, _: "_".join(
        [column.name for column in constraint.columns.values()]
    ),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s",
    "pk": "pk__%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)


class Project(Base):
    __tablename__ = "project"
    project_id: Mapped[str] = mapped_column(String(32), primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(String(256))
    start_time: Mapped[datetime]
    cpu: Mapped[str] = mapped_column(String(128))
    gpu: Mapped[str] = mapped_column(String(128))
    os: Mapped[str] = mapped_column(String(64))
    region: Mapped[str] = mapped_column(String(128))

    consumptions: Mapped[list["Consumption"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )


class Consumption(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    __tablename__ = "consumption"
    project_id: Mapped[str] = mapped_column(ForeignKey("project.project_id"))
    project: Mapped["Project"] = relationship(back_populates="consumptions")
    epoch_str: Mapped[str] = mapped_column(String(128))
    duration: Mapped[float]
    power: Mapped[float]
    co2: Mapped[float]
    cost: Mapped[float]
