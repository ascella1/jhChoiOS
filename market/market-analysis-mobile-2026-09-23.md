# 💼 Market Analysis - 2026-09-23 (Mobile)

## 🎯 Executive Summary

| Idea | Market Score | Grade | Viability | Risk |
|---|---|---|---|---|
| SellerSentry | 69/100 | B | ⭐⭐⭐⭐ | 🟡 Medium |
| ClientRadar | 63/100 | B | ⭐⭐⭐⭐ | 🔴 High |
| MarginPulse | 55/100 | C | ⭐⭐⭐ | 🔴 High |
| VisitVoice | 54/100 | C | ⭐⭐⭐ | 🔴 High |
| PayClear | 54/100 | C | ⭐⭐⭐ | 🟡 Medium |
| ClaimCheck | 52/100 | C | ⭐⭐⭐ | 🔴 High |
| QuarterEase | 48/100 | C | ⭐⭐ | 🔴 High |
| ShiftSOS | 46/100 | C | ⭐⭐ | 🔴 High |
| ReplyBrief | 46/100 | C | ⭐⭐ | 🔴 High |
| PetLaunch Kit | 42/100 | C | ⭐⭐ | 🟡 Medium |
| VoicePrint Watch | 33/100 | C | ⭐ | 🔴 High |
| HandoffPass | 28/100 | C | ⭐ | 🔴 High |

---

## 💡 Idea 010: SellerSentry
**Market Score: 69/100 | Grade: B**

### 📊 Market Signals

**Demand:** ✅ Confirmed
- Evidence: 아마존 셀러 매출 최대 75% 손실 사례 다수, 커뮤니티 내 반복 확인

**Customer:** Amazon 자체 브랜드 소규모 셀러
- Willingness to Pay: 경쟁사 Helium10이 월 $99~359에 유사기능 판매 중 → 고가 지불 관행 확인(단, WebFetch 미검증)

**Market Size:**
- 추정: Amazon FBA 자체 브랜드 셀러 전세계 다수
- Confidence: Medium

### 💰 Financial Snapshot

| 항목 | 평가 |
|---|---|
| **수익 모델** | Subscription |
| **가격대** | $42 - $70/월(5.9만원~) |
| **초기 10명 확보** | Amazon Seller 포럼·서브레딧·FB그룹 직접 접근 |
| **MVP 비용** | ₩230만 |
| **수익화 시간** | 3~6개월(API 승인 대기 포함) |

### ⚠️ Risk Assessment

🔴 **Critical Risk**: 셀러 계정 데이터 접근 권한을 제3자에 부여하는 데 대한 신뢰/프라이버시 저항
🟡 **Medium Risk**: Helium10·SellerSonar 등 기존 종합 툴과 기능 중복
🟢 **Low Risk**: Amazon SP-API 승인만 나면 기술 구현 자체는 안정적

### 🎯 Go/No-Go Decision Factors

✅ **Pro:**
- 12개 중 시장 규모·수요·수익모델 점수 모두 최상위권
- 확장성(타 마켓플레이스 이식 가능) 12개 중 최고

❌ **Con:**
- 계정 연동 동의라는 핵심 가설이 미검증
- Amazon API 접근 승인이라는 게이트키핑 리스크

---

## 💡 Idea 001: ClientRadar
**Market Score: 63/100 | Grade: B**

### 📊 Market Signals

**Demand:** ✅ Confirmed
- Evidence: 클라이언트 잠적·Net 30/60/90 대금지연은 Freelancers Union 등에서 반복 확인되는 실재 Pain

**Customer:** Upwork·Fiverr 프리랜서, 미국 건설 하청 컨트랙터
- Willingness to Pay: 거의 동일 컨셉의 Blacklisted Client가 "3회 무료+$9 평생 1회 결제" — 구독보다 1회성 저가 선호 신호

**Market Size:**
- 추정: 글로벌 프리랜서 플랫폼 이용자 수백만 (TAM), SAM/SOM은 니치 커뮤니티 단위로 축소
- Confidence: Medium

### 💰 Financial Snapshot

| 항목 | 평가 |
|---|---|
| **수익 모델** | Freemium + Subscription + B2B API |
| **가격대** | $14(월 1.9만원) / B2B $70~(월 9.9만원) |
| **초기 10명 확보** | 특정 Upwork 서브카테고리·Discord 니치 커뮤니티 |
| **MVP 비용** | ₩250만 |
| **수익화 시간** | 6개월+ (콜드스타트 밀도 확보 필요) |

### ⚠️ Risk Assessment

