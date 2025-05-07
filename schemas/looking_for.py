from pydantic import BaseModel


class LookingFor(BaseModel):
    name: str
