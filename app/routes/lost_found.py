from fastapi import APIRouter, Depends, HTTPException, Header, UploadFile, File
from sqlalchemy.orm import Session
from app import models, schemas, auth, database
import shutil
import os

router = APIRouter()

#  Auth function to get current user from token
def get_current_user(token: str = Header(...)):
    username = auth.decode_token(token)
    if not username:
        raise HTTPException(status_code=403, detail="Invalid or missing token")
    return username

#  Create Lost Item
@router.post("/lost-found")
def create_lost_item(item: schemas.LostItemBase, db: Session = Depends(database.get_db), username: str = Depends(get_current_user)):
    new_item = models.LostItem(title=item.title, description=item.description, owner=username)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"msg": "Lost item created", "id": new_item.id}

#  Read All Lost Items
@router.get("/lost-found", response_model=list[schemas.LostItemOut])
def get_all_items(db: Session = Depends(database.get_db)):
    return db.query(models.LostItem).all()

#  Read Lost Item by ID
@router.get("/lost-found/{id}", response_model=schemas.LostItemOut)
def get_lost_item(id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.LostItem).filter(models.LostItem.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

#  Update Lost Item
@router.put("/lost-found/{id}")
def update_item(id: int, updated: schemas.LostItemBase, db: Session = Depends(database.get_db), username: str = Depends(get_current_user)):
    item = db.query(models.LostItem).filter(models.LostItem.id == id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner != username:
        raise HTTPException(status_code=403, detail="You can only update your own item")

    item.title = updated.title
    item.description = updated.description
    db.commit()
    return {"msg": "Item updated"}

#  Delete Lost Item (Role-based access)
@router.delete("/lost-found/{id}")
def delete_item(id: int, db: Session = Depends(database.get_db), username: str = Depends(get_current_user)):
    item = db.query(models.LostItem).filter(models.LostItem.id == id).first()
    user = db.query(models.User).filter(models.User.username == username).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if user.role != "admin" and item.owner != username:
        raise HTTPException(status_code=403, detail="Only admins or item owners can delete")

    db.delete(item)
    db.commit()
    return {"msg": "Item deleted"}

#  OPTIONAL: File Upload Endpoint (for future use)
@router.post("/lost-found/upload/")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

