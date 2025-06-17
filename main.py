from fastapi import FastAPI
from app.core.logging import get_logger
from app.api.v1.endpoints import call_webhooks, agent_tools, inbound_webhook

# 로거 초기화
logger = get_logger(__name__)

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="Vox.ai Integration Client Server",
    description="Vox.ai 웹훅 및 API 도구 연동을 위한 고객사 서버",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 라우터 포함
app.include_router(call_webhooks.router, prefix="/api/v1", tags=["Call Webhooks"])
app.include_router(agent_tools.router, prefix="/api/v1", tags=["Agent Tools"])
app.include_router(inbound_webhook.router, prefix="/api/v1", tags=["Inbound Webhook"])


@app.get("/", include_in_schema=False)
async def root():
    """기본 경로 (헬스 체크용)"""
    return {"message": "Vox.ai Integration Skeleton Server is running."}


# 서버 실행 방법 안내 (주석)
# 터미널에서 아래 명령어를 실행하세요:
# poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
#
# .env 파일을 생성하여 환경 변수를 설정해야 합니다. (.env.example 참고)
