---
name: book-production
description: "AI 트렌드 온보딩 완벽 가이드 책 제작 오케스트레이터. AI-Education-Complete.md를 기반으로 6개 챕터 병렬 집필, 삽화 생성, 통합 편집, PDF 생성까지 전 과정을 조율. '책 제작', '북 프로덕션' 요청 시 사용."
---

# Book Production Orchestrator

AI-Education-Complete.md를 기반으로 "AI 트렌드 온보딩 완벽 가이드" 책을 제작하는 통합 오케스트레이터.

## 실행 모드: 서브 에이전트

> 서브 에이전트 선택 사유: 각 챕터 집필이 완전히 독립적이며 교차 통신 불필요. 기존 콘텐츠를 재구성하는 작업이므로 병렬 속도 최적화가 핵심.

## 에이전트 구성

| 에이전트 | subagent_type | 역할 | 출력 |
|---------|--------------|------|------|
| ch1-writer ~ ch6-writer | book-chapter-writer | 챕터별 집필 | `_workspace/ch{N}.md` |
| ch1-illustrator ~ ch6-illustrator | book-illustrator | 챕터별 삽화 생성 | `output/images/ch{N}_*.png` |
| final-editor | book-editor | 통합 편집 | `_workspace/book-complete.md` |

## 책 구조 (중복 제거 후 재구성)

| 챕터 | 제목 | 원본 범위 | 삽화 수 |
|------|------|----------|--------|
| 프롤로그 | 왜 지금 AI를 알아야 하는가 | 신규 작성 | 1 |
| Ch1 | 3년의 혁명 — AI 타임라인 2022~2026 | Ch1 (타임라인 + 투자), 모델 상세는 Ch3으로 | 2 |
| Ch2 | AI는 어떻게 생각하는가 | Ch2 §2.2 (기술 원리만), 모델 목록은 Ch3으로 | 3 |
| Ch3 | AI 모델 전쟁 | Ch2 §2.1(모델 비교) + Ch3 §3.2(범용 모델) 통합 | 2 |
| Ch4 | AI가 바꾸는 세상 | Ch3 §3.3~3.6 (응용 서비스 + 비즈니스), 범용 모델 제거 | 2 |
| Ch5 | 코드 없이 코딩하기 | Ch4-1 (바이브코딩), Ch3의 바이브코딩 언급 제거 | 2 |
| Ch6 | AI 팀을 지휘하라 | Ch4-2 (하네스 엔지니어링) | 2 |
| 부록 | 용어 사전 | 부록A (선별 정리) | 0 |
| 에필로그 | AI 시대를 준비하며 | 마무리 재구성 | 1 |

## 워크플로우

### Phase 1: 준비
1. `_workspace/` 디렉토리 생성
2. `output/images/` 디렉토리 생성
3. 소스 자료(`AI-Education-Complete.md`) 확인

### Phase 2: 병렬 챕터 집필 (팬아웃)

**실행 방식:** 6개 Agent를 동시 호출 (run_in_background: true)

각 Agent 프롬프트에 포함할 정보:
- 담당 챕터 번호, 제목
- 원본에서 참조할 범위 (라인 번호 또는 섹션 헤더)
- **제외할 내용** (다른 챕터로 이동한 내용)
- 삽화 위치 지정 요청 (`<!-- IMAGE: ... -->` 태그)
- 집필 스타일 가이드 (book-chapter-writer 에이전트 정의 참조)

| 에이전트 | 입력 범위 | 제외 사항 | 출력 |
|---------|----------|----------|------|
| ch1-writer | Ch1 전체 (L20~L213) | 모델별 상세 스펙(→Ch3), 투자 상세(핵심만 유지) | `_workspace/ch1.md` |
| ch2-writer | Ch2 §2.2 (L309~L400) | 모델 목록(→Ch3), 스케일링 분석 핵심만 | `_workspace/ch2.md` |
| ch3-writer | Ch2 §2.1(L228~L306) + Ch3 §3.2(L625~L701) | 응용 서비스(→Ch4), 추론 모델은 Ch2에서 다룸 | `_workspace/ch3.md` |
| ch4-writer | Ch3 §3.3~3.6(L704~L886) | 범용 모델(→Ch3), 바이브코딩 상세(→Ch5) | `_workspace/ch4.md` |
| ch5-writer | Ch4 §4-1(L912~L1177) | 하네스(→Ch6) | `_workspace/ch5.md` |
| ch6-writer | Ch4 §4-2(L1180~L1616) + 부록 용어사전 선별 | 바이브코딩(→Ch5) | `_workspace/ch6.md` |

