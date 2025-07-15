from datetime import datetime, timedelta
import random
from app.core.logging import get_logger
from app.models.tool_models import AgentToolRequestPayload, AgentToolResponsePayload

logger = get_logger(__name__)


# 에이전트 도구 호출을 처리하는 서비스
class AgentToolService:
    def __init__(self):
        # 기사 목록 초기화
        self.mock_technicians = [
            {"name": "김기사", "contact": "010-1234-5678", "area": "서울/경기"},
            {"name": "박기사", "contact": "010-2345-6789", "area": "부산/울산"},
            {"name": "이기사", "contact": "010-3456-7890", "area": "대구/경북"},
            {"name": "정기사", "contact": "010-4567-8901", "area": "광주/전남"},
            {"name": "최기사", "contact": "010-5678-9012", "area": "대전/충청"},
        ]

    async def process_tool_call(
        self, tool_name: str, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        에이전트의 특정 도구 호출을 처리하고 응답을 반환합니다.
        tool_name에 따라 다른 로직을 수행합니다.
        """
        logger.info(f"에이전트 도구 호출 처리 시작: {tool_name}, 페이로드: {payload}")

        # EV 충전 시스템 도구 라우팅
        if tool_name == "monitor_ev_system":
            return await self._handle_monitor_ev_system(payload)
        elif tool_name == "control_ev_system":
            return await self._handle_control_ev_system(payload)
        elif tool_name == "create_support_ticket":
            return await self._handle_create_support_ticket(payload)
        elif tool_name == "submit_zendesk_ticket":
            return await self._handle_submit_zendesk_ticket(payload)
        elif tool_name == "check_flight_ticket":
            return await self._handle_check_flight_ticket(payload)
        else:
            logger.warning(f"알 수 없는 도구 호출: {tool_name}")
            return {
                "error": f"알 수 없는 도구: {tool_name}",
                "details": "이 도구는 백엔드에 구현되지 않았습니다.",
            }

    async def _handle_submit_zendesk_ticket(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        젠데스크 티켓 제출 도구 처리
        SOP의 '젠데스크_티켓_제출' 도구에 대응
        """
        return {
            "status": "success",
            "message": "젠데스크 티켓 제출 완료",
            "ticket_id": "1234567890",
        }

    async def _handle_check_flight_ticket(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        항공권 예매 확인 도구 처리
        SOP의 '항공권_예매_확인' 도구에 대응
        """
        return {
            "meta": {},
            "result": {
                "data": [
                    {
                        "PNR_SEQNO": 10343878,
                        "DI_FLAG": "I",
                        "STOCK_AIR_CD": "TW",
                        "STOCK_AIR_NM": "티웨이항공",
                        "TRIP_TYPE_CD": "RT",
                        "TRIP_TYPE_NM": "왕복",
                        "RSV_INWON": 2,
                        "RSV_NO": "DTJZUK",
                        "RSV_USR_NM": "이정미",
                        "RSV_STATUS_CD": "RMTK",
                        "RSV_STATUS_NM": "발권완료",
                        "DEP_DTM": "20250801195500",
                        "ARR_DTM": "20250809000500",
                        "RSV_DTM": "20250714183734",
                        "PAY_TL": "20250714183700",
                        "PNR_SEAT_STATUS_CD": "RK",
                        "PNR_SEAT_STATUS_NM": "확약",
                        "PAY_STATUS_CD": "PAQK",
                        "PAY_STATUS_NM": "결제요청",
                        "ISSUE_STATUS_CD": "TKKY",
                        "ISSUE_STATUS_NM": "발권완료",
                        "SALE_TOT_AMT": 0,
                        "SEG_RSV_YN": "Y",
                        "CANCEL_YN": "N",
                        "FARE_CONFM_YN": "Y",
                        "MIJUNG_AMT_YN": "Y",
                        "PROOF_DOC_REQUIRE_YN": "N",
                        "PROOF_DOC_CONFM_YN": "N",
                        "ALPHA_PNR_NO": "DTJZUK",
                        "ITIN_NO": 1,
                        "ITIN_BUNDLE_UNIT": "1",
                        "FLTNO": "TW191",
                        "FLT_AIR_CD": "TW",
                        "FLT_AIR_NM": "티웨이항공",
                        "DEP_CITY_CD": "TAE",
                        "DEP_CITY_NM": "대구",
                        "DEP_AIRPORT_CD": "TAE",
                        "DEP_AIRPORT_NM": "대구",
                        "DEP_DATE": "20250801",
                        "DEP_TM": "1955",
                        "ARR_CITY_CD": "NHA",
                        "ARR_CITY_NM": "나트랑",
                        "ARR_AIRPORT_CD": "CXR",
                        "ARR_AIRPORT_NM": "나트랑/캄란",
                        "ARR_DATE": "20250801",
                        "ARR_TM": "2250",
                        "AUTO_ISSUE_YN": "N",
                        "STOP_OVER_YN": "N",
                        "ATC_REISSUE_FLAG": "N",
                        "FLIGHTS_STATUS": "발권완료",
                        "FLIGHTS_STATUS_CD": "FLTY",
                        "CODESHARE_YN": "N",
                        "CODESHARE_AIR_CD": "",
                        "CODESHARE_AIR_NM": "",
                        "CODESHARE_CD_IMG": "",
                    },
                    {
                        "PNR_SEQNO": 10343878,
                        "DI_FLAG": "I",
                        "STOCK_AIR_CD": "TW",
                        "STOCK_AIR_NM": "티웨이항공",
                        "TRIP_TYPE_CD": "RT",
                        "TRIP_TYPE_NM": "왕복",
                        "RSV_INWON": 2,
                        "RSV_NO": "DTJZUK",
                        "RSV_USR_NM": "이정미",
                        "RSV_STATUS_CD": "RMTK",
                        "RSV_STATUS_NM": "발권완료",
                        "DEP_DTM": "20250801195500",
                        "ARR_DTM": "20250809000500",
                        "RSV_DTM": "20250714183734",
                        "PAY_TL": "20250714183700",
                        "PNR_SEAT_STATUS_CD": "RK",
                        "PNR_SEAT_STATUS_NM": "확약",
                        "PAY_STATUS_CD": "PAQK",
                        "PAY_STATUS_NM": "결제요청",
                        "ISSUE_STATUS_CD": "TKKY",
                        "ISSUE_STATUS_NM": "발권완료",
                        "SALE_TOT_AMT": 0,
                        "SEG_RSV_YN": "Y",
                        "CANCEL_YN": "N",
                        "FARE_CONFM_YN": "Y",
                        "MIJUNG_AMT_YN": "Y",
                        "PROOF_DOC_REQUIRE_YN": "N",
                        "PROOF_DOC_CONFM_YN": "N",
                        "ALPHA_PNR_NO": "DTJZUK",
                        "ITIN_NO": 2,
                        "ITIN_BUNDLE_UNIT": "2",
                        "FLTNO": "TW192",
                        "FLT_AIR_CD": "TW",
                        "FLT_AIR_NM": "티웨이항공",
                        "DEP_CITY_CD": "NHA",
                        "DEP_CITY_NM": "나트랑",
                        "DEP_AIRPORT_CD": "CXR",
                        "DEP_AIRPORT_NM": "나트랑/캄란",
                        "DEP_DATE": "20250809",
                        "DEP_TM": "0005",
                        "ARR_CITY_CD": "TAE",
                        "ARR_CITY_NM": "대구",
                        "ARR_AIRPORT_CD": "TAE",
                        "ARR_AIRPORT_NM": "대구",
                        "ARR_DATE": "20250809",
                        "ARR_TM": "0720",
                        "AUTO_ISSUE_YN": "N",
                        "STOP_OVER_YN": "N",
                        "ATC_REISSUE_FLAG": "N",
                        "FLIGHTS_STATUS": "발권완료",
                        "FLIGHTS_STATUS_CD": "FLTY",
                        "CODESHARE_YN": "N",
                        "CODESHARE_AIR_CD": "",
                        "CODESHARE_AIR_NM": "",
                        "CODESHARE_CD_IMG": "",
                    },
                ],
                "status": 200,
                "message": "SUCCESS",
                "code": "success",
            },
        }

    async def _handle_monitor_ev_system(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        EV 충전 시스템 상태 조회 도구 처리
        SOP의 '시스템_조회/확인' 도구에 대응
        """
        charger_id = payload.get("charger_id", "").strip()

        if not charger_id:
            return {
                "status": "error",
                "message": "충전기 번호가 제공되지 않았습니다.",
                "error_code": "MISSING_CHARGER_ID",
            }

        logger.info(f"monitor_ev_system 처리 중, charger_id: {charger_id}")

        # 랜덤으로 충전기 상태 생성
        possible_statuses = [
            {"status": "통신장애", "error_code": "85"},
            {"status": "사용불가", "error_code": "31"},
            {"status": "전원차단", "error_code": "02"},
            {"status": "비상정지", "error_code": "07"},
        ]

        # 70% 확률로 정상, 30% 확률로 다른 상태
        if random.random() < 0.7:
            charger_info = possible_statuses[0]  # 정상
        else:
            charger_info = random.choice(possible_statuses[1:])  # 오류 상태들

        response_data = {
            "status": "success",
            "charger_id": charger_id,
            "current_status": charger_info["status"],
            "error_code": charger_info.get("error_code"),
            "message": f"충전기 {charger_id} 상태: {charger_info['status']}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        logger.info(
            f"monitor_ev_system 처리 완료: {charger_id}, 상태: {charger_info['status']}"
        )
        return response_data

    async def _handle_control_ev_system(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        EV 충전 시스템 원격 제어 도구 처리
        SOP의 '원격_조치' 도구에 대응
        """
        charger_id = payload.get("charger_id", "").strip()
        action = payload.get("action", "reset").strip().lower()

        if not charger_id:
            return {
                "status": "error",
                "message": "충전기 번호가 제공되지 않았습니다.",
                "error_code": "MISSING_CHARGER_ID",
            }

        logger.info(
            f"control_ev_system 처리 중, charger_id: {charger_id}, action: {action}"
        )

        # 지원되는 원격 조치 액션
        supported_actions = {
            "reset": {
                "action_name": "시스템 리셋",
                "description": "충전기 시스템을 재부팅했습니다.",
                "estimated_time": "3-5분",
                "next_steps": "재부팅 후 3-5분 뒤에 다시 충전을 시도해 주세요.",
                "success_message": "충전기 원격 리셋이 완료되었습니다.",
            },
            "force_stop": {
                "action_name": "강제 종료",
                "description": "현재 충전 세션을 강제로 종료했습니다.",
                "estimated_time": "2-3분",
                "next_steps": "세션 종료 후 2-3분 뒤에 다시 충전을 시도해 주세요.",
                "success_message": "충전 세션 강제 종료가 완료되었습니다.",
            },
        }

        if action not in supported_actions:
            return {
                "status": "error",
                "message": f"지원되지 않는 원격 조치: {action}",
                "supported_actions": list(supported_actions.keys()),
                "error_code": "UNSUPPORTED_ACTION",
            }

        action_info = supported_actions[action]

        response_data = {
            "status": "success",
            "charger_id": charger_id,
            "action": action_info["action_name"],
            "message": action_info["success_message"],
            "next_steps": action_info["next_steps"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # 원격 조치는 항상 성공으로 시뮬레이션 (실제로는 상태 변경 안함)

        logger.info(f"control_ev_system 처리 완료: {charger_id}, action: {action}")
        return response_data

    async def _handle_create_support_ticket(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        기술지원 티켓 생성 도구 처리
        SOP의 '내부/외부_전달_및_접수' 도구에 대응
        """
        charger_id = payload.get("charger_id", "").strip()
        issue_description = payload.get("issue_description", "").strip()

        if not charger_id:
            return {
                "status": "error",
                "message": "충전기 번호가 제공되지 않았습니다.",
                "error_code": "MISSING_CHARGER_ID",
            }

        if not issue_description:
            return {
                "status": "error",
                "message": "문제 설명이 제공되지 않았습니다.",
                "error_code": "MISSING_ISSUE_DESCRIPTION",
            }

        logger.info(f"create_support_ticket 처리 중, charger_id: {charger_id}")

        # 티켓 ID 생성 (날짜 + 랜덤 번호)
        ticket_id = (
            f"AS-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
        )

        # 기사 배정 (지역별 랜덤)
        assigned_technician = random.choice(self.mock_technicians)

        visit_days = 3
        # 영업일 기준으로 계산 (주말 제외)
        visit_date = self._calculate_business_date(datetime.now(), visit_days)

        response_data = {
            "status": "success",
            "ticket_id": ticket_id,
            "charger_id": charger_id,
            "issue_description": issue_description,
            "estimated_visit_date": visit_date.strftime("%Y-%m-%d"),
            "message": f"기술지원 티켓 {ticket_id}가 생성되었습니다. 담당 기사가 연락드릴 예정입니다.",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        logger.info(
            f"create_support_ticket 처리 완료: {ticket_id}, 담당자: {assigned_technician['name']}"
        )
        return response_data

    def _calculate_business_date(
        self, start_date: datetime, business_days: int
    ) -> datetime:
        """영업일 기준으로 날짜 계산 (주말 제외)"""
        current_date = start_date
        days_added = 0

        while days_added < business_days:
            current_date += timedelta(days=1)
            # 월요일(0)부터 금요일(4)까지만 영업일로 계산
            if current_date.weekday() < 5:
                days_added += 1

        return current_date
