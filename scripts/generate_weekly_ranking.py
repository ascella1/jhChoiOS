#!/usr/bin/env python3
"""
jhChoiOS Weekly Ideas Ranking Generator
매주 일요일 아침 자동으로 지난주 최고 아이디어 순위를 생성합니다.
"""

import re
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

def extract_ideas_from_reports():
    """지난 7일의 daily report에서 아이디어 추출"""
    repo_root = Path(__file__).parent.parent
    ideas = {}

    # 모든 daily-report 파일 스캔
    report_files = sorted(repo_root.glob('daily-report-2026-*.md'), reverse=True)[:7]

    for report_file in report_files:
        try:
            with open(report_file, 'r', encoding='utf-8') as f:
                content = f.read()
                date_str = report_file.stem.replace('daily-report-', '')

                # Manager/Market 점수 패턴 찾기
                # "| ExchangeGame | 87 | 85 | 172 |" 형태
                pattern = r'\|\s*([^\|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'

                matches = re.finditer(pattern, content)
                for match in matches:
                    idea_name = match.group(1).strip()
                    try:
                        manager = int(match.group(2))
                        market = int(match.group(3))

                        # 같은 아이디어가 여러 번 나오면 최고 점수만 유지
                        total = (manager + market) / 2

                        if idea_name not in ideas or total > ideas[idea_name]['total']:
                            ideas[idea_name] = {
                                'manager': manager,
                                'market': market,
                                'total': total,
                                'date': date_str,
                                'grade': 'S' if total >= 80 else 'A' if total >= 70 else 'B' if total >= 60 else 'C'
                            }
                    except (ValueError, AttributeError):
                        continue

        except Exception as e:
            print(f"Error reading {report_file}: {e}")

    return ideas

def generate_ranking_report(ideas):
    """순위 리포트 생성"""
    if not ideas:
        return None

    # TOP 10 추출 및 정렬
    sorted_ideas = sorted(
        ideas.items(),
        key=lambda x: (x[1]['total'], x[1]['market']),
        reverse=True
    )[:10]

    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    report = f"""# 📊 jhChoiOS 주간 아이디어 순위

**기준 기간**: {week_start.strftime('%Y-%m-%d')} ~ {week_end.strftime('%Y-%m-%d')}
**생성일**: {today.strftime('%Y-%m-%d %H:%M:%S')}

---

## 🏆 TOP 10 아이디어

| 순위 | 아이디어 | Manager | Market | 종합 | 등급 | 최초 등장 |
|------|---------|---------|--------|------|------|----------|
"""

    for idx, (name, scores) in enumerate(sorted_ideas, 1):
        report += f"| {idx} | {name} | {scores['manager']} | {scores['market']} | {scores['total']:.1f} | **{scores['grade']}** | {scores['date']} |\n"

    # TOP 3 상세 분석
    report += "\n---\n\n## 🎯 TOP 3 즉시 개발 추천\n\n"

    top_3_details = {
        'ExchangeGame': {
            'summary': 'Etsy/Shopify 판매자 환율 손실 자동화 + 게임화',
            'reason': '월 손실액 5~20만원 > Pro 월 4,990원 (명확한 ROI)',
            'timeline': '3주',
            'budget': '200~250만원'
        },
        'RepoMirror': {
            'summary': '프리랜서 정산 플랫폼 통합',
            'reason': '프리랜서 20~30% 멀티 플랫폼 사용 (시장 검증)',
            'timeline': '4주',
            'budget': '250~300만원'
        },
        'DailyRepeat': {
            'summary': '5일 초단기 챌린지',
            'reason': '챌린저스 200만 사용자의 미충족 니즈',
            'timeline': '2주',
            'budget': '200~250만원'
        }
    }

    for idx, (name, scores) in enumerate(sorted_ideas[:3], 1):
        if name in top_3_details:
            detail = top_3_details[name]
            report += f"""
### {idx}. {name}
- **설명**: {detail['summary']}
- **이유**: {detail['reason']}
- **개발**: {detail['timeline']} / {detail['budget']}
- **점수**: Manager {scores['manager']} + Market {scores['market']} = {scores['total']:.1f}점
"""

    # 주간 트렌드
    report += "\n---\n\n## 📈 주간 트렌드 분석\n\n"

    pain_types = defaultdict(int)
    positive_types = defaultdict(int)

    # Pain 유형 분류 (간단한 버전)
    pain_keywords = {
        '자동화': ['환율', '정산', '영수증', '공제', '가격'],
        '커뮤니티': ['챌린지', '아파트', '계약'],
        '추적': ['기한', '버전', '티켓'],
    }

    for idea_name in [name for name, _ in sorted_ideas[:10]]:
        for ptype, keywords in pain_keywords.items():
            if any(kw.lower() in idea_name.lower() for kw in keywords):
                pain_types[ptype] += 1

    report += "### 주요 Pain 유형\n"
    for ptype, count in sorted(pain_types.items(), key=lambda x: x[1], reverse=True):
        report += f"- **{ptype}**: {count}개 아이디어\n"

    report += "\n### Positive 패턴\n"
    report += "- **강박+스트릭**: 매일 반복 강제 (DailyRepeat, GitHub 스트릭)\n"
    report += "- **경쟁+리더보드**: 순위 경쟁으로 참여 유도 (ExchangeGame, AptCheck)\n"
    report += "- **금전적 리스크**: 돈 잃을까봐 진지함 (챌린지, 투자)\n"

    # 다음주 주목
    report += "\n---\n\n## 👀 다음주 주목할 점\n\n"
    report += "1. **ExchangeGame 시장 검증**: Etsy 판매자 50명 인터뷰 예정\n"
    report += "2. **RepoMirror API 협력**: 크몽/당신의서재 접촉 상황\n"
    report += "3. **DailyRepeat 베타**: SNS 모집 및 성공률 측정\n"

    return report

def save_report(report):
    """리포트를 파일로 저장"""
    if not report:
        print("No report to save")
        return None

    repo_root = Path(__file__).parent.parent
    today = datetime.now()
    filename = f"weekly-ideas-ranking-{today.strftime('%Y-%m-%d')}.md"
    filepath = repo_root / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Report saved: {filepath}")
    return filepath

if __name__ == '__main__':
    print("🔍 Extracting ideas from reports...")
    ideas = extract_ideas_from_reports()

    if not ideas:
        print("⚠️ No ideas found in reports")
        exit(1)

    print(f"✅ Found {len(ideas)} unique ideas")

    print("📊 Generating ranking report...")
    report = generate_ranking_report(ideas)

    if report:
        filepath = save_report(report)
        print(f"✅ Weekly ranking generated successfully")
        print(f"\nTOP 5 Ideas:")
        sorted_ideas = sorted(
            ideas.items(),
            key=lambda x: (x[1]['total'], x[1]['market']),
            reverse=True
        )[:5]
        for idx, (name, scores) in enumerate(sorted_ideas, 1):
            print(f"{idx}. {name} ({scores['total']:.1f} points)")
    else:
        print("❌ Failed to generate report")
        exit(1)
