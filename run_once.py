from app import models, database, auth

db = next(database.get_db())

# Avoid inserting duplicate admin
existing = db.query(models.User).filter(models.User.username == "admin").first()
if not existing:
    admin = models.User(
        username="admin",
        password=auth.hash_password("Admin@123"),
        role="admin"
    )
    db.add(admin)
    db.commit()
    print(" Admin user created")
else:
    print(" Admin user already exists")