from fastapi import FastAPI
from src.app.lifespan import lifespan
from src.app.api.v1.users import router as users_router
from src.app.api.v1.notifications import router as notifications_router


app = FastAPI(
    title="Notification API",
    description="API для уведомлений",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.include_router(users_router, prefix="/api/v1")
app.include_router(notifications_router, prefix="/api/v1")
