#!/usr/bin/env python3
"""
jhChoiOS Weekly Ideas Ranking Generator
매주 일요일 아침 자동으로 지난주 최고 아이디어 순위를 생성합니다.
"""

import re
from pathlib import Path
from datetime import datetime, timedelta

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

                # 패턴: "ExchangeGame(87), RepoMirror(85)"
                # 또는 "Manager 87, Market 85"
                pattern = r'([A-Za-z0-9]+)\s*\((\d+)\)'
                matches = re.finditer(pattern, content)

                temp_ideas = {}
                for match in matches:
                    name = match.group(1)
                    score = int(match.group(2))

                    if name not in temp_ideas:
                        temp_ideas[name] = []
                    temp_ideas[name].append(score)

                # Manager/Market 패턴도 찾기
                mgmt_pattern = r'Manager\s+(\d+)[^0-9]*?Market\s+(\d+)'
                mgmt_matches = re.finditer(mgmt_pattern, content)

                for match in mgmt_matches:
                    manager_score = int(match.group(1))
                    market_score = int(match.group(2))

                    # 근처의 아이디어 이름 찾기
                    start_pos = max(0, match.start() - 200)
                    before_text = content[start_pos:match.start()]

                    # 마지막으로 나온 대문자 단어를 아이디어명으로 추정
                    name_match = re.findall(r'([A-Z][a-zA-Z0-9]*)', before_text)
                    if name_match:
                        idea_name = name_match[-1]
                        total = (manager_score + market_score) / 2

                        if idea_name not in ideas or total > ideas[idea_name]['total']:
                            ideas[idea_name] = {
                                'manager': manager_score,
                                'market': market_score,
                                'total': total,
                                'date': date_str,
                                'grade': 'S' if total >= 80 else 'A' if total >= 70 else 'B' if total >= 60 else 'C'
                            }

        except Exception as e:
            print(f"⚠️ Error reading {report_file}: {e}")

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

| 순위 | 아이디어 | Manager | Market | 종합 | 등급 |
|------|---------|---------|--------|------|------|
"""

    for idx, (name, scores) in enumerate(sorted_ideas, 1):
        report += f"| {idx} | {name} | {scores['manager']} | {scores['market']} | {scores['total']:.1f} | **{scores['grade']}** |\n"

    # TOP 3 상세 분석
    report += "\n---\n\n## 🎯 TOP 3 즉시 개발 추천\n\n"

    for idx, (name, scores) in enumerate(sorted_ideas[:3], 1):
        report += f"### {idx}. {name}\n"
        report += f"- **Manager**: {scores['manager']}/100\n"
        report += f"- **Market**: {scores['market']}/100\n"
        report += f"- **종합**: {scores['total']:.1f}점\n"
        report += f"- **등급**: **{scores['grade']}**\n"
        report += f"- **최초 등장**: {scores['date']}\n\n"

    # 주간 트렌드
    report += "---\n\n## 📈 주간 트렌드\n\n"
    report += f"- **분석 대상**: TOP 10 아이디어\n"
    report += f"- **평균 Manager 점수**: {sum(s['manager'] for _, s in sorted_ideas) / len(sorted_ideas):.1f}/100\n"
    report += f"- **평균 Market 점수**: {sum(s['market'] for _, s in sorted_ideas) / len(sorted_ideas):.1f}/100\n"
    report += f"- **S 등급 아이디어**: {sum(1 for _, s in sorted_ideas if s['grade'] == 'S')}개\n"
    report += f"- **A 등급 아이디어**: {sum(1 for _, s in sorted_ideas if s['grade'] == 'A')}개\n"

    return report

def save_report(report):
    """리포트를 파일로 저장"""
    if not report:
        print("❌ No report to save")
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
        print(f"✅ Weekly ranking generated successfully\n")
        print("📋 TOP 5 Ideas:")
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
