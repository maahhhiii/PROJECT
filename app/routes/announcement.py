from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app import models, schemas, auth, database

router = APIRouter()

def get_current_user(token: str = Header(...)):
    username = auth.decode_token(token)
    if not username:
        raise HTTPException(status_code=403, detail="Invalid token")
    return username

@router.post("/announcements")
def post_announcement(announcement: schemas.AnnouncementBase, db: Session = Depends(database.get_db), username: str = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can post announcements")
    new = models.Announcement(title=announcement.title, content=announcement.content, posted_by=username)
    db.add(new)
    db.commit()
    return {"msg": "Posted"}

@router.get("/announcements", response_model=list[schemas.AnnouncementOut])
def get_all(db: Session = Depends(database.get_db)):
    return db.query(models.Announcement).all()

@router.get("/announcements/{id}", response_model=schemas.AnnouncementOut)
def get_one(id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Announcement).filter(models.Announcement.id == id).first()

@router.delete("/announcements/{id}")
def delete_announcement(
    id: int,
    token: str = Header(...),
    db: Session = Depends(database.get_db)):
    username = auth.decode_token(token)
    if not username:
        raise HTTPException(status_code=403, detail="Invalid token")

    user = db.query(models.User).filter(models.User.username == username).first()
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete announcements")

    announcement = db.query(models.Announcement).filter(models.Announcement.id == id).first()
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")

    db.delete(announcement)
    db.commit()

    return {"msg": "Announcement deleted"}