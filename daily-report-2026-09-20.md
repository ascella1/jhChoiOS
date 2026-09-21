# jhChoiOS Daily Report — 2026-09-20

## 신호 요약 (Top, 전체는 각 리서치 파일 참고)
| ID | 요약 | 지역 |
|----|------|------|
| P001 | 동물병원 진료비 병원마다 최대 61~150배 격차, 사전 비교 불가 | 한국 |
| P004 | 아파트 관리비 산출 내역 불투명 | 한국 |
| P014 | 헬스장 멤버십 해지가 의도적으로 어렵게 설계됨(뉴욕시 입법까지) | 전세계(미국) |
| P015 | Dependabot 자동 PR 노이즈로 개발자 업무 방해(GitHub Issue 원문 확인) | 전세계(개발자) |
| P020 | 여러 증권계좌 자산배분 수작업 통합(스크립트까지 작성한 사례) | 전세계(미국) |
| S002 | 챌린저스: 보증금+손실회피로 달성률 90% | 한국 |
| S010 | ふるさと納税: 매년 반복기부+답례품 리피트(14회 리피트 사례) | 일본 |
| S013 | Strava: 세그먼트 경쟁+Kudos로 유지되는 유료 구독 | 전세계 |

(Negative 전체 P001~P020: research/negative-2026-09-20-1.md, Positive 전체 S001~S020: research/positive-2026-09-20-1.md)

## 실행 요약
| Agent | 상태 | 산출물 |
|---|---|---|
| negative | **완료 (20/20)** | research/negative-2026-09-20-1.md |
| positive | **완료 (20/20)** | research/positive-2026-09-20-1.md |
| manager | 완료 (11개 아이디어) | research/manager-2026-09-20-1.md |
| market | 완료 (11개 전체 평가) | market/2026-09-20-1.md |
| ceo | 완료 | ceo/ceo-2026-09-20.md, ceo/ceo-performance.md |

Negative/Positive는 병렬 서브에이전트로, Manager/CEO 종합은 메인 세션이 직접, Market은 별도 서브에이전트로 순차 실행. 어제(9/21 파일)의 12/20, 8/20 대비 오늘은 목표를 완전히 달성했다.

## 핵심 발견
1. **인프라 제약 확인**: 이번 세션은 WebFetch가 github.com을 제외한 거의 모든 외부 도메인에서 `EGRESS_BLOCKED`로 차단됨(negative/positive/market 3개 에이전트와 CEO가 독립적으로 재현 확인). CEO의 지난 지시("원문 URL 직접 WebFetch")는 P015(GitHub Issue) 한 건만 완전히 이행 가능했고, 나머지는 WebSearch 요약 인용 + 신뢰도 표기로 대체했다.
2. **Manager 1위(I003 Dependency Digest, 76/A)가 Market에서 B(68)로 하락**: GitHub가 자체적으로 grouped updates·cooldown 기능을 2026년 내내 개선 중이라는 플랫폼 리스크가 확인됨.
3. **Manager 최하위권(I005 헬스장 해지대행, 57/C)이 Market에서 2위(65/B)로 상승**: Rocket Money의 실제 성과보수(35~60%) 모델 사례가 확인되며, "1회성 Pain=사업성 낮음"이라는 직관이 반박됨.
4. **4개 아이디어(관리비 감사관/클레임 워치/노콜 견적/놓치지마)가 이미 존재하는 강력한 무료·공공 대안(K-APT/보험사 자체 앱/헤이딜러/정부24)과 정면 경쟁**한다는 사실이 Market 단계에서 새로 드러남 — Manager 단계에서는 포착하지 못했던 리스크.

## Top 3 기회
1. **I003 Dependency Digest** (Manager 76/A, Market 68/B) — 근거가 가장 탄탄함(유일한 원문 GitHub Issue 직접 인용). GitHub 네이티브 기능이 못 따라오는 "AI 위험도 요약"에 차별화 집중 필요.
2. **I005 머니백 짐 (헬스장 해지대행+환급추적)** (Manager 57/C, Market 65/B) — Manager와 Market 평가가 정반대로 갈린 가장 흥미로운 케이스. 성과보수 모델 검증이 다음 단계.
3. **I001 펫닥터 프라이스 / I007 가구 자산배분 대시보드** (둘 다 Manager·Market 모두 B, 66/64, 66/63) — 안정적으로 중상위권. 다만 각각 펫트라슈, Monarch/Copilot Money 등 기존 경쟁자가 존재해 명확한 차별화 지점 검증이 필요.

## Cross-Agent Insights
- Manager와 Market의 순위가 크게 엇갈린 것은 두 에이전트가 서로 다른 질문("제품이 좋은가" vs "사업이 되는가")에 답하도록 설계된 구조가 실제로 작동하고 있다는 신호다.
- "이미 존재하는 무료/공공 대안"을 찾아내는 것이 이번 회차 Market Agent의 가장 큰 기여였다 — 지난 실행(9/21)에서 CEO가 지적한 "시장 근거 확인 미흡" 문제가 개선된 구체적 증거.
- Negative Agent가 유일하게 원문(GitHub Issue)을 확보한 신호(P015)가 곧 Manager 최고점 아이디어로 이어졌다는 것은, 근거의 질이 최종 아이디어 품질에 직결된다는 것을 보여준다.

## 알림 / 이슈
- **[인프라] WebFetch가 세션 전역에서 github.com 외 거의 모든 도메인에 대해 차단됨.** User의 egress 정책 확인/조정이 필요할 수 있음 (ceo/ceo-2026-09-20.md 1절 참고).
- **[데이터 정합성] 날짜 순서 이상**: 이번 실행은 시스템이 지정한 "오늘" 2026-09-20 기준으로 수행됐으나, 저장소에는 이미 2026-09-21 날짜의 실행 기록이 먼저 존재한다. CEO는 이 순서를 임의로 정정하지 않고 사실 그대로 기록했다(ceo/ceo-2026-09-20.md 0절). User 확인 필요.
- CEO Strike 상태: 0 (User 판정 대기, 변경 없음).

## 다음 날 권장
- WebFetch egress 정책이 해제되는지 먼저 확인하고, 해제 시 negative/positive agent가 오늘 미확보한 원문 1차 인용(맘카페, 5ch, Reddit 등)을 재시도.
- I003: 개발자 대상 "AI 위험도 요약 vs GitHub 네이티브 그룹핑" 선호도 소규모 검증.
- I005: 성과보수 단가(건당 평균 회수 가능 환급액) 추가 조사.
- 날짜 순서 이상에 대한 User 확인 후, 다음 실행부터는 정정된 날짜 기준(실제 캘린더 날짜)으로 파일명을 부여.
