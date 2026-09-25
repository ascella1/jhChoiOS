# Market Analysis Mobile Summary — 2026-09-25

빠른 검토용 Executive Summary (모바일/한눈에 보기)

---

## 🎯 Top 3: 즉시 추진 가능

### 1️⃣ ListingLifespan (공인중개사 채팅 통합 + AI 자동 답변)
**Market Score: 81 / 100 (A)**

| 평가 항목 | 결과 |
|---|---|
| **Pain** | 🔴 극도로 심각 (응답 누락 = 거래 손실) |
| **시장 규모** | 5만 중개사, 연 250억원 |
| **고객 지불 의사** | 🟢 높음 (직접 수익과 연결) |
| **경쟁** | 거의 없음 (기존 CRM은 고가) |
| **수익 모델** | 명확 (구독 + B2B) |
| **MVP 비용** | 650만원 (초기 대비 2.2배) |
| **위험** | 크롤링 정책, 플랫폼 변경 |

**Action:**
- 2~3주 검증 (중개사 커뮤니티 50명 설문)
- 당근·직방 API 정책 사전 확인
- 첫 MVP: 직방·당근만 통합 (2개)

---

### 2️⃣ MicroSupply (B2B 거래자 신용 + 미수금 추적)
**Market Score: 79 / 100 (A-)**

| 평가 항목 | 결과 |
|---|---|
| **Pain** | 🟡 명확 (현금 흐름 관리) |
| **시장 규모** | 5만 제조업, 연 500억원 |
| **고객 지불 의사** | 🟡 중상 (검증 필요) |
| **경쟁** | 국제 솔루션 있으나 한국 약함 |
| **수익 모델** | 다층 구조 (구독 + B2B + 수수료) |
| **MVP 비용** | 650만원 |
| **위험** | 프라이버시, 초기 데이터 부족 |

**Action:**
- 3~4주 검증 (제조업 협회 설문)
- 신용 점수 공개 법적 검토
- CSV 수동 입력으로 MVP 시작

---

### 3️⃣ AllBook (다중플랫폼 예약 통합 + 포인트)
**Market Score: 77 / 100 (B+)**

| 평가 항목 | 결과 |
|---|---|
| **Pain** | 🟢 명확 + 고빈도 |
| **시장 규모** | 20만명, 연 600억원 |
| **고객 지불 의사** | 🟢 높음 |
| **경쟁** | 거의 없음 |
| **수익 모델** | 명확 (구독 + 환금 수수료 + B2B) |
| **MVP 비용** | 850만원 (초기 대비 2.8배) |
| **위험** | 크롤링 차단 (높음), 플랫폼 기능 추가 |

**Action:**
- **사전 검증 필수:** 당근·숨고 API 정책
- 2주 설문 (방문미용사 50명)
- 위험 높음 → 사후 보험 전략 필요

---

## 📊 점수 분포 (10개 아이디어)

```
80+ ████░░░░░░ A    (1개) — ListingLifespan
75+ ██████░░░░ A-   (2개) — MicroSupply, AllBook
70+ ████████░░ B+   (3개) — AsyncStandup, ShopReverse, RetentionRx
65+ ██████████ B-   (2개) — GigInsight, LocalFinder
60+ █████░░░░░ C+   (2개) — SalaryTransparency, MedicalInventory
평균: 73.4점
```

---

## 🔴 주의: 낮은 우선순위 (점수 <70)

| 아이디어 | 점수 | 주된 문제 |
|---|---:|---|
| **GigInsight** | 70 | Toggl, Harvest 경쟁 포화 |
| **LocalFinder** | 68 | 광고 수익 불명확 (위험) |
| **SalaryTransparency** | 65 | 유료 전환 낮음 (무료 커뮤니티) |
| **MedicalInventory** | 64 | TAM 작음, 의료 법적 리스크 |

---

## 💡 실행 전략 추천

### Phase 1 (1개월): 최우선 검증
- **ListingLifespan:** 중개사 설문 + API 정책 확인
- **MicroSupply:** 제조업 협회 설문 + 법적 검토
- → 2개 중 1개 선택하고 MVP 시작

