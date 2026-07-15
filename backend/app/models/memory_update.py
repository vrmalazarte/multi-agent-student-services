from pydantic import BaseModel


class MemoryUpdate(BaseModel):
    key: str
    value: str