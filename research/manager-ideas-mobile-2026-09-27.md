# Manager Ideas — Mobile Format (2026-09-27)

## 🎯 빠른 요약

**Negative + Positive 40개 신호 분석**
- 12개 제품 아이디어 도출
- S급(85점+): 3개
- A급(70~84점): 5개
- 포트폴리오 다양성: ✅ 소비자 고빈도 제품 포함

---

## 🏆 S급 3개 (개발 우선순위 높음)

### 1️⃣ RepoMirror (85점) — 프리랜서 다중 플랫폼 정산 통합
**Problem**: 크몽 + 당신의서재 + 오늘의집에서 받는 정산액을 엑셀로 수작업 정리
**Solution**: 자동 통합 + 세금 자동 계산
**Monetization**: Pro(월 4,990원) + B2B
**MVP 난도**: ⭐⭐⭐ (API 협력 필요)

---

### 2️⃣ ExchangeGame (87점) — 환율 변동 게임화
**Problem**: Etsy/Shopify 판매자가 환율 변동 때 수동으로 가격 조정
**Solution**: 환율이 올랐을 때 "가격 올릴까?" 제안 + 리더보드 경쟁
**Monetization**: Pro(월 4,990원) + Shopify 앱 스토어
**MVP 난도**: ⭐⭐ (구현 간단)

---

### 3️⃣ DailyRepeat (83점) — 5일 초단기 챌린지
**Problem**: 습관 형성이 어려움
**Solution**: 1~5일 초단기 챌린지 + 참가비 환급(성공 시)
**Monetization**: Pro(월 2,990원) + 기부 모델
**MVP 난도**: ⭐⭐ (구현 간단)

---

## 🥈 A급 5개 (차별화 명확)

| 제품 | Score | Pain | Positive | 핵심 기능 |
|------|-------|------|----------|---------|
| 005 AptCheck | 83 | 관리비 오류 이의 | 커뮤니티 연대감 | 오류 자동 감지 + 공동 소송 |
| 001 MoneyStorm | 82 | 프리랜서 세금 신고 | 세금 챌린지 보상 | 플랫폼 통합 + AI 세금 계산 |
| 012 LoyalLoop | 82 | 소상공인 고객 이탈 | 반복 구매 게임화 | POS 연동 + Loyalty 자동화 |
| 008 HealthStreak | 74 | 없음 (Positive만) | 회복 점수 + 스트릭 | Whoop 데이터 + GitHub 히트맵 |
| 010 HealthPass | 75 | 없음 (Positive만) | 건강 데이터 통합 | Whoop + Strava 통합 |

---

## 📊 카테고리별 분포

### B2C 高頻度 (매일/매주)
- 🏃 DailyRepeat (습관)
- 📈 HealthStreak (회복 점수)
- 🏥 HealthPass (건강 데이터)
- 🍜 LoyalLoop (POS 연동)

### B2C 中頻度 (월 2~4회)
- 📧 RepoMirror (정산)
- 💰 MoneyStorm (세금)
- 📝 ContractVault (계약)
- 🏢 AptCheck (관리비)
- 💱 ExchangeGame (환율)

### B2C 低頻度 (월 1회 이하)
- 🏠 LeaseGuard (전세사기 검사)
- 📦 SegmentKeeper (택배 기한)
- 💻 ProtoZone (프롬프트 라이브러리)

---

## 🔥 즉시 개발 추천 (MVP 30만원 이내)

### 1. ExchangeGame (87점)
**Why**: 
- Pain 명확 (실제 환율 손실 월 2~5%)
- MVP 간단 (환율 API + 추천 로직)
- 수익화 명확 (Shopify 앱 스토어)

**First Week**:
- [ ] OpenExchangeRates API 연동
- [ ] Shopify 테스트 스토어 연결
- [ ] "가격 올릴까?" 추천 로직

**验证**: Etsy/Shopify 판매자 5명 인터뷰

