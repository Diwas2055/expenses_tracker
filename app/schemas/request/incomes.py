from pydantic import BaseModel


class IncomeCreate(BaseModel):
    amount: float
    description: str

    class Config:
        """Configure this Schema."""

        orm_mode = True
