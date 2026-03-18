---
name: book-production
description: "AI 트렌드 책 제작 오케스트레이터. AI-Education-Complete.md를 기반으로 5개 챕터 병렬 집필, 삽화 생성, 통합 편집, PDF 생성까지 전 과정을 조율. '책 제작', '북 프로덕션' 요청 시 사용."
---

# Book Production Orchestrator

AI-Education-Complete.md를 기반으로 "AI 트렌드 온보딩 완벽 가이드" 책을 제작하는 통합 오케스트레이터.

## 실행 모드: 서브 에이전트

> 서브 에이전트 선택 사유: 각 챕터 집필이 완전히 독립적이며 교차 통신 불필요. 기존 콘텐츠를 재구성하는 작업이므로 병렬 속도 최적화가 핵심.

## 에이전트 구성

| 에이전트 | subagent_type | 역할 | 출력 |
|---------|--------------|------|------|
| ch1-writer ~ ch5-writer | book-chapter-writer | 챕터별 집필 | `_workspace/ch{N}.md` |
| ch1-illustrator ~ ch5-illustrator | book-illustrator | 챕터별 삽화 생성 | `output/images/ch{N}_*.png` |
| final-editor | book-editor | 통합 편집 | `_workspace/book-complete.md` |

## 책 구조 (중복 제거 후 재구성)

| 챕터 | 제목 | 원본 범위 | 삽화 수 |
|------|------|----------|--------|
| 프롤로그 | 왜 지금 AI를 알아야 하는가 | 신규 작성 | 1 |
| Ch1 | AI 트랜드 분석 | 제1장 전체 | 2 |
| Ch2 | AI 시장 변화 | 제2장 전체 | 2 |
| Ch3 | 생성형 AI의 기본 이해와 서비스 설명 | 제3장 전체 | 2 |
| Ch4 | 생성형 AI의 핵심 개념과 작동 원리 | 제4장 전체 | 3 |
| Ch5 | 생성형 AI를 배워야 하는 이유와 필요 역량 | 제5장 전체 | 2 |
| 부록 | 용어 사전 | 부록 문서 기반 | 0 |
| 에필로그 | AI 시대를 준비하며 | 마무리 재구성 | 1 |

## 워크플로우

### Phase 1: 준비
1. `_workspace/` 디렉토리 생성
2. `output/images/` 디렉토리 생성
3. 소스 자료(`AI-Education-Complete.md`) 확인

### Phase 2: 병렬 챕터 집필 (팬아웃)

**실행 방식:** 5개 Agent를 동시 호출 (run_in_background: true)

각 Agent 프롬프트에 포함할 정보:
- 담당 챕터 번호, 제목
- 원본에서 참조할 범위 (해당 챕터 내용)
- 삽화 위치 지정 요청 (`<!-- IMAGE: ... -->` 태그)
- 집필 스타일 가이드 (book-chapter-writer 에이전트 정의 참조)

| 에이전트 | 입력 범위 | 출력 |
|---------|----------|------|
| ch1-writer | 제1장 전체 | `_workspace/ch1.md` |
| ch2-writer | 제2장 전체 | `_workspace/ch2.md` |
| ch3-writer | 제3장 전체 | `_workspace/ch3.md` |
| ch4-writer | 제4장 전체 | `_workspace/ch4.md` |
| ch5-writer | 제5장 전체 | `_workspace/ch5.md` |

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

1. 5개 챕터 파일을 Read로 수집
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
    └→ [ch5-writer] → ch5.md ─→ [ch5-illustrator] → images/ch5_*.png
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
2. Phase 2: 5개 챕터 작성 에이전트 병렬 실행 → 5개 md 파일 생성
3. Phase 3: 5개 삽화 에이전트 병렬 실행 → ~15개 이미지 생성
4. Phase 4: 통합 편집 → book-complete.md (원본 대비 30% 이상 축소)
5. Phase 5: PDF 생성 → AI-트렌드-온보딩-완벽가이드.pdf
6. 예상 결과: output/ 디렉토리에 PDF + images/ 디렉토리

### 에러 흐름
1. Phase 2에서 ch3-writer 실패
2. 1회 재시도 후에도 실패
3. Ch2 §2.1 + Ch3 §3.2 원본을 그대로 사용
4. Phase 4에서 editor가 원본 내용도 톤 통일 처리
5. 최종 보고서에 "Ch3 자동 재구성 미완료, 원본 기반" 명시
