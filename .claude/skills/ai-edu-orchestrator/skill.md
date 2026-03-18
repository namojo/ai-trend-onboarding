---
name: ai-edu-orchestrator
description: "AI 교육 자료 제작 오케스트레이터. 전문 에이전트 팀을 조율하여 회사의 임직원 대상 AI 교육 자료를 체계적으로 제작. '/ai-edu', '교육 자료 만들어줘', 'AI 교육' 요청 시 사용."
---

# AI Education Orchestrator — AI 교육 자료 제작 총괄

회사의 임직원 대상 AI 교육 자료를 6명의 전문 에이전트 팀이 협력하여 제작하는 오케스트레이터 스킬.

## 에이전트 팀 구성

| 에이전트 | 역할 | 담당 산출물 | 실행 순서 |
|---------|------|-----------|----------|
| ai-trend-analyst | AI 트랜드 연구 | `output/01-ai-trend-report.md` | Phase 1 (병렬) |
| ai-transformation-expert | 모델 진화 분석 | `output/03-일하는 방식의 변화-AI.md`, `output/04-생성형AI의 개념과 작동원리.md`, `output/05-AI시대-우리가 준비해야 하는 것.md` | Phase 1 (병렬) |
| trend-researcher | 최신 트렌드 리서치 | `output/02-trends-and-services.md` | Phase 1 (병렬) |
| content-assembler | 통합 편집 | `output/AI-Education-Complete.md` | Phase 2 (순차) |
| fact-checker | 팩트체크 | `output/fact-check-report.md` | Phase 3 (순차) |

## 실행 워크플로우

### Phase 1: 병렬 리서치 & 집필 (팬아웃)
3개 전문 에이전트를 **동시에** 실행하여 각 챕터를 독립 집필.

```
┌─── ai-trend-analyst ──────→ 01_ai_trend_report.md
│
├─── trend-researcher ─────→ 02-trends-and-services.md
│
└─── ai-transformation-expert ──→ 03-일하는 방식의 변화-AI.md`, `04-생성형AI의 개념과 작동원리.md`, `05-AI시대-우리가 준비해야 하는 것.md
```

**각 에이전트 실행 시 전달할 컨텍스트:**
- 대상 독자: 기업 임직원 (개발 경험 없음, AI 전문 지식 없음)
- 필수 포함: 정확한 정보, 출처 명시, 출시 시기, 비즈니스 효과
- 원리 설명: 어려운 개념은 tech-explainer 스킬 활용하여 풀어쓰기
- 용어: 전문 용어 첫 등장 시 영문 병기, glossary-builder로 용어 추출

### Phase 2: 통합 편집 (팬인)
content-assembler가 5개 산출물을 통합.

```
01-ai-trend-report.md ─────────┐
02-trends-and-services.md ──┤
03-일하는 방식의 변화-AI.md ─┤─→ content-assembler ─→ AI-Education-Complete.md
04-생성형AI의 개념과 작동원리.md ──┤
05-AI시대-우리가 준비해야 하는 것.md─┘
                              └─→ appendix-glossary.md (용어 사전)
```

**통합 시 체크:**
- [ ] 챕터 간 용어 통일
- [ ] 날짜/수치 일관성
- [ ] 중복 내용 제거
- [ ] 챕터 연결 문장 추가
- [ ] 포맷 일관성 (content-formatter 스킬 적용)
- [ ] 부록 용어 사전 완성

### Phase 3: 검증 (생성-검증)
fact-checker가 최종 문서를 검증.

```
AI-Education-Complete.md ─→ fact-checker ─→ fact-check-report.md
                                         ─→ 수정 사항 반영
```

### Phase 4: 최종 완성
검증 결과 반영 후 최종 버전 저장.

## 에이전트 실행 방법

### Agent 도구 사용 예시
```
Phase 1에서 3개 에이전트를 병렬 실행:

Agent(
  name: "ai-trend-analyst",
  prompt: "ai-trend-analyst 에이전트로서 ChatGPT 이후 AI 트랜드 변화를 조사하여 output/01-ai-trend-report.md를 작성하세요. [상세 지시사항]",
  run_in_background: true
)

Agent(
  name: "ai-transformation-expert",
  prompt: "생성형 AI 전문가 에이전트로서 AI의 역사와 트랜드 변화, 기술 지식을 바탕으로 output/04-생성형AI의 개념과 작동원리.md를 작성하세요. [상세 지시사항]",
  run_in_background: true
)

... (나머지 2개도 동시 실행)
```

## 산출물 목록

| 파일 | 내용 | 예상 분량 |
|------|------|----------|
| `output/01-ai-trend-report.md` | 제1장: AI 트랜드 분석 | 4,000자+ |
| `output/02-trends-and-services.md` | 제2장: AI 시장 변화 | 5,000자+ |
| `output/03-일하는 방식의 변화-AI.md` | 제3장: 생성형 AI의 기본 이해와 서비스 설명 | 5,000자+ |
| `output/04-생성형AI의 개념과 작동원리.md` | 제4장: 생성형 AI의 핵심 개념과 작동 원리 | 7,000자+ |
| `output/05-AI시대-우리가 준비해야 하는 것.md` | 제5장: 생성형 AI를 배워야 하는 이유와 필요 역량 | 5,000자+ |
| `output/appendix-glossary.md` | 부록: AI 용어 사전 | 3,000자+ |
| `output/AI-Education-Complete.md` | 통합 최종본 | 25,000자+ |
| `output/fact-check-report.md` | 팩트체크 보고서 | - |

## 품질 기준
- 모든 날짜/수치에 출처 명시
- 전문 용어는 부록 용어 사전에 수록
- 각 챕터에 최소 3개 이상의 표/테이블
- 어려운 개념마다 "쉽게 이해하기" 박스
- 일반 회사원들이 2-3시간 내 학습 가능한 분량과 난이도