---

### 2. RepoMirror (85점)
**Why**:
- Pain 심각 (월 1시간 + 세금 미신고 위험)
- 수익화 최고 (Pro + B2B)
- 시장 검증됨 (프리랜서 100만명+)

**First Week**:
- [ ] 크몽 API 신청
- [ ] 당신의서재 API 신청
- [ ] 엑셀 임포트 기능

**验证**: 프리랜서 10명 베타 → 3명 이상 Pro 구독 의향

---

## ⚠️ 거절 아이디어

### SegmentKeeper (56점, C급)
- Pain 심각도 낮음 (월 1~2회만 발생)
- Retention 약함 (택배는 자동 추적 앱이 이미 있음)
- 차별화 어려움 (알림만으로는 부족)

**→ 개발 보류**

---

## 🧠 핵심 검증 가설

### 가설 1: "자동화 도구의 Pro 전환율은 30% 이상인가?"
**테스트**: RepoMirror/MoneyStorm 베타 100명 → 30명 이상 구독?
**기간**: 2주

### 가설 2: "강박 스트릭 게임화는 일반화될 수 있나?"
**테스트**: DailyRepeat 1,000명 → 3개월 retention 60% 이상?
**기간**: 3개월

### 가설 3: "AI 자동화 + 보상이 행동을 정말 바꾸나?"
**테스트**: ExchangeGame 판매자 10명 → 실제 수익 2~5% 증가 확인?
**기간**: 1개월

---

## 📈 예상 Timeline

### Week 1-2: MVP 개발
- ExchangeGame: 환율 추적 + 가격 제안
- RepoMirror: API 연동 + 정산 자동 합산

### Week 3-4: 베타 테스트
- ExchangeGame: Shopify 판매자 10명
- RepoMirror: 프리랜서 10명

### Month 2: 검증 & Iterate
- 사용자 피드백 → Product-Market Fit 확인
- 경쟁사 분석 → 차별화 강화

### Month 3: 공식 런칭
- 프로 구독 오픈
- B2B 제휴 협상 시작

---

## 💡 추가 Insights

### Pain & Positive의 연결
**가장 강한 결합**: 
- Pain(P015 환율) + Positive(S003 시세) = ExchangeGame 
- Pain(P003 정산) + Positive(S005 자동누적) = RepoMirror

**약한 결합**:
- Pain(P004 전세사기) → 일회성이라 Positive(반복성) 연결 불가
- Pain(P002 관리비) → 해결책이 B2B 필요

### "Positive Signal만으로 도출된 제품" 트렌드
- 008/010 (운동 게임화)
- 011 (프롬프트 협업)
→ AI/웨어러블 시대에 "기록 + 공유 + 경쟁"만으로도 제품 가치 충분

---

## 🎯 Manager 최종 평가

**전략 성공도**: 8/10
- ✅ 5가지 동기 패턴 분명하게 도출
- ✅ Pain + Positive 결합 사례 다수
- ⚠️ B2B 어려움 (API 협력, 법적 책임)
- ⚠️ 생애이벤트 pain은 비즈니스화 어려움

**포트폴리오 건강도**: 9/10
- ✅ 소비자 고빈도 제품 4개 (33%)
- ✅ 수익화 모델 다양 (구독/거래수수료/제휴)
- ✅ S/A/B/C급 균형 잡음
- ⚠️ C급 1개(택배)는 거절 추천

**실행 난도**: 7/10
- ✅ MVP는 대부분 가능 (1인 개발)
- ⚠️ 스케일링 시 API 협력 필수
- ⚠️ 법적 책임(세금, 계약) 네비게이션 필요

---

**작성일**: 2026-09-27  
**분석 대상**: Negative 20개 + Positive 20개 = 40개 신호  
**산출 아이디어**: 12개 (S: 3개, A: 5개, B: 3개, C: 1개)  

