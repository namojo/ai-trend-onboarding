# 제1장. AI 산업의 대전환: ChatGPT부터 에이전트 시대까지 (2022~2026)

---

## 이 챕터에서 배울 내용

> - ChatGPT 출시(2022.11) 이후 AI 산업이 어떤 속도로 변화해왔는지 **연도별 타임라인**으로 파악합니다.
> - OpenAI, Google, Anthropic, Meta, xAI 등 **주요 플레이어의 모델 출시 전략**을 비교합니다.
> - 모델 개발뿐 아니라 **투자, 정책, 오픈소스** 영역의 변화를 함께 이해합니다.
> - 2026년 현재까지의 최신 동향을 포함하여, **앞으로의 흐름을 예측**할 수 있는 기초를 다집니다.

---

## 1. 연도별 1문장 요약

| 연도 | 키워드 | 요약 |
|------|--------|------|
| **2022** | ChatGPT, 대중화 | OpenAI가 ChatGPT를 출시하며 생성형 AI가 일반 대중의 일상에 진입했습니다. |
| **2023** | GPT-4, 경쟁 격화, 오픈소스 | GPT-4를 필두로 Google, Anthropic, Meta가 본격 참전하고, 샘 알트먼 해임 사태로 AI 거버넌스 문제가 부각되었습니다. |
| **2024** | 멀티모달, 추론, 영상생성 | GPT-4o, Claude 3, Gemini 1.5 등 멀티모달 모델이 대세가 되고, o1과 Sora로 추론과 영상 생성의 새 장이 열렸습니다. |
| **2025** | DeepSeek, 에이전트, 초거대 투자 | DeepSeek R1의 충격, GPT-5 통합 모델의 등장, 5000억 달러 규모 Stargate 프로젝트로 AI 인프라 경쟁이 본격화되었습니다. |
| **2026** | 초고속 반복, AGI 접근 | 2~3주 단위 모델 업데이트가 일상화되고, Claude Opus 4.6, GPT-5.3, Gemini 3.1 등이 경쟁하며 AGI에 한 걸음 더 다가갔습니다. |

---

## 2. 연도별 상세 타임라인

### 2022년: 시작의 해

