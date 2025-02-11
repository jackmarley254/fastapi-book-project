from fastapi import FastAPI
from routes.books import router as books_router
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)
app.include_router(books_router, prefix="/api/v1/books")

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}