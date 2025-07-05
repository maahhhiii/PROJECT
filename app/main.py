from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.database import Base, engine
from app.routes import user, announcement, lost_found

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(
    title="Student Community Portal",
    description="Login/Register, Announcements, and Lost & Found module",
    version="1.0.0"
)

# ADD THIS FUNCTION BELOW app = FastAPI(...)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    # Apply BearerAuth to all paths
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Tell FastAPI to use this function
app.openapi = custom_openapi

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the student Community Portal"}

# Include all routers
app.include_router(user.router)
app.include_router(announcement.router)
app.include_router(lost_found.router)