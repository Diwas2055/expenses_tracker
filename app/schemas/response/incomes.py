import uuid
from pydantic import BaseModel
from app.schemas.response.user import UserResponse


class IncomesResponse(BaseModel):
    id: uuid.UUID
    amount: float
    description: str
    user_id: int
    user: UserResponse
    created_at: str

    class Config:
        orm_mode = True
