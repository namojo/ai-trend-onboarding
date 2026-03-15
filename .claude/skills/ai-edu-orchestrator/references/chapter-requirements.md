# 챕터별 상세 요구사항

## 제1장: AI 변화의 타임라인 (ai-historian)

### 필수 포함 이벤트
- 2022.11: ChatGPT 출시
- 2023.01: Microsoft-OpenAI $100억 투자
- 2023.02: Bing Chat / Google Bard 발표
- 2023.03: GPT-4 출시
- 2023.03: Claude 출시 (Anthropic)
- 2023.05: Google PaLM 2 / Google I/O
- 2023.07: Meta LLaMA 2 오픈소스 공개
- 2023.07: Claude 2 출시
- 2023.09: DALL-E 3 출시
- 2023.11: OpenAI DevDay (GPT-4 Turbo, GPTs, 샘 알트먼 해임-복귀)
- 2023.12: Google Gemini 1.0 출시
- 2023.12: Mistral AI Mixtral 8x7B
- 2024.02: Google Gemini 1.5 (100만 토큰)
- 2024.02: Sora 공개 (동영상 생성)
- 2024.03: Claude 3 시리즈 출시
- 2024.04: Meta LLaMA 3 출시
- 2024.05: GPT-4o 출시 (멀티모달)
- 2024.06: Claude 3.5 Sonnet 출시
- 2024.06: Apple Intelligence 발표
- 2024.08: AI 안전 관련 각국 규제 동향
- 2024.09: o1 출시 (추론 모델)
- 2024.10: Claude 3.5 Sonnet (신규) + Computer Use
- 2024.12: Google Gemini 2.0 / Sora 정식 출시
- 2025.01: DeepSeek R1 공개 (저비용 추론 모델)
- 2025.01: o3-mini 출시
- 2025.02: Claude 3.7 Sonnet (하이브리드 추론)
- 2025.02: GPT-4.5 출시
- 2025.03: Claude 3.7 Opus / Claude 4 계열
- 2025.03~: 에이전트 시대 본격화
- (이후 최신 이벤트는 웹 리서치로 보완)

### 표현 형식
- 연도별 대형 표 + 연도별 1문장 요약
- 변화 속도 수치화 ("2023년 주요 모델 X개 vs 2024년 Y개")

---

## 제2장: AI 모델의 진화와 스케일링 (model-analyst)

### 필수 다룰 주제
1. **GPT 계열 진화**: 3.5 → 4 → 4o → 4.5 → o1 → o3
2. **Claude 계열 진화**: 1 → 2 → 3 → 3.5 → 3.7 → 4
3. **Gemini 계열 진화**: 1.0 → 1.5 → 2.0 → 2.5
4. **오픈소스 진화**: LLaMA → LLaMA 2 → 3 → 3.1 → 4
5. **핵심 기술 변화**:
   - MoE (Mixture of Experts) 원리와 효과
   - RLHF → DPO 진화
   - 추론 시간 컴퓨팅 (test-time compute)
   - 긴 컨텍스트 (4K → 128K → 1M+)
   - 소형 모델의 반격 (sLLM)
   - 멀티모달 통합
6. **스케일링 법칙**: Chinchilla, 데이터 품질 vs 양
7. **발전 속도 분석**: 반기별 비교, 무어의 법칙 대비

### 기술 원리 풀어쓰기 (tech-explainer 활용)
- Transformer와 Attention 메커니즘
- 토큰과 토크나이저
- 사전훈련 → 파인튜닝 → RLHF 파이프라인
- MoE가 효율적인 이유
- 추론 모델(o1/o3)의 사고 과정

---

## 제3장: 최신 기술과 응용 서비스 (trend-researcher)

### 분류 기준
**범용 모델**: 다양한 용도로 사용 가능한 기반 모델
**응용 서비스**: 특정 문제 해결을 위해 범용 모델을 활용한 서비스/제품

### 필수 포함 범용 모델 (2025년 초~)
- GPT-4.5, o3, o3-mini (OpenAI)
- Claude 3.7 Sonnet, Claude 4 계열 (Anthropic)
- Gemini 2.0/2.5 (Google)
- LLaMA 4 (Meta)
- DeepSeek R1, V3 (DeepSeek)
- Grok 3 (xAI)
- 최신 이미지/영상 생성 모델

### 필수 포함 응용 서비스
- AI 코딩: Cursor, GitHub Copilot, Claude Code, Windsurf
- AI 검색: Perplexity, ChatGPT Search, Gemini
- AI 에이전트: Devin, Manus, Claude Agent SDK
- AI 디자인: v0, Figma AI
- AI 영상: Sora, Veo, Kling
- 기업용: Microsoft 365 Copilot, Notion AI, Slack AI

### 모델-서비스 매핑 테이블 필수

---

## 제4장: 바이브코딩과 하네스 엔지니어링 (devpractice-expert)

### 바이브코딩 섹션
- Karpathy 원문 인용 및 맥락
- 도구별 비교표 (Cursor, Copilot, Claude Code, Windsurf, v0, bolt)
- 실전 워크플로우 예시 (새 프로젝트 시작부터 배포까지)
- 생산성 향상 데이터/사례
- 한계와 주의사항 (보안, 품질, 디버깅)

### 하네스 엔지니어링 섹션
- 프롬프트 엔지니어링 → 에이전트 → 하네스의 진화
- 하네스 구조 (에이전트, 스킬, 오케스트레이션)
- 디자인 패턴 (파이프라인, 팬아웃, 전문가 풀)
- Claude Code에서의 실제 구현 예시
- 미래 전망 (Agent SDK, MCP 등)

---

## 부록A: AI 용어 사전 (glossary-builder)

### 카테고리
1. 모델/아키텍처 (Transformer, Attention, MoE...)
2. 학습 방법 (Pre-training, Fine-tuning, RLHF, DPO...)
3. 추론/서빙 (Inference, Latency, Quantization...)
4. 응용/서비스 (RAG, Agent, MCP, Tool Use...)
5. 새로운 개념 (바이브코딩, 하네스, 추론 모델...)
6. 비즈니스 (ARR, API, SaaS, Foundation Model...)

### 최소 50개 용어 수록
