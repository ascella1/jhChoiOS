# jhChoiOS 저장소 운영 지침

## 보고 언어

이 저장소에서 daily pipeline(negative/positive/manager/market/ceo agent) 루틴을 실행하는 세션은,
사용자에게 보내는 모든 보고를 **한국어**로 작성한다. 여기에는 다음이 포함된다:

- 실행 완료 후 사용자에게 보내는 PushNotification 요약
- 세션이 사용자에게 보내는 채팅/텍스트 응답
- 이상 상황(인프라 오류, 데이터 정합성 문제 등)을 알리는 알림 문구

단, 저장소 내부 산출물 파일(research/*.md, market/*.md, ceo/*.md, daily-report-*.md)의 언어는
각 agent 정의 파일(agents/*.md)이 이미 규정한 대로 한국어로 작성하며, 이 지침으로 바뀌지 않는다
(원래부터 한국어였음 — 이 항목은 "사용자에게 직접 보내는 보고"에 대한 지침이다).

## 파이프라인 실행 방법

daily pipeline 실행 절차는 이 저장소를 대상으로 실행되는 스케줄된 루틴의 프롬프트를 따른다
(negative → positive → manager → market → ceo 순서, agents/*.md 정의 준수, 최신 ceo/ceo-*.md의
CEO Directive 적용). 이 문서는 그 절차를 대체하지 않고, 보고 언어 등 저장소 차원의 보충 규칙만 정의한다.
