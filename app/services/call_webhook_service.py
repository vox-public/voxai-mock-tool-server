from typing import List, Union, Literal
from app.models.webhook_models import CallStartedPayload, CallEndedPayload
from app.core.logging import get_logger
from .handlers.make_com_handler import MakeComHandler
from .handlers.database_handler import DatabaseHandler
from .handlers.custom_url_handler import CustomUrlHandler
from .handlers.base_handler import BaseCallEventHandler

logger = get_logger(__name__)


# 콜 데이터 웹훅 이벤트를 받아 여러 핸들러에게 전달하는 서비스
class CallWebhookService:

    def __init__(self):
        """핸들러 인스턴스를 초기화하고 등록합니다."""
        # 여기에 필요한 다른 핸들러들을 추가하세요.
        self.handlers: List[BaseCallEventHandler] = [
            MakeComHandler(),
            DatabaseHandler(),  # 예시: DB 저장 핸들러
            CustomUrlHandler(),  # 예시: 커스텀 서버 전송 핸들러
        ]
        logger.info(
            f"{len(self.handlers)}개의 핸들러로 CallWebhookService를 초기화했습니다."
        )

    async def process_webhook_event(
        self,
        event_type: Literal["call_started", "call_ended"],
        payload: Union[CallStartedPayload, CallEndedPayload],
    ):
        """
        받은 웹훅 이벤트를 등록된 모든 핸들러에게 전달합니다.
        각 핸들러는 순차적으로 실행됩니다.
        """
        logger.info(f"통화 웹훅 이벤트 처리 시작: {event_type}")

        # 순차 실행 (디버깅 및 로깅에 더 용이할 수 있음)
        for handler in self.handlers:
            try:
                handler_name = handler.__class__.__name__
                logger.info(f"핸들러 실행: {handler_name} (이벤트: {event_type})")
                await handler.handle(event_type, payload)
                logger.info(f"핸들러 {handler_name} 실행 완료 (이벤트: {event_type})")
            except Exception as e:
                # 특정 핸들러 실패가 전체 요청을 중단시키지 않도록 예외 처리
                logger.error(
                    f"핸들러 {handler_name} 실행 중 오류 발생 (이벤트: {event_type}): {e}"
                )

        logger.info(f"통화 웹훅 이벤트 처리 완료: {event_type}")

        return {
            "message": f"통화 웹훅 이벤트 '{event_type}'가 서비스에 의해 처리되었습니다."
        }
