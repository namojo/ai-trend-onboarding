# 제1장. 생성형 AI, 왜 지금 배워야 하는가?

> **핵심 메시지**: 생성형 AI는 더 이상 기술 부서만의 관심사가 아닙니다. 2026년 현재, 전 세계 기업의 88%가 AI를 업무에 활용하고 있으며, AI를 이해하고 활용하는 역량은 모든 직무의 기본 소양이 되었습니다.

---

## 1. 생성형 AI 도입의 필요성 (Why Generative AI)

### 1.1 생성형 AI란 무엇인가?

생성형 AI(Generative AI)란 텍스트, 이미지, 영상, 코드 등 **새로운 콘텐츠를 스스로 만들어내는 인공지능** 기술입니다. 기존 AI가 "이 사진은 고양이인가, 개인가?"를 판별하는 데 집중했다면, 생성형 AI는 "고양이 그림을 그려줘"라는 요청에 직접 그림을 만들어냅니다.

> **쉽게 이해하기**
>
> 생성형 AI를 "매우 똑똑한 신입사원"이라고 생각해보세요. 회사의 문서 양식을 보여주면 비슷한 문서를 작성하고, 기존 보고서를 요약하며, 아이디어 브레인스토밍도 함께 해줍니다. 다만, 가끔 확인이 필요한 실수를 하기도 합니다. 이것을 **환각(Hallucination)** 현상이라고 부릅니다.

### 1.2 숫자로 보는 AI 도입의 당위성

글로벌 컨설팅 기관들의 조사 결과는 생성형 AI 도입이 선택이 아닌 필수임을 보여줍니다.

