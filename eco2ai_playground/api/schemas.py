from datetime import datetime
from enum import Enum
from typing import Generic, TypeVar

from pydantic import UUID4, BaseModel, Field
from pydantic.generics import GenericModel


class ConsumptionListStrIn(BaseModel):
    id: list[str]
    project_name: list[str]
    experiment_description: list[str]
    epoch: list[str]
    start_time: list[str]
    durations: list[str] = Field(alias="duration(s)")
    power_consumption: list[str] = Field(alias="power_consumption(kWh)")
    co2_emissions: list[str] = Field(alias="CO2_emissions(kg)")
    cpu_name: list[str] = Field(alias="CPU_name")
    gpu_name: list[str] = Field(alias="GPU_name")
    os: list[str] = Field(alias="OS")
    region: list[str] = Field(alias="region/country")

    def convert_to_dict(self) -> dict[str, str]:
        return {field: value[0] for field, value in self.dict().items()}


class ConsumptionIn(BaseModel):
    id: UUID4
    project_name: str
    experiment_description: str
    epoch: str
    start_time: datetime
    durations: float
    power_consumption: float
    co2_emissions: float
    cpu_name: str
    gpu_name: str
    os: str
    region: str


class ConsumptionDB(BaseModel):
    duration: str
    power: float
    co2: float

    class Config:
        orm_mode = True


class ConsumptionInProjectDB(BaseModel):
    duration: str
    power: float
    co2: float

    class Config:
        orm_mode = True


class ProjectWithConsumptionsDB(BaseModel):
    project_id: UUID4
    name: str
    description: str
    start_time: datetime
    cpu: str
    gpu: str
    os: str
    region: str
    consumptions: list[ConsumptionInProjectDB]

    class Config:
        orm_mode = True


NotificationItem = TypeVar("NotificationItem", bound=BaseModel)


class NotificationType(str, Enum):
    new_consumption = "new_consumption"


class Notification(GenericModel, Generic[NotificationItem]):
    type: NotificationType
    project_id: UUID4
    data: NotificationItem
