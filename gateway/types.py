from typing import TypedDict


class DataEntry(TypedDict):
    device_id: str  # mac-address
    time: int       # unix-time
    temperature: float
    humidity: float


class Payload(TypedDict):
    values: list[list[str, str, str, str]]
