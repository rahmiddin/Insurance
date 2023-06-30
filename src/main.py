from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.db_config import settings
from src.insurance.router import router as insurance_router

app = FastAPI()

app.include_router(insurance_router)

register_tortoise(
    app,
    db_url=settings.get_database_url,
    modules={"models": ["src.insurance.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
