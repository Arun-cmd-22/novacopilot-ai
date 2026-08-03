from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers.auth import router as auth_router
from app.routers.users import router as user_router
from app.routers.roles import router as role_router
from app.routers.permissions import router as permission_router
from app.routers.role_permissions import router as role_permission_router
from app.routers.ai_models import router as ai_model_router
from app.routers.chat_session import router as chat_session_router
from app.routers.message import router as message_router
from app.routers import chat
from app.routers.ai_prompt_template import router as ai_prompt_template_router
from app.routers.ai_code import router as ai_code_router
from app.routers.ai_sql import router as ai_sql_router
from app.routers.ai_explain import router as ai_explain_router
from app.routers.ai_debug import router as ai_debug_router
from app.routers.ai_erp import router as ai_erp_router





app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(permission_router)
app.include_router(role_permission_router)
app.include_router(ai_model_router)
app.include_router(chat.router)
app.include_router(chat_session_router)
app.include_router(message_router)
app.include_router(ai_prompt_template_router)
app.include_router(ai_code_router)
app.include_router(ai_sql_router)
app.include_router(ai_explain_router)
app.include_router(ai_debug_router)
app.include_router(ai_erp_router)

@app.get("/")
async def home():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "status": "Running",
    }


@app.get("/health")
async def health():
    return {
        "status": "OK",
    }