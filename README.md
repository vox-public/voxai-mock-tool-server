# VoxAI 연동을 위한 FastAPI 서버 (고객사용)

이 프로젝트는 Vox.ai의 웹훅(Webhook) 및 API 도구 기능을 고객사 시스템에 쉽게 연동할 수 있도록 돕기 위해 제작된 FastAPI 기반의 스켈레톤 서버입니다.

## 목적

-   **빠른 시작:** 고객사가 Vox.ai의 다양한 기능을 최소한의 설정으로 빠르게 테스트하고 도입할 수 있도록 지원합니다.
-   **높은 확장성:** 잘 정의된 구조를 통해 새로운 기능을 추가하거나 기존 로직을 수정하기 용이하게 설계되었습니다.
-   **쉬운 이해:** 직관적인 코드와 상세한 주석을 통해 개발자가 쉽게 이해하고 활용할 수 있도록 합니다.

## 주요 기능

이 스켈레톤 서버는 Vox.ai의 세 가지 주요 연동 포인트를 처리합니다.

1.  **통화 데이터 웹훅 (`/api/v1/call_events`):** 통화 시작(`call_started`) 및 종료(`call_ended`) 시 발생하는 이벤트를 수신하여 다양한 후속 작업을 처리합니다.
2.  **에이전트 API 도구 (`/api/v1/tools/{tool_name}`):** Vox.ai 에이전트가 대화 중 필요한 작업을 수행하기 위해 호출하는 외부 API 엔드포인트를 제공합니다.
3.  **인바운드 콜 웹훅 (`/api/v1/inbound`):** 인바운드 콜이 시작될 때 동적 변수(`dynamic_variables`)와 메타데이터(`metadata`)를 제공하여 개인화된 응대를 가능하게 합니다.

## 프로젝트 구조

프로젝트는 역할과 책임에 따라 명확하게 분리된 모듈식 구조를 따릅니다.

```
.
├── .gitignore
├── README.md           # (현재 파일) 프로젝트 안내 문서
├── main.py             # FastAPI 애플리케이션의 메인 진입점
├── poetry.lock         # 의존성 버전 잠금 파일
├── pyproject.toml      # Poetry 프로젝트 설정 및 의존성 관리
└── app/
    ├── __init__.py
    ├── api/            # API 라우터 (엔드포인트) 정의
    │   └── v1/
    │       └── endpoints/
    │           ├── agent_tools.py      # 에이전트 도구 라우터
    │           ├── call_webhooks.py    # 통화 데이터 웹훅 라우터
    │           └── inbound_webhook.py  # 인바운드 콜 웹훅 라우터
    ├── core/           # 핵심 컴포넌트 (설정, 로깅 등)
    │   ├── config.py
    │   └── logging.py
    ├── models/         # Pydantic 데이터 모델 (요청/응답 스키마)
    │   ├── tool_models.py
    │   └── webhook_models.py
    └── services/       # 비즈니스 로직
        ├── agent_tool_service.py
        ├── call_webhook_service.py
        ├── inbound_webhook_service.py
        └── handlers/   # 웹훅 이벤트를 처리하는 구체적인 핸들러
            ├── base_handler.py
            ├── custom_url_handler.py
            ├── database_handler.py
            └── make_com_handler.py
```

## 설정 및 실행 방법

### 1. 필수 요구사항

-   Python 3.8+
-   Poetry (의존성 관리 도구)

### 2. 저장소 복제

```bash
git clone <repository_url>
cd voxai-client-server
```

### 3. 의존성 설치

Poetry를 사용하여 필요한 패키지를 설치합니다.

```bash
poetry install
```

### 4. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 필요한 환경 변수를 설정합니다. `.env.example` 파일을 복사하여 사용할 수 있습니다.

```bash
cp .env.example .env
```

`.env` 파일을 열어 각 변수에 실제 값을 입력하세요.

```dotenv
# .env
# 예시: Make.com 웹훅 URL (필요한 경우)
MAKE_COM_WEBHOOK_URL="https://hook.us2.make.com/your-webhook-id"

# 예시: 커스텀 서버 웹훅 URL (필요한 경우)
CUSTOM_SERVER_WEBHOOK_URL="https://your-custom-server.com/webhook"

# 예시: 데이터베이스 연결 URL (필요한 경우)
DATABASE_URL="postgresql://user:password@host:port/dbname"
```

### 5. 서버 실행

Poetry 스크립트를 사용하여 FastAPI 개발 서버를 실행합니다. `--reload` 플래그 덕분에 코드가 변경될 때마다 서버가 자동으로 재시작됩니다.

```bash
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

서버가 성공적으로 실행되면 터미널에 다음과 같은 메시지가 나타납니다.

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx]
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

이제 웹 브라우저에서 [http://localhost:8000/docs](http://localhost:8000/docs) 로 접속하여 API 문서를 확인할 수 있습니다.

## 확장 방법

### 새 웹훅 핸들러 추가

통화 데이터 웹훅(`call_started`, `call_ended`)에 대한 새로운 처리 로직(예: Slack 알림)을 추가하려면:

1.  `app/services/handlers/` 디렉토리에 `slack_handler.py`와 같은 새 핸들러 파일을 생성합니다.
2.  `BaseCallEventHandler`를 상속받아 `handle` 메서드를 구현합니다.
3.  `app/services/call_webhook_service.py` 파일에서 새 핸들러를 임포트하고 `self.handlers` 리스트에 추가합니다.

### 새 에이전트 도구 로직 추가

새로운 API 도구(예: `get_order_status`)를 추가하려면:

1.  `app/services/agent_tool_service.py` 파일에 `_handle_get_order_status`와 같은 비공개 메서드를 추가하여 실제 로직을 구현합니다.
2.  `process_tool_call` 메서드 내에서 `tool_name`에 따라 새로 만든 메서드를 호출하도록 분기 로직을 추가합니다.

## 보안 고려 사항

Vox.ai 서버와 연동 시 보안을 강화하기 위해, 서버의 방화벽이나 클라우드 보안 그룹에서 Vox.ai의 고정 IP 주소からの 요청만 허용하는 것이 좋습니다.

-   **Vox.ai Whitelist IP:** `34.123.198.226` 