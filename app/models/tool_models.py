from typing import Dict, Any

# 에이전트 도구 호출 시 요청 본문 모델
# 도구별로 스키마가 다르지만, 여기서는 범용 Dict로 처리합니다.
# 사용자 정의 도구에 따라 더 구체적인 모델을 정의할 수 있습니다.
AgentToolRequestPayload = Dict[str, Any]

# 에이전트 도구 호출 응답 본문 모델
# Vox.ai 에이전트에게 전달될 JSON 응답입니다.
AgentToolResponsePayload = Dict[str, Any]
