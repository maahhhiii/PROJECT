from pydantic import BaseModel

# ---------------- USER ----------------

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "student"


class UserLogin(BaseModel):
    username: str
    password: str


# ---------------- ANNOUNCEMENT ----------------

class AnnouncementBase(BaseModel):
    title: str
    content: str


class AnnouncementOut(AnnouncementBase):
    id: int
    posted_by: str

    
    model_config = {
        "from_attributes": True
    }


# ---------------- LOST ITEM ----------------

class LostItemBase(BaseModel):
    title: str
    description: str


class LostItemOut(LostItemBase):
    id: int
    owner: str

    # FIX for Pydantic v2
    model_config ={
        "from_attributes":True
    }