from abc import ABC, abstractmethod
from typing import Dict, Any, Union, Literal
from app.models.webhook_models import CallStartedPayload, CallEndedPayload


# 콜 데이터 웹훅 이벤트에 대한 핸들러 기본 클래스
# 각 시나리오(Make.com, DB 등)별 핸들러는 이 클래스를 상속받습니다.
class BaseCallEventHandler(ABC):

    @abstractmethod
    async def handle(
        self,
        event_type: Literal["call_started", "call_ended"],
        payload: Union[CallStartedPayload, CallEndedPayload],
    ):
        """
        콜 웹훅 이벤트를 처리합니다.
        구체적인 처리 로직은 상속받는 클래스에서 구현해야 합니다.
        """
        pass