### Phase 2 (2~3개월): AllBook 병행 검증
- ListingLifespan 또는 MicroSupply MVP 구축 중
- AllBook API 정책 최종 확인 후 병행 진행 여부 판단

### Phase 3 (4~6개월): 추가 아이디어 평가
- AsyncStandup, ShopReverse, RetentionRx 중 차별화 가능 아이디어 선택

---

## 🚀 최대 수익 잠재력 (연간)

| 순위 | 아이디어 | TAM | 수익 모델 | 추정 연수익 (Year 2-3) |
|---|---|---:|---|---:|
| 1 | ListingLifespan | 250억원 | 구독 + B2B | 50~100억원 |
| 2 | AllBook | 600억원 | 구독 + 환금 + B2B | 80~150억원 |
| 3 | MicroSupply | 500억원 | 구독 + B2B + 수수료 | 60~120억원 |
| 4 | RetentionRx | 500억원 | 구독 + 성과급 | 50~100억원 |
| 5 | AsyncStandup | 500억원 | 구독 + B2B | 40~80억원 |

**주의:** 추정치이며 실제 시장 점유율은 5~15% 수준으로 매우 보수적

---

## ⚠️ 공통 위험 요소

1. **초기 300만원 기준 MVP 비용 초과**
   - 모든 아이디어 650만원~850만원 (2배~2.8배)
   - 초기 자금조달 또는 단계적 개발 필요

2. **플랫폼 정책 리스크** (AllBook, ListingLifespan)
   - 당근·숨고·직방 크롤링 금지 가능성
   - API 공식 지원 여부 확인 필수

3. **경쟁 심화**
   - AsyncStandup: Geekbot, Standuply 등 선발주자
   - ShopReverse: Loop Returns, Narvar 등 경쟁
   - GigInsight: Toggl, Harvest 포화

4. **유료 전환율 미검증**
   - SalaryTransparency: 무료 커뮤니티 강함
   - LocalFinder: 광고 기반 수익 불명확

---

## ✅ 신뢰도 높은 검증 기준

### Manager Score vs Market Score 차이로 본 신뢰도

| 큰 차이 | 의미 |
|---|---|
| **Manager 82 → Market 77** (AllBook) | 제품은 좋지만 시장·경쟁 리스크 있음 |
| **Manager 80 → Market 81** (ListingLifespan) | 제품과 시장 모두 우수 ✓ |
| **Manager 76 → Market 79** (MicroSupply) | 시장 평가가 더 높음 (실제 수요 존재) |
| **Manager 75 → Market 75** (ShopReverse) | 균형잡힌 평가 |
| **Manager 72 → Market 65** (SalaryTransparency) | 제품 평가는 높으나 시장 수익성 낮음 |

---

## 🎯 최종 추천 (순위)

### 실행 순서
1. **ListingLifespan** (81점) → 즉시 시작
2. **MicroSupply** (79점) → 2주 후 병행
3. **AllBook** (77점) → API 정책 확인 후 결정

### 스킵 추천
- **GigInsight, SalaryTransparency:** 경쟁 포화 + 유료 전환 낮음
- **LocalFinder:** 광고 수익 모델 불확실
- **MedicalInventory:** TAM 너무 작음

---

## 📋 1인 개발자 기준 MVP 구현 가능성

| 아이디어 | 가능성 | 소요 시간 | 주의사항 |
|---|---|---:|---|
| ListingLifespan | 🟡 중간 | 3~6개월 | 크롤링 유지 필요 |
| MicroSupply | 🟢 높음 | 2~3개월 | CSV 입력 단계로 시작 |
| AllBook | 🟡 중간 | 3~6개월 | 크롤링 차단 위험 |
| AsyncStandup | 🟢 높음 | 2~3개월 | Claude API 비용 관리 필수 |
| RetentionRx | 🟢 높음 | 2~3개월 | 신용카드 자동 수집은 나중 |
| ShopReverse | 🔴 어려움 | 4~6개월 | 라이브 스트림 인프라 필요 |

---

Generated: 2026-09-25
Market Analyst: Claude Haiku 4.5
Based on: Actual market research (WebSearch)
