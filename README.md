# AI 트렌드 온보딩 완벽 가이드

> AI 입문자를 위한 AI 시대 생존 교본 (2026년 3월 기준)

ChatGPT 이후 3년간의 AI 혁명을 한 권으로 정리한 교육 자료입니다. 기술 원리부터 실전 활용까지, AI 시대에 필요한 핵심 지식을 담고 있습니다.

## 📖 책 구성

| 챕터 | 제목 | 핵심 내용 |
|------|------|----------|
| 프롤로그 | 왜 지금 AI를 알아야 하는가 | AI 시대 동기 부여 |
| Ch1 | 3년의 혁명 | 2022~2026 AI 타임라인, 주요 이벤트, 변화 속도 분석 |
| Ch2 | AI는 어떻게 생각하는가 | 트랜스포머, MoE, 정렬, 추론 시간 컴퓨팅, 멀티모달 |
| Ch3 | AI 모델 전쟁 | OpenAI·Anthropic·Google·Meta·DeepSeek 5강 경쟁 구도 |
| Ch4 | AI가 바꾸는 세상 | 응용 서비스, 비즈니스 임팩트, 5대 메가트렌드 |
| Ch5 | 코드 없이 코딩하기 | 바이브코딩 개념, 도구 생태계, 실전 가이드 |
| Ch6 | AI 팀을 지휘하라 | 하네스 엔지니어링, 에이전트 디자인 패턴 |
| 부록 | AI 용어 사전 | 핵심 용어 40개 정리 |

## 📥 산출물

- **소스 교육 자료**: [`AI-Education-Complete.md`](AI-Education-Complete.md) (1,886줄)
- **인터랙티브 웹**: [`docs/`](docs/) (챕터별 HTML 페이지)
- **리서치 산출물**: [`output/`](output/) (트렌드 리포트, 팩트체크 등)

## 🌐 인터랙티브 웹 페이지

`docs/` 디렉토리에 챕터별 인터랙티브 웹 페이지가 포함되어 있습니다.

| 파일 | 내용 |
|------|------|
| `index.html` | 홈 (전체 목차 및 네비게이션) |
| `ch1.html` ~ `ch6.html` | 챕터별 상세 페이지 |

## 🏗️ 제작 방식

이 교육 자료는 **Claude Code의 하네스 엔지니어링**으로 제작되었습니다.

### 에이전트 팀 구성 (8개)

| 에이전트 | 역할 | 정의 파일 |
|---------|------|----------|
| `ai-trend-analyst` | AI 트렌드 분석 및 교육 콘텐츠 설계 | `.claude/agents/ai-trend-analyst.md` |
| `ai-transformation-expert` | 기업 AI 전환 및 업무 혁신 전문가 | `.claude/agents/ai-transformation-expert.md` |
| `trend-researcher` | 최신 AI 기술/서비스 트렌드 리서치 | `.claude/agents/trend-researcher.md` |
| `content-assembler` | 교육 콘텐츠 통합 편집 | `.claude/agents/content-assembler.md` |
| `fact-checker` | 팩트체크 및 출처 검증 | `.claude/agents/fact-checker.md` |
| `book-chapter-writer` | 챕터별 집필 | `.claude/agents/book-chapter-writer.md` |
| `book-illustrator` | Gemini 이미지 생성 | `.claude/agents/book-illustrator.md` |
| `book-editor` | 통합 편집, 중복 제거, 톤 통일 | `.claude/agents/book-editor.md` |

### 스킬 구성 (7개)

| 스킬 | 역할 | 정의 파일 |
|------|------|----------|
| `ai-edu-orchestrator` | 교육 자료 제작 워크플로우 관리 | `.claude/skills/ai-edu-orchestrator/skill.md` |
| `book-production` | 책 제작 전체 프로세스 조율 | `.claude/skills/book-production/skill.md` |
| `web-research` | 체계적 웹 검색 및 정보 수집 | `.claude/skills/web-research/skill.md` |
| `tech-explainer` | 기술 개념 쉽게 풀어쓰기 | `.claude/skills/tech-explainer/skill.md` |
| `timeline-builder` | 타임라인/표 생성 | `.claude/skills/timeline-builder/skill.md` |
| `glossary-builder` | AI 용어 사전 구축 | `.claude/skills/glossary-builder/skill.md` |
| `content-formatter` | 교육 자료 포맷팅 및 스타일 적용 | `.claude/skills/content-formatter/skill.md` |

### 오케스트레이터

두 개의 오케스트레이터 스킬이 워크플로우를 조율합니다.

**`ai-edu-orchestrator`** — 교육 자료 제작:
```
Phase 1: 4개 리서치 에이전트 병렬 실행 → Phase 2: content-assembler 통합
→ Phase 3: fact-checker 검증 → Phase 4: 최종본 생성
```

**`book-production`** — 책 제작:
```
Phase 1: 준비 → Phase 2: 6개 챕터 병렬 집필 → Phase 3: 삽화 병렬 생성
→ Phase 4: 통합 편집 → Phase 5: PDF 생성
```

## 📁 프로젝트 구조

```
ai-trend-onboarding/
├── AI-Education-Complete.md    # 소스 교육 자료 (1,886줄)
├── CLAUDE.md                   # 프로젝트 지침
├── image-style.txt             # 삽화 스타일 정의
├── .claude/
│   ├── agents/                 # 에이전트 정의 (8개)
│   └── skills/                 # 스킬 정의 (7개)
├── docs/                       # 인터랙티브 웹 페이지
│   ├── index.html              # 홈 페이지
│   ├── ch1.html ~ ch6.html     # 챕터별 페이지
│   └── logo.png                # 로고 이미지
├── output/                     # 산출물
│   ├── AI-Education-Complete.md        # 최종 교육 자료
│   ├── 01-ai-trend-report.md           # AI 트렌드 리포트
│   ├── 02-trends-and-services.md       # 트렌드 및 서비스 분석
│   ├── 03-일하는 방식의 변화-AI.md      # 업무 혁신
│   ├── 04-생성형AI의 개념과 작동원리.md  # 기술 원리
│   ├── 05-AI시대-우리가 준비해야 하는 것.md # 준비 사항
│   ├── appendix-glossary.md            # 부록 용어 사전
│   └── fact-check-report.md            # 팩트체크 리포트
└── _workspace/
    └── md_to_pdf.py            # PDF 변환 스크립트
```

## 🔧 PDF 생성

Markdown에서 PDF를 생성하려면:

```bash
pip install weasyprint markdown pypdf
python3 _workspace/md_to_pdf.py
```

## 📌 기준 정보

- **기준 시점**: 2026년 3월
- **대상 독자**: AI 입문자 (회사 임직원)
- **삽화 스타일**: 손그림 doodle, 크림색 배경, 파스텔 톤
- **이미지 생성**: Google Gemini Image Generation

## ✍️ 저작자

- **황민호** (revfactory@gmail.com)

## 📜 라이선스

이 저작물은 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) 라이선스를 따릅니다.

- ✅ **출처를 밝히면** 자유롭게 공유 및 변형할 수 있습니다.
- ✅ **교육 및 연구 목적**으로 사용할 수 있습니다.
- ❌ **상업적 판매는 불가**합니다.
- 🔄 변형 저작물에도 동일한 라이선스를 적용해야 합니다.

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
