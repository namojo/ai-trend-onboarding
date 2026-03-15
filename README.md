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

## 📥 최종 산출물

- **PDF**: [`AI-트렌드-온보딩-완벽가이드.pdf`](AI-트렌드-온보딩-완벽가이드.pdf) (72페이지)
- **Markdown 원본**: [`_workspace/book-complete.md`](_workspace/book-complete.md)
- **삽화**: [`output/images/`](output/images/) (14개, 손그림 doodle 스타일)

## 🏗️ 제작 방식

이 책은 **Claude Code의 하네스 엔지니어링**으로 제작되었습니다.

### 에이전트 팀 구성

```
AI-Education-Complete.md (소스 자료)
    │
    ├→ [ch1-writer] ~ [ch6-writer]     6개 챕터 병렬 집필
    ├→ [ch1-illustrator] ~ [ch6-illustrator]  삽화 병렬 생성
    ├→ [book-editor]                    통합 편집
    └→ [pdf converter]                  PDF 변환
```

| 에이전트 | 역할 | 정의 파일 |
|---------|------|----------|
| `book-chapter-writer` | 챕터별 집필 | `.claude/agents/book-chapter-writer.md` |
| `book-illustrator` | Gemini 이미지 생성 | `.claude/agents/book-illustrator.md` |
| `book-editor` | 통합 편집, 중복 제거, 톤 통일 | `.claude/agents/book-editor.md` |

### 오케스트레이터

[`book-production`](.claude/skills/book-production/skill.md) 스킬이 전체 워크플로우를 조율합니다.

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
│   ├── agents/                 # 에이전트 정의 (9개)
│   └── skills/                 # 스킬 정의 (7개)
├── _workspace/                 # 중간 산출물
│   ├── ch1.md ~ ch6.md         # 개별 챕터
│   ├── book-complete.md        # 통합 편집본
│   └── md_to_pdf.py            # PDF 변환 스크립트
└── output/
    ├── AI-트렌드-온보딩-완벽가이드.pdf  # 최종 PDF
    └── images/                 # 삽화 이미지 (14개)
```

## 🔧 PDF 재생성

Markdown을 수정한 후 PDF를 다시 생성하려면:

```bash
pip install weasyprint markdown pypdf
python3 _workspace/md_to_pdf.py
```

## 📌 기준 정보

- **기준 시점**: 2026년 3월
- **대상 독자**: AI 입문자
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
