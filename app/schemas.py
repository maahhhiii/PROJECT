from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "student"

class UserLogin(BaseModel):
    username: str
    password: str

class AnnouncementBase(BaseModel):
    title: str
    content: str

class AnnouncementOut(AnnouncementBase):
    id: int
    posted_by: str
    class Config:
        orm_mode = True

class LostItemBase(BaseModel):
    title: str
    description: str

class LostItemOut(LostItemBase):
    id: int
    owner: str
    class Config:
        orm_mode = True