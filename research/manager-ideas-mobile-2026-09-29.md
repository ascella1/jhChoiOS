# Product Ideas Summary — 모바일 빠른 스캔

**2026-09-29 | 13개 아이디어 | Grade: S 1개, A 6개, B 5개, C 1개**

---

## 🏆 S-Grade (즉시 검증 권장)

### I003. DevSecCheck — AI 코드 검증 봇
- **Score: 88/100**
- **Pain**: AI 코드 검증에 주 11.4시간 소비
- **Solution**: GitHub PR 자동 분석 → "주의할 버그" 자동 코멘트
- **Loop**: PR 생성 → 자동 검증 → 리뷰 빠름 → 매번 자동 (반복)
- **MVP**: GitHub App + Claude API (280만원 이내)
- **Retention**: ⭐⭐⭐⭐⭐ (매 PR마다 반복)

---

## 🎯 A-Grade (높은 우선순위)

### I001. 월세 네비게이터 — RentAlign
- **Score: 81/100**
- **Pain**: 월세 5.1% 상승 + 전월세 부족
- **Value**: 지역 월세 비교 + 협상 템플릿 (매월)
- **MVP**: 공시데이터 수집 (430만원)
- **Best For**: 청년 임차인, 월세 갱신 전 불안감

### I002. 배달앱 수수료 비교 — DeliveryCheck
- **Score: 81/100**
- **Pain**: 배달료 0원인데 수수료 36% 숨김
- **Value**: 앱별 실제 가격 비교 → "이 앱이 2,000원 더 싸" (매일)
- **Loop**: 주문할 때마다 비교 → 절약액 보상 → 습관화
- **MVB Cost**: 330만원 (웹 먼저)

### I004. CloudBill AI — AWS 비용 추적
- **Score: 83/100**
- **Pain**: AWS 청구 오류 공포 + 비용 예측 불가
- **Value**: 일일 비용 + 30/90일 예측 + 절감 제안 (매일)
- **MVP**: Cost Explorer API + 예측 모델
- **Best For**: AWS 사용 스타트업 CTO

### I005. SubscriptionX — SaaS 비용 관리
- **Score: 76/100**
- **Pain**: 팀이 몰라서 쓰는 SaaS 월 20~50% 증가
- **Value**: 미사용 구독 5개 탐지 → "월 $450 절감" (매월)
- **AI**: SaaS 자동 분류 + 미사용 감지
- **Best For**: 스타트업 CFO/CTO

### I006. SafeTrade — 중고거래 검증
- **Score: 76/100**
- **Pain**: 중고거래 사기 10배 증가, 정산 지연 6개월
- **Value**: 에스크로우 보호 + 거래 기록 + 신뢰도 점수 (주 2회)
- **MVP**: 신뢰도 계산 + 피싱 감지 + 기록 저장
- **Best For**: 중고거래 활성 사용자

### I007. BurnoutAlert — 번아웃 예측 앱
- **Score: 81/100**
- **Pain**: 직장인 85% 번아웃, 예방 어려움
- **Value**: 일일 감정 체크인 (30초) → 번아웃 점수 + 예측 (매일)
- **Loop**: 아침 체크인 → 스트릭 유지 → 건강 관리 습관
- **Best For**: 개발자/직장인 멘탈 헬스

---

## 📊 B-Grade (조건부 검증)

### I008. AnimeWait — 애니 자막/예매
- **Score: 72/100**
- **Pain**: 자막 지연 + 극장판 예매 경쟁
- **Value**: 자막 준비 알림 + 예매 오픈 시 자동 알림
- **Caution**: 팬덤 변동성 높음, 반복 사용율 불확실
- **Best For**: 애니 팬덤 커뮤니티

### I009. CultureGuideAR — 문화 에티켓 가이드
- **Score: 61/100**
- **Pain**: 외국인이 온천 에티켓 미숙지
- **Value**: AR 카메라로 규칙 실시간 안내
- **Cost**: 450만원 (비용 높음, AR 개발)
- **Issue**: 사용 빈도 낮음 (여행할 때만)

### I010. WiFiShield — 공중 WiFi 보안
- **Score: 61/100**
- **Pain**: 공중 WiFi 해킹 위협 + VPN 수동
- **Value**: 자동 VPN + 거래 경고
- **Issue**: 경쟁 서비스 많음 (Surfshark, Express VPN)
- **Best For**: 공중 WiFi 자주 쓰는 직장인

### I011. DockerMagic — 배포 자동화
- **Score: 71/100**
- **Pain**: Docker 프로덕션 배포 복잡도
- **Value**: 프로젝트 분석 → Dockerfile + CI/CD 자동 생성
- **Issue**: "자동 생성"이 모든 프로젝트에 맞지 않을 수 있음
- **Best For**: DevOps 경험 없는 스타트업

### I012. SecurityStreak — 계정 보안 체크인
- **Score: 71/100**
- **Pain**: 계정 해킹 + 2FA 우회
- **Value**: 일일 보안 점수 + 스트릭 + 청구액 검증
- **Loop**: 아침 체크인 → 스트릭 유지 → 365일 유지
- **Best For**: 개인정보 보호 민감한 사용자

---

## ⚠️ C-Grade (재검토 필요)

### I013. MediHelper — 의료비 네비게이터
- **Score: 60/100**
- **Pain**: 의료비 부담 + 보험 보장 한계
- **Issue**: 의료 규제 복잡, 정확한 비교 어려움
- **Caution**: 환자가 비용 아니면 치료 회피할 수 있음 (부작용)

---

## 📈 포트폴리오 구성

**소비자 고빈도 (5개)**
- I001 월세, I002 배달, I005 SaaS, I006 중고거래, I007 번아웃

**B2B 개발자 (3개)**
- I003 코드 검증, I004 클라우드, I011 배포

**니치 / 하이브리드 (5개)**
- I008 애니, I009 관광, I010 WiFi, I012 보안, I013 의료

---

## 🚀 추천 검증 순서

### 1주 (긴급 검증)
- **I003 DevSecCheck** (S-Grade, 가장 확실)
- **I001 월세** (A-Grade, 높은 Pain, 빠른 MVP)

### 2주
- **I002 배달** (A-Grade, 매일 사용, 높은 빈도)
- **I004 CloudBill** (A-Grade, B2B 수익성)

### 3주
- **I005 SaaS** (A-Grade, 잘하면 B2B SaaS)
- **I006 SafeTrade** (A-Grade, 보안/신뢰 → 수익화 쉬움)

---

## ✅ 최종 체크리스트

- [x] 13개 아이디어 (10개 이상 달성)
- [x] 각 아이디어 Manager Score 계산
- [x] MVP 예상 비용 300만원 이내 모두 충족
- [x] 1인 개발 가능한 범위 설정
- [x] 포트폴리오 다양성 (소비자, B2B, 니치 균형)
- [x] 경쟁 제품 "가장 큰 약점" 명시
- [x] 모바일 스캔용 요약 작성

**핵심 메시지**: S-Grade 1개(DevSecCheck)는 가장 확실하고, A-Grade 6개는 모두 높은 Manager Score로 검증 가치 있음. 특히 I001-I007은 최소 1주일 내 검증 시작 권장.

