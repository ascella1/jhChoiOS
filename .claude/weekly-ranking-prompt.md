# jhChoiOS Weekly Ideas Ranking Prompt

이 프롬프트는 매주 일요일 아침에 자동 실행되어 지난주 최고 아이디어 순위를 생성합니다.

## 실행 시간
- **매주**: 일요일
- **시간**: 아침 08:47 (한국 시간)
- **빈도**: 매주 1회

## 실행 내용

```bash
cd /home/user/jhChoiOS

# 지난 7일 일일 report 검토
ls -1t daily-report-2026-*.md | head -7

# 각 report에서 TOP 3 아이디어 추출
# Manager Score + Market Score 계산
# 종합 순위 작성

# 결과 파일 생성
# weekly-ideas-ranking-YYYY-MM-DD.md

# 사용자에게 보고 (한국어)
# PushNotification 발송
```

## 추출 기준

### 순위 계산
- **종합 점수** = (Manager Score + Market Score) / 2
- **등급**: S (80+) / A (70-79) / B (60-69) / C (0-59)
- **동점 시**: Market Score 높은 것 우선 (시장성 중시)
- **같으면**: 최근 날짜 우선

### 결과 포맷

```markdown
# 📊 jhChoiOS 주간 아이디어 TOP 10 — 2026-09-27 주간

## 순위표

| 순위 | 아이디어 | Manager | Market | 종합 | 등급 | 상태 |
|------|---------|---------|--------|------|------|------|
| 1 | ExchangeGame | 87 | 85 | 86 | S | 즉시 개발 |
| 2 | RepoMirror | 85 | 84 | 84.5 | S | 즉시 개발 |
| 3 | DailyRepeat | 83 | 81 | 82 | S | 즉시 개발 |
...
```

## 포함 정보

### 1. TOP 3 분석 (개발 추천)
- 아이디어명
- 한 줄 설명
- 즉시 개발 이유
- MVP 예상 비용 및 시간

### 2. 주간 트렌드
- 이번주 가장 많은 Pain 유형
- 이번주 가장 많은 Positive 패턴
- 반복되는 아이디어 조합

### 3. CEO 성과 추이
- Strike 상태
- Consecutive Unsatisfactory Runs
- 이번주 Quality Gate 통과율
- SATISFACTORY 일수

### 4. 주의 필요 사항
- 점수 급락한 아이디어 분석
- 기술적 장벽이 높아진 아이디어
- 무료 경쟁이 심해진 분야

## 보고 방식

### 채팅 응답 (사용자 인터페이스)
- 순위표 (마크다운)
- TOP 3 핵심 분석
- 주간 인사이트 3가지
- 다음주 주목할 점

### 파일 저장
- 경로: `/home/user/jhChoiOS/weekly-ideas-ranking-YYYY-MM-DD.md`
- 저장소 커밋: `Weekly ideas ranking — YYYY-MM-DD`

### 알림 (PushNotification)
- 제목 (한국어): "📊 이번주 TOP 아이디어 순위"
- 본문: TOP 3 요약 + 1줄 핵심 insight
- 상태: proactive (휴대폰에도 알림)

## 기술 요구사항

### 필수 읽기
- `/home/user/jhChoiOS/daily-report-2026-09-*.md` (최근 7개)
- `/home/user/jhChoiOS/ceo/ceo-2026-09-*.md` (최근 7개)
- `/home/user/jhChoiOS/research/manager-2026-09-*.md` (최근 7개)
- `/home/user/jhChoiOS/market/2026-09-*.md` (최근 7개)

### 필수 출력
- 채팅 응답 (한국어)
- PushNotification (한국어)
- 파일 저장 + 커밋

### 예외 처리
- 파일 없으면 스킵 (에러 아님)
- 같은 아이디어 반복 → 최고 점수만 카운트
- 점수 미기록 → 해당 날짜 제외

## 자동화 설정

### 환경
- 저장소: ascella1/jhChoiOS
- 브랜치: master (또는 claude/eager-curie-0g6dg1)
- 실행 사용자: Claude (routine session)
- 언어: 한국어 (CLAUDE.md 준수)

### 스케줄
- **Cron**: `47 8 * * 0` (매주 일요일 08:47)
- **시간대**: Asia/Seoul (한국 시간)
- **Fallback**: 실패 시 다음주에 재시도
