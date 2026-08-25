from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    starred: bool

    class Config:
        from_attributes = True