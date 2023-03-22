from datetime import datetime

from pydantic import UUID4, BaseModel, Field


class ConsumptionListStrInPydantic(BaseModel):
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


class ConsumptionInPydantic(BaseModel):
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