| 시기 | 이벤트 | 주체 | 카테고리 | 의미 | 출처 |
|------|--------|------|----------|------|------|
| 2022.11.30 | **ChatGPT 출시** | OpenAI | 서비스 | GPT-3.5 기반 대화형 AI 서비스 공개. 출시 5일 만에 100만 사용자 돌파, 2개월 만에 1억 사용자 달성. 역사상 가장 빠르게 성장한 소비자 앱이 되었습니다. | [OpenAI 공식 블로그](https://openai.com/blog/chatgpt) |

---

### 2023년: 경쟁의 서막

| 시기 | 이벤트 | 주체 | 카테고리 | 의미 | 출처 |
|------|--------|------|----------|------|------|
| 2023.02.06 | **Google Bard 발표** | Google | 서비스 | Google이 ChatGPT에 대응하여 Bard를 발표. 3월 21일 미국/영국에서 제한 공개되었습니다. | [Google Blog](https://blog.google/technology/ai/bard-google-ai-search-updates/) |
| 2023.03.14 | **GPT-4 출시** | OpenAI | 모델 | 멀티모달(텍스트+이미지 입력) 지원. 변호사 시험 상위 10% 수준의 성능을 보여주며 LLM 성능의 새 기준을 제시했습니다. | [OpenAI 공식 발표](https://openai.com/index/gpt-4/) |
| 2023.03.14 | **Claude 1.0 출시** | Anthropic | 모델 | 안전성을 강조한 Constitutional AI 기반 모델 공개. OpenAI의 대항마로 등장했습니다. | [Anthropic 공식](https://www.anthropic.com) |
| 2023.07.18 | **LLaMA 2 오픈소스 공개** | Meta | 오픈소스 | Microsoft와 협력하여 7B/13B/70B 파라미터 모델을 상업적 사용 가능한 라이선스로 공개. 오픈소스 LLM 생태계의 폭발적 성장을 이끌었습니다. | [Meta 공식 발표](https://about.fb.com/news/2023/07/llama-2/) |
| 2023.11.06 | **GPTs 및 GPT Store 발표** | OpenAI | 서비스 | 첫 개발자 컨퍼런스 DevDay에서 커스텀 GPT 생성 기능과 GPT Store 계획을 발표. AI 앱스토어 시대를 예고했습니다. (실제 GPT Store 오픈은 2024.01) | [OpenAI DevDay](https://openai.com/index/introducing-the-gpt-store/) |
| 2023.11.17 | **샘 알트먼 해임** | OpenAI 이사회 | 정책 | OpenAI 이사회가 "소통의 일관성 부족"을 이유로 CEO를 해임. 전 직원의 95%가 복귀를 요구하는 전례 없는 사태가 발생했습니다. | [TechCrunch 타임라인](https://techcrunch.com/2024/01/05/a-timeline-of-sam-altmans-firing-from-openai-and-the-fallout/) |
| 2023.11.22 | **샘 알트먼 복귀** | OpenAI | 정책 | 5일 만에 CEO 복귀. 새로운 이사회 구성(Bret Taylor 의장). AI 기업 거버넌스의 취약성과 핵심 인물 의존도를 드러냈습니다. | [ABC News](https://abcnews.go.com/Business/sam-altman-reaches-deal-return-ceo-openai/story?id=105091534) |
| 2023.12.06 | **Gemini 1.0 발표** | Google DeepMind | 모델 | Google의 차세대 멀티모달 AI 모델 패밀리(Ultra/Pro/Nano) 발표. GPT-4와 정면 승부를 선언했습니다. | [Google DeepMind 블로그](https://blog.google/technology/ai/google-gemini-ai/) |

---

### 2024년: 멀티모달과 추론의 해

| 시기 | 이벤트 | 주체 | 카테고리 | 의미 | 출처 |
|------|--------|------|----------|------|------|
| 2024.02.07 | **Bard를 Gemini로 리브랜딩** | Google | 서비스 | Bard 서비스명을 Gemini로 통합. Gemini Advanced(Ultra 1.0 기반) 유료 서비스 출시. AI 브랜드 전략의 전환점이었습니다. | [Google Blog](https://blog.google/products/gemini/) |
| 2024.02.15 | **Sora 프리뷰 공개** | OpenAI | 모델 | 텍스트-투-비디오 생성 모델 최초 공개. 1분 길이 고품질 영상 생성으로 크리에이티브 산업에 충격을 주었습니다. | [OpenAI 공식](https://openai.com/index/sora/) |
| 2024.02 | **Gemini 1.5 Pro 프리뷰** | Google | 모델 | 100만 토큰 컨텍스트 윈도우 최초 달성. 장문 처리 능력에서 새로운 기준을 제시했습니다. | [Google Blog](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) |
| 2024.03.04 | **Claude 3 패밀리 출시** | Anthropic | 모델 | Opus/Sonnet/Haiku 3종 동시 출시. Claude 3 Opus가 GPT-4를 일부 벤치마크에서 최초로 추월했습니다. | [Anthropic 공식](https://www.anthropic.com/news/claude-3-family) |
| 2024.04 | **LLaMA 3 출시** | Meta | 오픈소스 | 8B/70B 모델 공개. 오픈소스 모델의 성능이 상용 모델에 근접하기 시작했습니다. | [Meta AI Blog](https://ai.meta.com/blog/meta-llama-3/) |
| 2024.05.13 | **GPT-4o 출시** | OpenAI | 모델 | "Omni" 모델로 텍스트/음성/이미지를 통합 처리. 무료 사용자에게도 공개하여 AI 접근성을 대폭 확대했습니다. | [OpenAI 공식](https://openai.com/index/hello-gpt-4o/) |
| 2024.06.20 | **Claude 3.5 Sonnet 출시** | Anthropic | 모델 | 중간 티어 모델이 플래그십(Opus)을 능가하는 이변. 코딩 성능에서 업계 최고 수준을 달성했습니다. | [Anthropic 공식](https://www.anthropic.com/news/claude-3-5-sonnet) |
| 2024.08 | **Grok-2 출시** | xAI | 모델 | 일론 머스크의 xAI가 Grok-2를 출시하며 AI 모델 경쟁에 본격 합류했습니다. | [xAI 공식](https://x.ai/news) |
| 2024.09.12 | **OpenAI o1 프리뷰 출시** | OpenAI | 모델 | "추론(reasoning)" 특화 모델의 시작. Chain-of-thought를 내재화하여 수학/코딩에서 획기적 성능 향상을 보였습니다. | [OpenAI 공식](https://openai.com/index/introducing-openai-o1-preview/) |
| 2024.10.02 | **OpenAI 66억 달러 투자 유치** | OpenAI | 투자 | 1,570억 달러 기업가치로 66억 달러 조달. Thrive Capital 주도, Microsoft/Nvidia 참여. AI 스타트업 역대 최대 규모 펀딩이었습니다. | [CNBC 보도](https://www.cnbc.com/2024/10/02/openai-raises-at-157-billion-valuation-microsoft-nvidia-join-round.html) |
| 2024.10.22 | **Claude 3.5 Sonnet 업그레이드 + Computer Use** | Anthropic | 모델/서비스 | 업그레이드된 Sonnet과 함께 AI가 컴퓨터를 직접 조작하는 Computer Use 기능을 최초 공개했습니다. | [Anthropic 공식](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| 2024.12.05 | **OpenAI o1 정식 출시** | OpenAI | 모델 | 추론 모델의 정식 버전. 복잡한 과학/수학 문제에서 인간 전문가 수준에 도달했습니다. | [OpenAI 공식](https://openai.com) |
| 2024.12.09 | **Sora Turbo 공개 출시** | OpenAI | 서비스 | sora.com에서 ChatGPT Plus/Pro 사용자에게 영상 생성 서비스를 정식 오픈했습니다. | [OpenAI 공식](https://openai.com/index/sora-is-here/) |
| 2024.12.11 | **Gemini 2.0 Flash 출시** | Google | 모델 | 에이전트 시대를 위한 차세대 모델. 멀티모달 라이브 API, 네이티브 이미지 생성, Google 검색 통합 기능을 제공합니다. | [Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/) |
| 2024.12.20 | **OpenAI o3 발표** | OpenAI | 모델 | 차세대 추론 모델 발표. ARC-AGI 벤치마크에서 획기적 성과를 달성하며 2024년을 마무리했습니다. | [OpenAI 공식](https://openai.com) |

---

### 2025년: 에이전트와 초거대 투자의 해

| 시기 | 이벤트 | 주체 | 카테고리 | 의미 | 출처 |
|------|--------|------|----------|------|------|
| 2025.01.20 | **DeepSeek R1 출시** | DeepSeek (중국) | 모델/오픈소스 | MIT 라이선스 오픈소스 추론 모델. GPT-4/o1 수준 성능을 저비용으로 달성하여 "AI 스푸트니크 모먼트"라 불렸습니다. 1주일 만에 iOS 앱스토어 1위 달성. | [DeepSeek API Docs](https://api-docs.deepseek.com/news/news250120) |
| 2025.01.21 | **Stargate 프로젝트 발표** | OpenAI/SoftBank/Oracle | 투자 | 트럼프 대통령이 백악관에서 발표. 4년간 5,000억 달러 규모 AI 인프라 투자 합작법인. 초기 1,000억 달러 즉시 투입. 10만 개 일자리 창출 목표. | [OpenAI 공식](https://openai.com/index/announcing-the-stargate-project/) |
| 2025.01.31 | **o3-mini 출시** | OpenAI | 모델 | 경량화된 추론 모델로 비용 효율적인 추론 AI 접근을 가능하게 했습니다. | [OpenAI 공식](https://openai.com) |
| 2025.02.02 | **EU AI Act 1차 시행** | EU | 정책 | 허용 불가 위험 AI(사회적 점수제, 취약계층 조작 등) 금지 조항 발효. 세계 최초의 포괄적 AI 규제가 본격 시행되었습니다. | [EU 공식](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) |
| 2025.02.17 | **Grok 3 출시** | xAI | 모델 | xAI의 플래그십 모델. 추론 성능에서 상위권 진입하며 경쟁 구도를 5파전으로 확대했습니다. | [xAI 공식](https://x.ai/news) |
| 2025.02.24 | **Claude 3.7 Sonnet 출시** | Anthropic | 모델 | "확장된 사고(extended thinking)" 기능 도입. 하이브리드 추론 모델의 새 패러다임을 제시했습니다. | [Anthropic 공식](https://www.anthropic.com) |
| 2025.02.27 | **GPT-4.5 출시** | OpenAI | 모델 | 코드명 "Orion". 샘 알트먼이 "사려 깊은 사람과 대화하는 느낌"이라 표현한 모델. GPT-5 이전의 마지막 GPT-4 계열 모델이었습니다. | [OpenAI 공식](https://openai.com/index/introducing-gpt-4-5/) |
| 2025.03.25 | **Gemini 2.5 Pro 실험 버전** | Google | 모델 | Chain-of-thought 추론을 네이티브로 지원하는 차세대 모델 공개. | [Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| 2025.03.31 | **OpenAI 400억 달러 투자 유치** | OpenAI | 투자 | 사상 최대 민간 기업 펀딩. SoftBank 300억 달러 주도, 기업가치 3,000억 달러. | [CNBC 보도](https://www.cnbc.com/2025/03/31/openai-closes-40-billion-in-funding-the-largest-private-fundraise-in-history-softbank-chatgpt.html) |
| 2025.04.05 | **LLaMA 4 출시** | Meta | 오픈소스 | Scout(109B)/Maverick(400B) MoE 아키텍처 공개. 최대 1,000만 토큰 컨텍스트, 멀티모달 지원. 오픈소스 모델의 새 이정표를 세웠습니다. | [TechCrunch 보도](https://techcrunch.com/2025/04/05/meta-releases-llama-4-a-new-crop-of-flagship-ai-models/) |
| 2025.04.16 | **o3 및 o4-mini 출시** | OpenAI | 모델 | 추론 모델 라인업 확대. 도구 사용(tool use)을 네이티브로 지원하는 에이전트형 추론 모델이 등장했습니다. | [OpenAI 공식](https://openai.com/index/introducing-o3-and-o4-mini/) |
| 2025.05.22 | **Claude Opus 4 출시** | Anthropic | 모델 | Anthropic의 최상위 모델. 코딩과 에이전트 작업에서 업계 최고 수준을 기록했습니다. | [Anthropic 공식](https://www.anthropic.com) |
| 2025.07 | **Grok 4 출시** | xAI | 모델 | 네이티브 도구 사용과 실시간 검색 통합. "세계에서 가장 지능적인 모델"을 표방했습니다. | [xAI 공식](https://x.ai/news) |
| 2025.08.02 | **EU AI Act GPAI 의무 발효** | EU | 정책 | 범용 AI(GPAI) 모델 제공자 대상 의무 조항 시행. EU AI Office 공식 운영 개시. | [EU AI Act 공식](https://artificialintelligenceact.eu/implementation-timeline/) |
| 2025.08.07 | **GPT-5 출시** | OpenAI | 모델 | OpenAI 최초의 "통합(unified)" 모델. o-시리즈 추론 능력과 GPT 시리즈의 빠른 응답을 결합. 수학/코딩/의료 벤치마크에서 SOTA 달성. | [OpenAI 공식](https://openai.com/index/introducing-gpt-5/) |
| 2025.09.02 | **Anthropic 130억 달러 투자 유치 (Series F)** | Anthropic | 투자 | 기업가치 1,830억 달러. ICONIQ 주도. AI 스타트업 가치 평가의 새로운 차원을 열었습니다. | [Anthropic 공식](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation) |
| 2025.10 | **OpenAI 기업가치 5,000억 달러 돌파** | OpenAI | 투자 | 100억 달러 규모 직원 주식 매각으로 세계 최고 가치 비상장 기업이 되었습니다. | [NBC News 보도](https://www.nbcnews.com/tech/tech-news/microsoft-openai-reach-new-deal-valuing-openai-500-billion-rcna240255) |
| 2025.11.24 | **Claude Opus 4.5 출시** | Anthropic | 모델 | 코딩, 에이전트, 컴퓨터 사용에서 세계 최고 성능 모델. | [Anthropic 공식](https://www.anthropic.com/news/claude-opus-4-5) |

---

### 2026년: 초고속 반복의 시대 (현재 진행 중)

| 시기 | 이벤트 | 주체 | 카테고리 | 의미 | 출처 |
|------|--------|------|----------|------|------|
| 2026.01 | **Grok 5 출시** | xAI | 모델 | 6조 파라미터 규모. AI 모델 스케일링의 새 기록을 세웠습니다. | [xAI 공식](https://x.ai/news) |
| 2026.01.07 | **Anthropic 100억 달러 투자 텀시트 체결** | Anthropic | 투자 | 기업가치 3,500억 달러. Coatue/GIC 주도. | [CNBC 보도](https://www.cnbc.com/2026/01/07/anthropic-funding-term-sheet-valuation.html) |
| 2026.02.05 | **Claude Opus 4.6 출시** | Anthropic | 모델 | 100만 토큰 컨텍스트(베타), 적응형 사고(4단계 노력 수준), Agent Teams 기능. | [Anthropic 공식](https://www.anthropic.com/claude/opus) |
| 2026.02.05 | **GPT-5.3 Codex 출시** | OpenAI | 모델 | 가장 진보된 에이전틱 코딩 모델. 속도 25% 향상. | [OpenAI 공식](https://openai.com) |
| 2026.02.17 | **Claude Sonnet 4.6 출시** | Anthropic | 모델 | Opus급 성능을 Sonnet 가격으로 제공. 비용 효율성의 새 기준. | [Anthropic 공식](https://www.anthropic.com) |
| 2026.02.19 | **Gemini 3.1 Pro 출시** | Google | 모델 | ARC-AGI-2에서 77.1% 달성(전작 31.1%의 2배 이상). Deep Think 추론 네이티브 통합. "AI 슈퍼컴퓨터를 모델에 담다". | [Google 공식](https://blog.google) |
| 2026.02 | **Anthropic 300억 달러 투자 유치 (Series G)** | Anthropic | 투자 | 기업가치 3,800억 달러. AI 기업 투자 사상 최대 규모 중 하나. | [Anthropic 공식](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) |
| 2026.03 (예정) | **NVIDIA GTC 2026** | NVIDIA | 서비스 | 3월 16~19일, 산호세. Jensen Huang 키노트에서 차세대 AI 칩 및 플랫폼 발표 예정. | [NVIDIA GTC](https://www.nvidia.com/gtc/) |
| 2026.03 (예정) | **Apple Siri AI 대규모 업데이트** | Apple | 서비스 | iOS 26.4와 함께 AI 기반 Siri 대폭 업그레이드 예정. | 업계 보도 |

---

## 3. 변화 속도 분석: 무어의 법칙보다 빠른 가속화

### 연도별 주요 이벤트 수 비교

```
2022년: ██                                          1건
2023년: ██████████████████                          9건
2024년: ██████████████████████████████              15건
2025년: ██████████████████████████████████████████  20건+
2026년: ████████████████████ (3개월)                10건+ (연간 환산 40건+)
```

### 가속화의 핵심 지표

| 지표 | 2023년 | 2024년 | 2025년 | 2026년 (3월 기준) |
|------|--------|--------|--------|-------------------|
| 주요 모델 출시 수 | ~5개 | ~12개 | ~20개 | ~10개 (3개월) |
| 모델 업데이트 주기 | 6~12개월 | 3~6개월 | 1~3개월 | **2~3주** |
| 최대 컨텍스트 윈도우 | 128K 토큰 | 1M 토큰 | 10M 토큰 | 10M+ 토큰 |
| 최대 투자 라운드 | ~수십억 달러 | 66억 달러 | 400억 달러 | 300억 달러 (단일) |
| 경쟁 플레이어 수 | 3사 (OpenAI, Google, Anthropic) | 4사 (+Meta) | 5사 (+xAI) | 6사+ (+DeepSeek 등) |

### 무어의 법칙과의 비교

무어의 법칙은 "18~24개월마다 트랜지스터 수가 2배"라는 관찰이었습니다. 그러나 AI 산업은 이를 훨씬 능가하는 속도로 변화하고 있습니다.

- **모델 성능**: 2023년 GPT-4의 벤치마크 점수가 2025년에는 2~3배 이상 향상되었습니다 (특히 추론, 코딩 영역).
- **비용 효율성**: 동일 성능 기준 API 비용이 매년 5~10배씩 감소하고 있습니다.
- **업데이트 주기**: 2023년에 연간 1~2회였던 메이저 모델 출시가 2026년에는 월 2~3회로 단축되었습니다.
- **투자 규모**: 2023년 수십억 달러 수준이던 AI 투자가 2025년에 수천억 달러 규모로 폭증했습니다.

> **핵심 통찰**: 무어의 법칙이 "2년에 2배"였다면, 생성형 AI 시대는 **"6개월에 세대 교체"**에 가까운 속도로 진행되고 있습니다. 이는 반도체라는 물리적 한계에 영향받는 하드웨어와 달리, 소프트웨어/알고리즘/데이터의 시너지가 만들어낸 결과입니다.

---

## 4. 주요 투자 흐름 요약

| 시기 | 대상 | 금액 | 기업가치 | 주요 투자자 |
|------|------|------|----------|-------------|
| 2024.10 | OpenAI | 66억 달러 | 1,570억 달러 | Thrive Capital, Microsoft, Nvidia |
| 2025.01 | Stargate 프로젝트 | 5,000억 달러 (4년) | - | OpenAI, SoftBank, Oracle, MGX |
| 2025.03 | OpenAI | 400억 달러 | 3,000억 달러 | SoftBank(300억), Microsoft |
| 2025.09 | Anthropic | 130억 달러 | 1,830억 달러 | ICONIQ |
| 2025.10 | OpenAI (직원주식) | 100억 달러 | 5,000억 달러 | 기존 투자자 |
| 2026.02 | Anthropic | 300억 달러 | 3,800억 달러 | 다수 기관투자자 |

---

## 5. 정리: 신입사원이 기억해야 할 5가지

1. **ChatGPT는 시작일 뿐입니다**: 2022년 11월 이후 3년 만에 AI 산업은 완전히 다른 세계가 되었습니다. 단순 챗봇에서 멀티모달, 추론, 에이전트, 영상 생성으로 진화했습니다.

2. **경쟁이 혁신을 만듭니다**: OpenAI 독주 체제에서 Google, Anthropic, Meta, xAI, DeepSeek까지 참여하는 다자 경쟁으로 전환되면서, 모델 성능은 급상승하고 비용은 급락했습니다.

3. **오픈소스가 판을 바꿉니다**: Meta의 LLaMA 시리즈와 DeepSeek R1은 오픈소스 모델도 상용 모델에 필적할 수 있음을 증명했습니다.

4. **규제가 뒤따르고 있습니다**: EU AI Act를 시작으로 각국의 AI 규제 프레임워크가 형성되고 있습니다. AI 개발자라면 규제 동향을 반드시 파악해야 합니다.

5. **변화 속도는 더 빨라집니다**: 2026년 현재, 주요 AI 기업들은 2~3주 간격으로 모델을 업데이트합니다. 이 속도에 적응하는 것이 AI 시대 IT 전문가의 핵심 역량입니다.

---

## 참고 출처

- [OpenAI 공식 블로그](https://openai.com/blog)
- [Anthropic 공식 뉴스](https://www.anthropic.com/news)
- [Google AI 블로그](https://blog.google/technology/ai/)
- [Meta AI 블로그](https://ai.meta.com/blog/)
- [xAI 공식](https://x.ai/news)
- [DeepSeek API Docs](https://api-docs.deepseek.com/news/news250120)
- [EU AI Act 공식](https://artificialintelligenceact.eu/)
- [TechCrunch AI 섹션](https://techcrunch.com/category/artificial-intelligence/)
- [CNBC AI 보도](https://www.cnbc.com)
- [Wikipedia - 2025 in artificial intelligence](https://en.wikipedia.org/wiki/2025_in_artificial_intelligence)
- [KDnuggets - 10 AI Developments That Defined 2025](https://www.kdnuggets.com/the-10-ai-developments-that-defined-2025)
- [TIME - 5 AI Developments That Reshaped 2025](https://time.com/7341939/ai-developments-2025-trump-china/)

---

> **다음 챕터 예고**: 제2장에서는 이 타임라인의 핵심 기술인 **대규모 언어 모델(LLM)의 작동 원리**를 신입사원 눈높이에서 설명합니다. 트랜스포머 아키텍처부터 프롬프트 엔지니어링까지, "왜 이 모델들이 이렇게 똑똑한지"를 이해할 수 있게 됩니다.