### Phase 3: 병렬 삽화 생성 (팬아웃)

**실행 방식:** Phase 2 완료 후, 각 챕터별 illustrator를 동시 호출

각 illustrator에게:
1. 해당 챕터 markdown 파일 경로 제공
2. `<!-- IMAGE: ... -->` 태그에서 이미지 설명 추출
3. gemini-3-pro-imagegen 스킬로 이미지 생성
4. `output/images/ch{N}_{seq}.png`에 저장

이미지 스타일 프롬프트 (모든 이미지 공통):
"손그림 스타일의 교육용 인포그래픽. 따뜻한 크림색 종이 배경에 색연필과 마카로 그린 듯한 질감. 귀엽고 아기자기한 'doodle' 아트 스타일. 파스텔 톤의 부드러운 색상 팔레트 사용. 각 아이콘과 손글씨 타이포그래피, 화살표와 반짝이 장식 요소 포함. 친근하고 직관적인 구성."

### Phase 4: 통합 편집 (팬인)

**실행 방식:** Phase 3 완료 후, book-editor 에이전트 호출

1. 6개 챕터 파일을 Read로 수집
2. 프롤로그/에필로그 작성
3. 챕터 간 연결 문장 추가
4. 톤/스타일/용어 통일
5. 이미지 참조 태그를 실제 경로로 변환
6. 부록(용어 사전) 정리
7. 최종 파일 저장: `_workspace/book-complete.md`

### Phase 5: PDF 생성

**실행 방식:** pdf 스킬 호출

1. `_workspace/book-complete.md`를 PDF로 변환
2. 이미지 포함
3. 목차 자동 생성
4. 최종 출력: `output/AI-트렌드-온보딩-완벽가이드.pdf`

### Phase 6: 정리
1. `_workspace/` 보존 (중간 산출물 감사 추적용)
2. 사용자에게 결과 요약 보고

## 데이터 흐름

```
AI-Education-Complete.md
    │
    ├→ [ch1-writer] → ch1.md ─→ [ch1-illustrator] → images/ch1_*.png
    ├→ [ch2-writer] → ch2.md ─→ [ch2-illustrator] → images/ch2_*.png
    ├→ [ch3-writer] → ch3.md ─→ [ch3-illustrator] → images/ch3_*.png
    ├→ [ch4-writer] → ch4.md ─→ [ch4-illustrator] → images/ch4_*.png
    ├→ [ch5-writer] → ch5.md ─→ [ch5-illustrator] → images/ch5_*.png
    └→ [ch6-writer] → ch6.md ─→ [ch6-illustrator] → images/ch6_*.png
                                        │
                                        ↓
                              [book-editor] → book-complete.md
                                        │
                                        ↓
                              [pdf skill] → AI-트렌드-온보딩-완벽가이드.pdf
```

## 에러 핸들링

| 상황 | 전략 |
|------|------|
| 챕터 작성 실패 | 1회 재시도. 재실패 시 원본 내용을 그대로 사용 |
| 이미지 생성 실패 | 1회 재시도(프롬프트 단순화). 재실패 시 이미지 없이 진행 |
| 편집 에이전트 실패 | 메인이 직접 챕터 병합 수행 |
| PDF 생성 실패 | pdf 스킬 재시도. 실패 시 markdown으로 최종 산출물 제공 |

## 테스트 시나리오

### 정상 흐름
1. AI-Education-Complete.md 확인 (1886줄)
2. Phase 2: 6개 챕터 작성 에이전트 병렬 실행 → 6개 md 파일 생성
3. Phase 3: 6개 삽화 에이전트 병렬 실행 → ~15개 이미지 생성
4. Phase 4: 통합 편집 → book-complete.md (원본 대비 30% 이상 축소)
5. Phase 5: PDF 생성 → AI-트렌드-온보딩-완벽가이드.pdf
6. 예상 결과: output/ 디렉토리에 PDF + images/ 디렉토리

### 에러 흐름
1. Phase 2에서 ch3-writer 실패
2. 1회 재시도 후에도 실패
3. Ch2 §2.1 + Ch3 §3.2 원본을 그대로 사용
4. Phase 4에서 editor가 원본 내용도 톤 통일 처리
5. 최종 보고서에 "Ch3 자동 재구성 미완료, 원본 기반" 명시