🔴 **Critical Risk**: 거의 동일한 경쟁자(Blacklisted Client)가 이미 운영 중 — 차별화 실패 시 무의미
🟡 **Medium Risk**: 명예훼손·허위제보로 인한 법적·운영 리스크
🟢 **Low Risk**: 기술 구현 자체는 1인 개발로 무난

### 🎯 Go/No-Go Decision Factors

✅ **Pro:**
- Pain 강도·시장 규모는 12개 중 최상위권
- 콜드스타트 해법(제보 게이트+시드 데이터)이 설계에 내장됨

❌ **Con:**
- 이미 유사 서비스가 존재해 "왜 옮겨야 하는가"에 대한 답이 필요
- 구독형 가격 모델이 확인된 시장 관행(1회성 저가)과 어긋날 위험

---

## 💡 Idea 005: MarginPulse
**Market Score: 55/100 | Grade: C**

### 📊 Market Signals

**Demand:** ✅ Confirmed
- Evidence: 일본 음식점 오너의 원가상승 대응 가격결정 마비, note 등 직접 발언으로 확인

**Customer:** 일본 개인·소규모 음식점 오너
- Willingness to Pay: 무료 경쟁 도구가 다수 존재해 낮음(월 9,900엔 제안가 대비 미확인)

**Market Size:**
- 추정: 일본 소규모 음식점 다수, 단 무료 도구 밀도가 높아 유료 전환 SOM은 작음
- Confidence: Low

### 💰 Financial Snapshot

| 항목 | 평가 |
|---|---|
| **수익 모델** | Subscription |
| **가격대** | ¥9,900/월 |
| **초기 10명 확보** | 일본 음식점 오너 note·SNS 커뮤니티 |
| **MVP 비용** | ₩150만 |
| **수익화 시간** | 불확실(무료 대안과 경쟁 필요) |

### ⚠️ Risk Assessment

🔴 **Critical Risk**: 핵심 계산 기능이 이미 다수의 무료 웹 도구·상공회의소 도구로 존재
🟡 **Medium Risk**: 차별화 지점(크라우드소싱 벤치마크)의 콜드스타트 미해결
🟢 **Low Risk**: 기술 구현 자체는 단순

### 🎯 Go/No-Go Decision Factors

✅ **Pro:**
- 원자재 가격 인상이라는 지속적 시장 타이밍 존재
- 계산기를 넘어선 "동종업계 벤치마크"라는 잠재적 차별화

❌ **Con:**
- 무료 대안(계산기·상공회의소 도구·note 콘텐츠)이 이미 풍부
- 벤치마크 데이터 기여 유인이 무료 도구 대비 약함

---

## 📈 Top Opportunities

### 🥇 Highest Viability
**SellerSentry** (Score: 69/100)
- Key: 매출 최대 75% 손실이라는 고강도 Pain에, 이미 확인된 고가 지불 관행(Helium10 $99~359/월)까지 더해져 12개 중 가장 안정적인 사업성 신호
- TAM: 글로벌 Amazon FBA 자체브랜드 셀러
- GTM: Amazon Seller 포럼·서브레딧에서 피해 셀러 직접 타겟팅 후 API 연동 신뢰 확보 순서로 진입

---

## ⚡ Quick Verdicts

**Immediate Action:**
- SellerSentry: Amazon SP-API 접근 승인 여부부터 먼저 확인 필요 — 이게 막히면 MVP 자체가 성립 안 함

**Further Research Needed:**
- ClientRadar: Blacklisted Client 대비 실질적 차별화 지점(엔티티 퍼지매칭, 배지 시스템)이 실사용자에게 전환 유인이 되는지 소규모 A/B 검증

**Not Recommended:**
- HandoffPass: 핵심 산출물(동의서)이 이미 변호사 감수 무료 템플릿으로 존재하고 1회성 매출 구조라 사업성 자체가 성립하기 어려움
- VoicePrint Watch: 거의 동일한 무료 경쟁자(Loti AI)가 이미 운영 중이며 시장 규모도 매우 작음

---

## 📊 Market Heat Map

**Hot (Score 75+, Grade A):** 0개
**Warm (Score 60-74, Grade B):** 2개
**Cold (Score <60, Grade C):** 10개

가장 큰 시장 기회: SellerSentry — Amazon 셀러 방어 도구, 경쟁사가 고가로 검증한 지불 관행이 존재
가장 높은 진입 장벽: HandoffPass — 핵심 산출물이 이미 무료 템플릿으로 존재 + 1회성 매출 구조 + 법적 리스크
