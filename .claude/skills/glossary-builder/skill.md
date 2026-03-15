---
name: glossary-builder
description: "AI 용어 사전 구축 스킬. 교육 자료에 등장하는 AI 관련 전문 용어를 수집하고, 정의/영문 원어/관련 용어를 정리하여 부록 용어 사전 생성. '용어 사전', '부록', '용어 정리' 시 사용."
---

# Glossary Builder — AI 용어 사전 구축 스킬

## 목적
교육 자료에 등장하는 AI 전문 용어를 체계적으로 수집/정의하여 부록 용어 사전 생성.

## 워크플로우

### Step 1: 용어 수집
- 각 챕터 산출물에서 전문 용어 추출
- 카테고리별 분류 (모델/아키텍처/학습/서비스/비즈니스 등)

### Step 2: 정의 작성
각 용어에 대해:
1. **한글명 (영문 원어)**
2. **한줄 정의** (30자 이내)
3. **상세 설명** (2-3문장, 쉬운 표현)
4. **관련 용어** 태그
5. **첫 등장 챕터** 표기

### Step 3: 용어 사전 포맷

```markdown
## AI 용어 사전

### ㄱ
**강화학습 (Reinforcement Learning, RL)**
한줄: 시행착오를 통해 보상을 최대화하는 학습 방법
설명: 에이전트가 환경과 상호작용하며, 좋은 행동에는 보상을, 나쁜 행동에는 벌점을 받아
      점차 최적의 행동을 학습하는 방식입니다. 게임 AI나 RLHF에 활용됩니다.
관련: RLHF, DPO, PPO
등장: 제2장

### ㅂ
**바이브코딩 (Vibe Coding)**
한줄: AI에게 의도만 전달하여 코드를 생성하는 개발 방식
설명: 2025년 Andrej Karpathy가 명명한 용어로, 개발자가 자연어로 원하는 기능을 설명하면
      AI가 코드를 작성하는 방식입니다. 전통적 코딩의 패러다임 전환을 의미합니다.
관련: 프롬프트 엔지니어링, AI 코딩 도구, Cursor
등장: 제4장
```

## 정렬 규칙
- 한글 가나다순 (ㄱ, ㄴ, ㄷ...)
- 영문 약어는 풀네임 기준으로 분류하되, 약어에서 참조 안내
  - "GPT → 생성형 사전훈련 트랜스포머(GPT) 참조"

## 필수 수록 용어 (최소)
- Transformer, Attention, 토큰, 임베딩, 파인튜닝
- LLM, sLLM, Foundation Model, Pre-training
- RLHF, DPO, SFT, PPO
- Prompt Engineering, Few-shot, Zero-shot, CoT
- RAG, Vector DB, Embedding
- Agent, MCP, Tool Use, Function Calling
- MoE, Scaling Law, Emergent Ability
- Hallucination, Alignment, Safety
- API, SDK, Inference, Latency
- 바이브코딩, 하네스 엔지니어링
- Multimodal, Vision, TTS, STT
- LoRA, QLoRA, Quantization, Distillation

## 출력
`output/appendix-glossary.md`에 저장