| 지표 | 수치 | 출처 |
|:---|:---|:---|
| 기업 AI 도입률 (2025) | 88% (1개 이상의 업무에 AI 활용) | [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) |
| 생성형 AI 정기 활용 비율 | 71% | [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) |
| 2026년 기업 GenAI API/앱 사용 전망 | 80% 이상 | [Gartner (2023.10)](https://www.gartner.com/en/newsroom/press-releases/2023-10-11-gartner-says-more-than-80-percent-of-enterprises-will-have-used-generative-ai-apis-or-deployed-generative-ai-enabled-applications-by-2026) |
| 생산성 향상 효과 | 26~55% | [McKinsey / Aristek Systems](https://aristeksystems.com/blog/whats-going-on-with-ai-in-2025-and-beyond/) |
| AI 투자 대비 수익률 (ROI) | $1 투자 시 $3.70 회수 | [McKinsey / Aristek Systems](https://aristeksystems.com/blog/whats-going-on-with-ai-in-2025-and-beyond/) |
| 생성형 AI 시장 규모 (2025) | 713.6억 달러 | [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/generative-ai-market-142870584.html) |
| 생성형 AI 시장 전망 (2032) | 8,905.9억 달러 (CAGR 43.4%) | [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/generative-ai-market-142870584.html) |
| 2026년 AI 에이전트 탑재 기업 앱 비율 | 40% (2025년 5% 미만 대비) | [Gartner (2025.08)](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) |

McKinsey는 생성형 AI가 **16개 비즈니스 기능에 걸쳐 63개 유즈케이스**에서 연간 **2.6조~4.4조 달러(약 3,400조~5,700조 원)** 규모의 경제적 가치를 창출할 수 있다고 분석했습니다.

> **쉽게 이해하기**
>
> "2.6조~4.4조 달러"가 얼마나 큰 금액일까요? 이는 대한민국 GDP(약 1.7조 달러)의 1.5~2.5배에 달하는 규모입니다. 생성형 AI 하나의 기술이 한 국가의 경제 규모만큼의 새로운 가치를 만들어낼 수 있다는 의미입니다.

### 1.3 산업별 주요 유즈케이스와 기대 효과

생성형 AI는 특정 산업에 국한되지 않고 거의 모든 분야에서 활용됩니다.

| 산업 | 주요 유즈케이스 | 기대 효과 |
|:---|:---|:---|
| **제조** | 예측 정비(Predictive Maintenance), AI 품질 검사, 에너지 최적화 | 유지보수 비용 25~40% 절감, 78% 시설에서 폐기물 감소, 에너지 평균 12% 절감 |
| **금융** | 이상거래 탐지, 리스크 분석, 감사 보고서 자동 생성 | 사기 탐지 정밀도 대폭 향상, 컴플라이언스 업무 자동화 |
| **마케팅/영업** | 콘텐츠 자동 생성, 개인화 캠페인, 고객 인사이트 분석 | 직원 1인당 주 11.4시간 절약, 매출 증대 효과 |
| **소프트웨어 개발** | 코드 자동 생성, 테스트 자동화, 문서화 | 개발 생산성 30~50% 향상 |
| **법무/컴플라이언스** | 계약서 검토, 규제 변화 모니터링, 법률 리서치 | 검토 시간 대폭 단축, 리스크 조기 발견 |
| **인사/교육** | 채용 스크리닝, 맞춤형 교육 콘텐츠, 온보딩 자동화 | 채용 프로세스 효율화, 교육 효과 향상 |

> **쉽게 이해하기**
>
> 여러분의 일상 업무에서 생성형 AI는 이렇게 활용됩니다:
> - **이메일 작성**: "거래처에 납기 지연 사과 메일 작성해줘" -> 즉시 초안 생성
> - **보고서 요약**: 30페이지 보고서를 3줄로 요약
> - **데이터 분석**: "지난 분기 매출 데이터에서 트렌드를 찾아줘"
> - **번역/통역**: 해외 파트너와의 커뮤니케이션 지원
> - **회의록 정리**: 녹음된 회의 내용을 자동으로 정리하고 액션 아이템 추출

### 1.4 AI를 배우지 않으면 벌어지는 일

Gartner는 2026년까지 기업 앱의 40%가 AI 에이전트(Agent)를 탑재할 것으로 전망했습니다 (2025년 5% 미만 대비). 이는 곧 우리가 매일 사용하는 업무 도구 자체가 AI 기반으로 전환된다는 뜻입니다.

AI를 활용하는 직원과 그렇지 않은 직원 사이의 **생산성 격차**는 이미 벌어지고 있습니다. McKinsey의 조사에 따르면, AI를 적극 활용하는 상위 6%의 기업은 EBIT(영업이익)에서 5% 이상의 AI 기여 효과를 보고하고 있습니다.

---

## 2. AI 발전 타임라인 (2022.11 ~ 2026.03)

아래 표는 2022년 11월 ChatGPT 출시 이후 현재(2026년 3월)까지의 주요 AI 이정표를 정리한 것입니다.

### 2.1 2022~2023년: 대중화의 시작과 LLM 경쟁의 서막

| 시기 | 주요 사건 | 주체 | 비즈니스적 의미 | 출처 |
|:---|:---|:---|:---|:---|
| 2022.11 | **ChatGPT 출시** | OpenAI | AI 대중화의 기폭제. 출시 2개월 만에 1억 사용자 돌파, 역사상 가장 빠른 성장 | [OpenAI](https://openai.com/blog/chatgpt) |
| 2023.01 | **Microsoft, OpenAI에 100억 달러 투자** | Microsoft | 빅테크의 본격적 AI 투자 경쟁 시작. Azure 클라우드와 AI 통합 가속 | [Reuters](https://www.reuters.com/technology/microsoft-invest-10-billion-openai-2023-01-23/) |
| 2023.02 | **Bing Chat / Google Bard 발표** | Microsoft, Google | 검색 엔진에 AI 대화 기능 통합. 검색 시장의 패러다임 전환 시작 | [Microsoft Blog](https://blogs.microsoft.com/blog/2023/02/07/reinventing-search-with-a-new-ai-powered-microsoft-bing-and-edge-your-copilot-for-the-web/) |
| 2023.03 | **GPT-4 출시** | OpenAI | 멀티모달(텍스트+이미지 입력) 지원. 전문 분야 추론 능력 비약적 향상 | [OpenAI](https://openai.com/index/gpt-4/) |
| 2023.03 | **Claude 출시** | Anthropic | AI 안전성을 강조한 대화형 AI 등장. 기업 시장 경쟁 심화 | [Anthropic](https://www.anthropic.com/news/introducing-claude) |
| 2023.05 | **PaLM 2 발표** | Google | Google의 차세대 LLM. 다국어 지원과 추론 능력 강화 | [Google AI Blog](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/) |
| 2023.07 | **LLaMA 2 오픈소스 공개** | Meta | 오픈소스 LLM 생태계의 본격적 시작. 기업의 자체 AI 구축 가능성 확대 | [Meta AI](https://ai.meta.com/llama/) |
| 2023.07 | **Claude 2 출시** | Anthropic | 10만 토큰 컨텍스트 창 지원. 긴 문서 분석 능력 대폭 향상 | [Anthropic](https://www.anthropic.com/news/claude-2) |
| 2023.09 | **DALL-E 3 출시** | OpenAI | ChatGPT와 통합된 이미지 생성. 텍스트-이미지 생성 품질 도약 | [OpenAI](https://openai.com/index/dall-e-3/) |
| 2023.11 | **OpenAI DevDay** (GPT-4 Turbo, GPTs 스토어, 샘 알트먼 해임-복귀 사태) | OpenAI | 맞춤형 AI 앱(GPTs) 생태계 시작. CEO 해임-복귀로 AI 기업 거버넌스 이슈 부각 | [OpenAI DevDay](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) |
| 2023.12 | **Gemini 1.0 출시** | Google | Google의 새 통합 AI 브랜드. 멀티모달 네이티브 모델로 전환 | [Google DeepMind](https://deepmind.google/technologies/gemini/) |
| 2023.12 | **Mixtral 8x7B 공개** | Mistral AI | 유럽 기반 오픈소스 MoE 모델. GPT-3.5급 성능을 오픈소스로 제공 | [Mistral AI](https://mistral.ai/news/mixtral-of-experts/) |

### 2.2 2024년: 멀티모달의 완성과 추론 AI의 등장

| 시기 | 주요 사건 | 주체 | 비즈니스적 의미 | 출처 |
|:---|:---|:---|:---|:---|
| 2024.02 | **Gemini 1.5 발표** (100만 토큰 컨텍스트) | Google | 초장문 문서 처리 가능. 책 한 권 분량을 한 번에 분석 | [Google DeepMind](https://deepmind.google/technologies/gemini/) |
| 2024.02 | **Sora 공개** | OpenAI | 텍스트에서 고품질 영상 생성. 영상 제작 산업의 혁신 가능성 제시 | [OpenAI](https://openai.com/index/sora/) |
| 2024.03 | **Claude 3 시리즈** (Opus, Sonnet, Haiku) | Anthropic | 성능/비용/속도별 3단계 모델 라인업. 기업 맞춤형 선택지 제공 | [Anthropic](https://www.anthropic.com/news/claude-3-family) |
| 2024.04 | **LLaMA 3 출시** | Meta | 오픈소스 최강 모델. 기업 Private AI 구축의 핵심 기반 | [Meta AI](https://ai.meta.com/blog/meta-llama-3/) |
| 2024.05 | **GPT-4o 출시** (멀티모달 통합) | OpenAI | 텍스트/음성/이미지를 하나의 모델로 통합. 실시간 음성 대화 가능 | [OpenAI](https://openai.com/index/hello-gpt-4o/) |
| 2024.06 | **Claude 3.5 Sonnet 출시** | Anthropic | Opus급 성능을 Sonnet 가격에 제공. 가성비 혁신 | [Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet) |
| 2024.06 | **Apple Intelligence 발표** | Apple | iPhone/Mac에 AI 내장. 온디바이스 AI 시대의 시작 | [Apple](https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/) |
| 2024.08 | **EU AI Act 발효** | EU | 세계 최초 포괄적 AI 규제법. 기업의 AI 거버넌스 체계 구축 필수화 | [EU](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) |
| 2024.09 | **o1-preview 출시** (추론 모델) | OpenAI | "생각하는 AI"의 등장. 복잡한 수학/과학 문제 해결 능력 비약적 향상 | [OpenAI](https://openai.com/index/introducing-openai-o1-preview/) |
| 2024.10 | **Claude 3.5 Sonnet (신규) + Computer Use** | Anthropic | AI가 컴퓨터를 직접 조작 가능. AI 에이전트 시대의 서막 | [Anthropic](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| 2024.12 | **Gemini 2.0 출시** | Google | 에이전트 기능 강화 + 멀티모달 고도화 | [Google DeepMind](https://deepmind.google/technologies/gemini/) |
| 2024.12 | **Sora 정식 출시** | OpenAI | 텍스트-비디오 생성 서비스 상용화 | [OpenAI](https://openai.com/index/sora/) |
| 2024.12 | **DeepSeek V3 출시** | DeepSeek | 중국발 고성능 오픈소스 모델. 저비용 고성능의 새로운 기준 제시 | [DeepSeek](https://www.deepseek.com/) |

### 2.3 2025년: AI 에이전트와 추론 경쟁의 본격화

| 시기 | 주요 사건 | 주체 | 비즈니스적 의미 | 출처 |
|:---|:---|:---|:---|:---|
| 2025.01 | **DeepSeek R1 출시** | DeepSeek | o1급 추론 능력을 파격적 저가에 제공. NVIDIA 주가 17% 급락 촉발. AI 비용 혁신의 상징 | [DeepSeek](https://www.deepseek.com/) |
| 2025.01 | **o3-mini 출시** | OpenAI | 경량 추론 모델. 저비용으로 고급 추론 능력 접근 가능 | [OpenAI](https://openai.com/) |
| 2025.02 | **Claude 3.7 Sonnet 출시** | Anthropic | 확장된 사고(Extended Thinking) 기능 도입. 하이브리드 추론 모델의 시작 | [Anthropic](https://www.anthropic.com/) |
| 2025.02 | **GPT-4.5 출시** | OpenAI | GPT-4 계열의 최종 진화. 대규모 사전학습 모델의 집대성 | [OpenAI](https://openai.com/) |
| 2025.04 | **LLaMA 4 출시** (Scout, Maverick) | Meta | 109B~400B 규모 오픈소스 모델. 에이전트 기능 지원 시작 | [Meta AI](https://ai.meta.com/) |
| 2025.05 | **Claude Opus 4, Sonnet 4 출시** | Anthropic | 세계 최고 수준의 코딩 모델. 장시간 에이전트 워크플로우 지원 | [Anthropic](https://www.anthropic.com/news/claude-4) |
| 2025.08 | **GPT-5 출시** | OpenAI | 차세대 플래그십 모델. 추론/멀티모달/에이전트 통합 | [OpenAI](https://openai.com/) |
| 2025.09~11 | **Claude 4.5 Sonnet/Opus 출시** | Anthropic | 코딩 및 장기 에이전트 작업에 특화된 업그레이드 | [Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5) |
| 2025.11 | **Gemini 3.0 출시** | Google | 100만+ 토큰 지원, 프론티어급 멀티모달 성능 | [Google DeepMind](https://deepmind.google/technologies/gemini/) |
| 2025.11 | **EU AI Act 디지털 옴니버스 제안** | EU | AI법 시행 간소화 및 일정 조정 제안. 기업 컴플라이언스 부담 완화 | [EU](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) |
| 2025.12 | **GPT-5.2 출시** | OpenAI | AIME 2025 100% 달성, 연구급 수학 추론 능력. 6단계 추론 레벨 조절 기능 | [OpenAI](https://openai.com/) |

### 2.4 2026년 1분기: 초경쟁 시대의 도래

| 시기 | 주요 사건 | 주체 | 비즈니스적 의미 | 출처 |
|:---|:---|:---|:---|:---|
| 2026.02 | **Claude Sonnet 5 ("Fennec") 출시** | Anthropic | SWE-Bench 82.1% 달성, 최초로 80% 장벽 돌파. 자율 코딩 에이전트의 새 기준 | [Anthropic](https://www.anthropic.com/) |
| 2026.02 | **Claude Opus 4.6 출시** (1M 컨텍스트) | Anthropic | 100만 토큰 컨텍스트, 에이전트 팀 기능, 파워포인트 통합 | [Anthropic](https://www.anthropic.com/) |
| 2026.02 | **DeepSeek V4 준비** (Engram 아키텍처) | DeepSeek | 정적 메모리/추론 분리. 100만+ 토큰을 50% 낮은 비용으로 처리 | [DeepSeek](https://www.deepseek.com/) |
| 2026.02 | **Gemini 3.1 Pro 출시** | Google | ARC-AGI-2 77.1%, 16개 벤치마크 중 13개에서 1위. 가격 동결로 가성비 극대화 | [Google DeepMind](https://deepmind.google/technologies/gemini/) |
| 2026.03 | **Q1 2026: 271+ 신규 모델 출시** | 다수 | 하루 평균 3개의 새 AI 모델 등장. 특화 모델(sLLM) 시대 본격화 | [LLM Stats](https://llm-stats.com/llm-updates) |

> **쉽게 이해하기**
>
> **컨텍스트 창(Context Window)** 이란 AI가 한 번에 읽고 이해할 수 있는 정보의 양입니다.
> - 2023년 초: ~4,000 토큰 = A4 약 3페이지
> - 2024년 초: ~100,000 토큰 = 소설 1권
> - 2026년 현재: ~1,000,000 토큰 = 소설 약 10권
>
> 이는 AI에게 방대한 문서를 한꺼번에 넘기고 분석을 요청할 수 있게 되었다는 뜻입니다.

---

## 3. 분기별 트렌드 요약

### 3.1 2023년: "LLM의 폭발적 성장과 모델 성능 경쟁"

2023년은 생성형 AI의 원년이라 할 수 있습니다. ChatGPT의 등장 이후 빅테크 기업들이 일제히 자체 LLM(Large Language Model, 거대언어모델)을 출시하며 치열한 경쟁이 시작되었습니다.

**핵심 키워드**: LLM 경쟁, 오픈소스 생태계 시작, GPTs 플랫폼

- **빅테크 전면전**: OpenAI(GPT-4), Google(PaLM 2, Gemini), Anthropic(Claude), Meta(LLaMA 2)가 모두 주력 모델을 공개
- **오픈소스 혁명**: Meta의 LLaMA 2 오픈소스 공개로 중소기업과 스타트업도 자체 AI 모델 구축 가능
- **플랫폼화**: OpenAI의 GPTs 스토어를 통해 비개발자도 맞춤형 AI 앱을 만드는 시대 도래
- **거버넌스 이슈**: 샘 알트먼 해임-복귀 사태로 AI 기업의 안전성 vs 상업성 논쟁 촉발

### 3.2 2024년: "멀티모달의 완성과 온디바이스 AI의 서막"

2024년은 AI가 텍스트를 넘어 **이미지, 음성, 영상을 모두 이해하고 생성하는 멀티모달(Multimodal)** 시대로 진입한 해입니다. 동시에, AI가 클라우드가 아닌 개인 기기에서 직접 구동되는 **온디바이스(On-device) AI**의 막이 올랐습니다.

**핵심 키워드**: 멀티모달, 온디바이스 AI, 추론 모델, AI 규제

- **멀티모달 통합**: GPT-4o가 텍스트/음성/이미지를 하나의 모델로 처리. "보고, 듣고, 말하는" AI의 실현
- **온디바이스 AI**: Apple Intelligence가 iPhone에 AI를 내장. 개인 데이터가 기기를 떠나지 않는 프라이버시 보호형 AI
- **추론(Reasoning) AI의 탄생**: OpenAI o1이 "생각하는 시간"을 도입. 단순 패턴 매칭을 넘어 논리적 추론 가능
- **AI 에이전트의 시작**: Claude의 Computer Use 기능으로 AI가 컴퓨터를 직접 조작하는 시대 시작
- **글로벌 규제 본격화**: EU AI Act 발효(2024.08)로 세계 최초 포괄적 AI 규제 체계 가동

> **쉽게 이해하기**
>
> **멀티모달(Multimodal)** 이란 AI가 여러 종류의 정보(텍스트, 이미지, 음성, 영상)를 동시에 이해하고 처리하는 능력입니다. 예를 들어, 제품 사진을 보여주면서 "이 제품의 마케팅 문구를 작성해줘"라고 요청할 수 있습니다.

### 3.3 2025년: "AI 에이전트 기반 업무 자동화와 sLLM 확산"

2025년은 AI가 단순 "질문-답변" 도구에서 **자율적으로 여러 단계의 작업을 수행하는 에이전트(Agent)** 로 진화한 해입니다. 동시에 특정 산업이나 업무에 특화된 소규모 언어모델(sLLM, small Large Language Model)이 확산되었습니다.

**핵심 키워드**: AI 에이전트, 멀티모델 전략, sLLM, 비용 혁신

- **AI 에이전트의 시대**: Claude Opus 4의 장시간 에이전트 워크플로우, GPT-5의 에이전트 통합 등 자율 업무 처리 AI 등장
- **DeepSeek 충격**: DeepSeek R1이 OpenAI o1급 성능을 파격적 저가에 제공하며 AI 비용 구조를 재편. NVIDIA 주가 17% 급락
- **멀티모델 전략**: 기업들이 단일 AI가 아닌 복수 모델을 용도별로 조합하는 전략 채택 (복잡한 추론은 GPT-5, 코딩은 Claude, 멀티모달은 Gemini, 대량 처리는 DeepSeek)
- **추론 레벨 조절**: GPT-5.2의 6단계 추론 레벨처럼, 작업 복잡도에 따라 AI의 "생각 깊이"를 조절하는 기능 보편화

### 3.4 2026년 현재: "초경쟁과 특화의 시대"

2026년 1분기만으로도 271개 이상의 새로운 AI 모델이 출시되었습니다. 하루 평균 3개의 AI 모델이 나오는 속도입니다. 이제 경쟁은 "누가 더 큰 모델을 만드는가"에서 **"누가 더 실용적인 AI를 만드는가"** 로 이동하고 있습니다.

**핵심 키워드**: 1M 컨텍스트, 에이전트 팀, 업무 특화 모델, AI 통합

- **100만 토큰 시대**: Claude Opus 4.6, Gemini 3.1 등 주요 모델이 100만 토큰 컨텍스트를 지원하며 대규모 문서 분석이 일상화
- **AI 에이전트 팀**: 단일 AI가 아닌 여러 AI 에이전트가 협업하여 복잡한 프로젝트를 수행하는 구조 등장
- **업무 도구 완전 통합**: 파워포인트, 엑셀, 이메일 등 일상 업무 도구에 AI가 기본 내장
- **벤치마크 경쟁 가속**: SWE-Bench 80% 돌파(Claude Sonnet 5), ARC-AGI-2 77.1%(Gemini 3.1) 등 AI 능력이 매월 새로운 기록 경신

---

## 4. 핵심 용어 정리

| 용어 | 영문 | 설명 |
|:---|:---|:---|
| 거대언어모델 | LLM (Large Language Model) | 방대한 텍스트 데이터로 학습하여 인간처럼 글을 읽고 쓸 수 있는 AI 모델 |
| 멀티모달 | Multimodal | 텍스트, 이미지, 음성, 영상 등 여러 종류의 정보를 동시에 처리하는 능력 |
| 환각 | Hallucination | AI가 사실이 아닌 내용을 마치 사실인 것처럼 생성하는 현상 |
| 토큰 | Token | AI가 텍스트를 처리하는 최소 단위. 한국어 기준 약 1글자 = 1~2토큰 |
| 컨텍스트 창 | Context Window | AI가 한 번에 읽고 기억할 수 있는 정보의 최대 분량 |
| 프롬프트 | Prompt | AI에게 주는 지시문이나 질문 |
| AI 에이전트 | AI Agent | 사람의 개입 없이 자율적으로 여러 단계의 작업을 수행하는 AI |
| 온디바이스 AI | On-device AI | 클라우드 서버가 아닌 스마트폰이나 PC 등 개인 기기에서 직접 작동하는 AI |
| 파인튜닝 | Fine-tuning | 범용 AI 모델을 특정 업무나 산업에 맞게 추가 학습시키는 과정 |
| sLLM | small LLM | 특정 업무에 특화된 소규모 언어모델. 비용 효율적이며 기업 맞춤 배포 가능 |
| MoE | Mixture of Experts | 여러 전문가 모델을 조합하여 효율성을 높이는 AI 아키텍처 |
| RAG | Retrieval-Augmented Generation | 외부 데이터를 검색하여 AI 답변의 정확도를 높이는 기술 |

---

## 5. 정리: 지금 시작해야 하는 이유

### 기업 관점
- 2026년 생성형 AI 시장은 **713억 달러**를 넘어서며 폭발적으로 성장 중
- AI 도입 기업은 평균 **26~55%의 생산성 향상**과 **$1당 $3.70의 ROI**를 달성
- Gartner는 2026년까지 기업 앱의 **40%가 AI 에이전트**를 탑재할 것으로 전망

### 개인 관점
- AI는 더 이상 "알면 좋은 기술"이 아니라 **"모르면 뒤처지는 기본 역량"**
- AI를 활용하는 직원과 그렇지 않은 직원의 생산성 격차는 이미 **26~55%** 수준
- AI와 협업하는 능력은 디지털 시대의 **새로운 리터러시(문해력)**

> **한 줄 요약**: 생성형 AI는 엑셀이 수기 계산을 대체했듯, 지식 노동의 방식을 근본적으로 바꾸고 있습니다. 지금 배우기 시작하면 변화를 주도할 수 있고, 미루면 변화에 끌려갈 수밖에 없습니다.

---

*본 자료의 정보는 2026년 3월 18일 기준으로 작성되었습니다.*

**주요 출처:**
- [McKinsey - The State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [McKinsey - The Economic Potential of Generative AI](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier)
- [Gartner - GenAI Enterprise Adoption Forecast](https://www.gartner.com/en/newsroom/press-releases/2023-10-11-gartner-says-more-than-80-percent-of-enterprises-will-have-used-generative-ai-apis-or-deployed-generative-ai-enabled-applications-by-2026)
- [Gartner - AI Agent Prediction 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
- [MarketsandMarkets - Generative AI Market](https://www.marketsandmarkets.com/Market-Reports/generative-ai-market-142870584.html)
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [LLM Stats - AI Model Updates](https://llm-stats.com/llm-updates)
