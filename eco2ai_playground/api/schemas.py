from datetime import datetime
from enum import Enum
from typing import Generic, TypeVar, Union

from pydantic import UUID4, BaseModel, Field, ValidationError, field_serializer


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


class Epoch(BaseModel):
    epoch: int
    train_loss: float
    train_accuracy: float
    test_loss: float
    test_accuracy: float


class ConsumptionDB(BaseModel):
    duration: float
    power: float
    co2: float
    epoch_str: Epoch | str | None

    @field_serializer("epoch_str")
    def serialize_epoch(self, epoch_str: str) -> Union[Epoch, None]:
        if epoch_str == "N/A":
            return None

        epoch_splited = epoch_str.split(",")
        epoch_entries = map(lambda x: x.split(":"), epoch_splited)
        epoch_filtered = [epoch for epoch in epoch_entries if len(epoch) == 2]
        epoch_dict = {
            key.strip(): value.strip() for key, value in epoch_filtered
        }

        print(epoch_dict)

        try:
            return Epoch(**epoch_dict)
        except ValidationError as ex:
            print(ex)
            return None

    class Config:
        from_attributes = True


class ConsumptionInProjectDB(ConsumptionDB):
    class Config:
        from_attributes = True


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
        from_attributes = True


NotificationItem = TypeVar("NotificationItem", bound=BaseModel)


class NotificationType(str, Enum):
    new_consumption = "new_consumption"


class Notification(BaseModel, Generic[NotificationItem]):
    type: NotificationType
    project_id: UUID4
    data: NotificationItem
