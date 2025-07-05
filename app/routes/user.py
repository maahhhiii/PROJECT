from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, auth, utils, database

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    print("Received registration request:", user.dict())
    
    try:
        utils.validate_password_strength(user.password)
    except Exception as e:
        print("Password validation failed:", e)
        raise HTTPException(status_code=400, detail=str(e))

    hashed = auth.hash_password(user.password)
    print("Password hashed.")

    new_user = models.User(username=user.username, password=hashed, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "user registered"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}