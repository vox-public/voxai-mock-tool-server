from datetime import datetime, timedelta
import random
import re
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
        elif tool_name == "validate_pnr_format":
            return await self._handle_validate_pnr_format(payload)
        elif tool_name == "determine_urgency_and_sla":
            return await self._handle_determine_urgency_and_sla(payload)
        elif tool_name == "schedule_priority_callback":
            return await self._handle_schedule_priority_callback(payload)
        elif tool_name == "submit_detailed_zendesk_ticket":
            return await self._handle_submit_detailed_zendesk_ticket(payload)
        elif tool_name == "save_csat_survey":
            return await self._handle_save_csat_survey(payload)
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
                        "PNR_SEQNO": 10456789,
                        "DI_FLAG": "I",
                        "STOCK_AIR_CD": "KE",
                        "STOCK_AIR_NM": "대한항공",
                        "TRIP_TYPE_CD": "RT",
                        "TRIP_TYPE_NM": "왕복",
                        "RSV_INWON": 3,
                        "RSV_NO": "KFMNPQ",
                        "RSV_USR_NM": "김민지",
                        "RSV_STATUS_CD": "RMTK",
                        "RSV_STATUS_NM": "발권완료",
                        "DEP_DTM": "20250915141000",
                        "ARR_DTM": "20250922092000",
                        "RSV_DTM": "20250820094523",
                        "PAY_TL": "20250820094500",
                        "PNR_SEAT_STATUS_CD": "RK",
                        "PNR_SEAT_STATUS_NM": "확약",
                        "PAY_STATUS_CD": "PAQK",
                        "PAY_STATUS_NM": "결제완료",
                        "ISSUE_STATUS_CD": "TKKY",
                        "ISSUE_STATUS_NM": "발권완료",
                        "SALE_TOT_AMT": 1280000,
                        "SEG_RSV_YN": "Y",
                        "CANCEL_YN": "N",
                        "FARE_CONFM_YN": "Y",
                        "MIJUNG_AMT_YN": "N",
                        "PROOF_DOC_REQUIRE_YN": "N",
                        "PROOF_DOC_CONFM_YN": "N",
                        "ALPHA_PNR_NO": "KFMNPQ",
                        "ITIN_NO": 1,
                        "ITIN_BUNDLE_UNIT": "1",
                        "FLTNO": "KE647",
                        "FLT_AIR_CD": "KE",
                        "FLT_AIR_NM": "대한항공",
                        "DEP_CITY_CD": "ICN",
                        "DEP_CITY_NM": "인천",
                        "DEP_AIRPORT_CD": "ICN",
                        "DEP_AIRPORT_NM": "인천국제공항",
                        "DEP_DATE": "20250915",
                        "DEP_TM": "1410",
                        "ARR_CITY_CD": "BKK",
                        "ARR_CITY_NM": "방콕",
                        "ARR_AIRPORT_CD": "BKK",
                        "ARR_AIRPORT_NM": "방콕 수완나품",
                        "ARR_DATE": "20250915",
                        "ARR_TM": "1755",
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
                        "PNR_SEQNO": 10456789,
                        "DI_FLAG": "I",
                        "STOCK_AIR_CD": "KE",
                        "STOCK_AIR_NM": "대한항공",
                        "TRIP_TYPE_CD": "RT",
                        "TRIP_TYPE_NM": "왕복",
                        "RSV_INWON": 3,
                        "RSV_NO": "KFMNPQ",
                        "RSV_USR_NM": "박서현",
                        "RSV_STATUS_CD": "RMTK",
                        "RSV_STATUS_NM": "발권완료",
                        "DEP_DTM": "20250915141000",
                        "ARR_DTM": "20250922092000",
                        "RSV_DTM": "20250820094523",
                        "PAY_TL": "20250820094500",
                        "PNR_SEAT_STATUS_CD": "RK",
                        "PNR_SEAT_STATUS_NM": "확약",
                        "PAY_STATUS_CD": "PAQK",
                        "PAY_STATUS_NM": "결제완료",
                        "ISSUE_STATUS_CD": "TKKY",
                        "ISSUE_STATUS_NM": "발권완료",
                        "SALE_TOT_AMT": 1280000,
                        "SEG_RSV_YN": "Y",
                        "CANCEL_YN": "N",
                        "FARE_CONFM_YN": "Y",
                        "MIJUNG_AMT_YN": "N",
                        "PROOF_DOC_REQUIRE_YN": "N",
                        "PROOF_DOC_CONFM_YN": "N",
                        "ALPHA_PNR_NO": "KFMNPQ",
                        "ITIN_NO": 2,
                        "ITIN_BUNDLE_UNIT": "2",
                        "FLTNO": "KE648",
                        "FLT_AIR_CD": "KE",
                        "FLT_AIR_NM": "대한항공",
                        "DEP_CITY_CD": "BKK",
                        "DEP_CITY_NM": "방콕",
                        "DEP_AIRPORT_CD": "BKK",
                        "DEP_AIRPORT_NM": "방콕 수완나품",
                        "DEP_DATE": "20250922",
                        "DEP_TM": "0920",
                        "ARR_CITY_CD": "ICN",
                        "ARR_CITY_NM": "인천",
                        "ARR_AIRPORT_CD": "ICN",
                        "ARR_AIRPORT_NM": "인천국제공항",
                        "ARR_DATE": "20250922",
                        "ARR_TM": "1630",
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

    async def _handle_validate_pnr_format(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        PNR 번호 형식 검증 도구
        SOP Phase 2.1.b에 대응
        """
        pnr_input = payload.get("pnr_input", "").strip().upper()
        
        if not pnr_input:
            return {
                "status": "error",
                "message": "PNR 번호가 제공되지 않았습니다.",
                "valid": False,
                "error_code": "MISSING_PNR"
            }
        
        # PNR 형식 검증: 6자리 영문+숫자 조합
        pnr_pattern = re.compile(r'^[A-Z0-9]{6}$')
        
        if pnr_pattern.match(pnr_input):
            return {
                "status": "success",
                "message": "유효한 PNR 형식입니다.",
                "valid": True,
                "pnr": pnr_input
            }
        else:
            return {
                "status": "error", 
                "message": "잘못된 PNR 형식입니다. 6자리 영문과 숫자 조합이어야 합니다.",
                "valid": False,
                "error_code": "INVALID_PNR_FORMAT"
            }

    async def _handle_determine_urgency_and_sla(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        긴급도 및 SLA 자동 판정 도구
        SOP Phase 4.1.a에 대응
        """
        inquiry_keywords = payload.get("inquiry_keywords", "")
        
        # 키워드 문자열을 리스트로 변환
        keywords_list = [keyword.strip() for keyword in inquiry_keywords.split(",") if keyword.strip()]
        
        urgency = "Normal"
        assigned_team = "일반상담팀"
        
        # 키워드 기반 판정
        urgent_keywords = ["긴급", "오늘", "지금", "당장", "공항", "출발"]
        change_keywords = ["변경", "수정", "바꾸기"]
        refund_keywords = ["환불", "취소", "돌려받기"]
        
        keywords_text = " ".join(keywords_list)
        
        if any(keyword in keywords_text for keyword in urgent_keywords):
            urgency = "Critical"
        
        if any(keyword in keywords_text for keyword in change_keywords):
            assigned_team = "항공권 변경팀"
        elif any(keyword in keywords_text for keyword in refund_keywords):
            assigned_team = "환불팀"
        
        return {
            "status": "success",
            "urgency": urgency,
            "assigned_team": assigned_team,
            "message": f"긴급도: {urgency}, 담당팀: {assigned_team}로 판정되었습니다.",
            "keywords_processed": keywords_list
        }

    async def _handle_schedule_priority_callback(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        우선순위 콜백 스케줄링 도구
        SOP Phase 4.2.a에 대응
        """
        inquiry_summary = payload.get("inquiry_summary", "")
        urgency = payload.get("urgency", "Normal")
        
        # 콜백 ID 생성
        callback_id = f"CB-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
        
        # 우선순위별 예상 대기시간
        if urgency == "Critical":
            estimated_wait_time = "5분 이내"
            priority_level = 1
        elif urgency == "High":
            estimated_wait_time = "15분 이내"
            priority_level = 2
        else:
            estimated_wait_time = "30분 이내"
            priority_level = 3
        
        return {
            "status": "success",
            "callback_id": callback_id,
            "priority_level": priority_level,
            "estimated_wait_time": estimated_wait_time,
            "message": f"최우선 콜백이 접수되었습니다. {estimated_wait_time} 연락드릴 예정입니다.",
            "scheduled_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "inquiry_summary": inquiry_summary
        }

    async def _handle_submit_detailed_zendesk_ticket(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        상세 젠데스크 티켓 제출 도구
        SOP Phase 4.2.b에 대응
        """
        urgency = payload.get("urgency", "Normal")
        assigned_team = payload.get("assigned_team", "일반상담팀")
        
        # 티켓 ID 생성
        ticket_id = f"ZD-{datetime.now().strftime('%Y%m%d')}-{random.randint(10000, 99999)}"
        
        # 우선순위별 SLA 시간
        sla_hours = {
            "Critical": 2,
            "High": 8,
            "Normal": 24
        }
        
        expected_resolution = datetime.now() + timedelta(hours=sla_hours.get(urgency, 24))
        
        return {
            "status": "success",
            "ticket_id": ticket_id,
            "urgency": urgency,
            "assigned_team": assigned_team,
            "sla_hours": sla_hours.get(urgency, 24),
            "expected_resolution": expected_resolution.strftime("%Y-%m-%d %H:%M:%S"),
            "message": f"상세 티켓 {ticket_id}가 {assigned_team}에 접수되었습니다.",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    async def _handle_save_csat_survey(
        self, payload: AgentToolRequestPayload
    ) -> AgentToolResponsePayload:
        """
        고객 만족도 조사 결과 저장 도구
        SOP Phase 5.2.e에 대응
        """
        score = payload.get("score", "")
        
        if not score:
            return {
                "status": "error",
                "message": "점수가 제공되지 않았습니다.",
                "error_code": "MISSING_SCORE"
            }
        
        try:
            score_int = int(score)
            if not (1 <= score_int <= 5):
                return {
                    "status": "error",
                    "message": "점수는 1-5 사이여야 합니다.",
                    "error_code": "INVALID_SCORE_RANGE"
                }
        except ValueError:
            return {
                "status": "error",
                "message": "점수는 숫자여야 합니다.",
                "error_code": "INVALID_SCORE_FORMAT"
            }
        
        # 점수별 만족도 레벨
        satisfaction_levels = {
            1: "매우 불만족",
            2: "불만족", 
            3: "보통",
            4: "만족",
            5: "매우 만족"
        }
        
        return {
            "status": "success",
            "score": score_int,
            "satisfaction_level": satisfaction_levels[score_int],
            "message": "고객 만족도 조사 결과가 저장되었습니다.",
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "feedback_id": f"CSAT-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
        }
