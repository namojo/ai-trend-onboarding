# 제2장: AI 기술 트렌드와 서비스 생태계

> **학습 목표**: 현재 AI 기술의 전체 지형을 이해하고, "범용 모델"과 "응용 서비스"의 차이를 구분할 수 있다.
> 각 서비스가 어떤 모델을 기반으로 동작하는지 파악하여, 업무에 적합한 도구를 선택하는 안목을 기른다.

---

## 2.1 범용 모델과 응용 서비스 -- 무엇이 다른가?

AI 뉴스를 보면 "GPT-5", "Claude 4", "Cursor", "Copilot" 같은 이름이 쏟아집니다. 이것들을 한 줄로 이해하려면 **범용 모델(Foundation Model)**과 **응용 서비스(Application Service)**를 구분하는 것이 핵심입니다.

---

> **쉽게 이해하기 -- "엔진과 자동차"**
>
> 범용 모델은 자동차의 **엔진**에 해당합니다. 엔진 자체로는 운전할 수 없지만, 성능의 핵심을 결정합니다.
> 응용 서비스는 그 엔진을 장착한 **완성차**입니다. 운전대, 좌석, 내비게이션이 붙어 있어 누구나 탈 수 있습니다.
>
> 예를 들어, **Claude Opus 4.5**는 엔진이고, 이 엔진을 탑재한 **Cursor**는 코딩용 완성차입니다.

---

- **범용 모델(Foundation Model)**: OpenAI, Anthropic, Google 같은 회사가 만드는 거대한 AI 두뇌. 텍스트, 이미지, 영상 등을 생성하는 핵심 능력을 가지며, API(Application Programming Interface, 프로그램 간 통신 규약)로 다른 서비스에 제공됩니다.
- **응용 서비스(Application Service)**: 범용 모델을 활용하여 특정 업무 문제를 해결하는 최종 제품. 사용자 인터페이스, 워크플로우, 데이터 연동 등이 추가되어 비전문가도 쉽게 사용할 수 있습니다.

---

## 2.2 범용 모델 (Foundation Models) 전체 지도

### 2.2.1 텍스트 생성 모델

2023년 ChatGPT의 등장 이후, 텍스트 생성 모델은 매 분기마다 성능이 급등하고 있습니다. 2025~2026년 현재, 주요 모델은 다음과 같습니다.

| 모델명 | 제공사 | 출시 시기 | 주요 특징 | 참고 가격(API 입력 기준) |
|--------|--------|-----------|-----------|------------------------|
| GPT-4o | OpenAI | 2024.05 | 텍스트+이미지+음성 통합 멀티모달, 빠른 응답 속도 | $2.50 / 1M 토큰 |
| GPT-4.5 | OpenAI | 2025.02 | 감성 지능 향상, 환각(Hallucination) 대폭 감소 | $75 / 1M 토큰 |
| GPT-5.2 | OpenAI | 2025.12 | AIME 100% 달성, 400K 컨텍스트 윈도우 | 비공개 |
| Claude 3.5 Sonnet | Anthropic | 2024.06 | 코딩 특화, 안전성 강조, 합리적 가격 | $3 / 1M 토큰 |
| Claude 3.7 Sonnet | Anthropic | 2025.02 | 확장 사고(Extended Thinking) 도입 | $3 / 1M 토큰 |
| Claude Opus 4.5 | Anthropic | 2025.12 | SWE-bench 80.9%, 최고 수준 코딩 성능 | $15 / 1M 토큰 |
| Claude Sonnet 5 "Fennec" | Anthropic | 2026.02 | SWE-bench 82.1%, 최초 80% 돌파 모델 | 추정 $3~5 / 1M 토큰 |
| Gemini 2.0 Flash | Google | 2025.02 | 빠른 속도, 멀티모달, 에이전트 기능 내장 | $0.10 / 1M 토큰 |
| Gemini 2.5 Pro | Google | 2025.03 | 100만 토큰 컨텍스트, 추론 강화 | $1.25 / 1M 토큰 |
| Gemini 3 Pro | Google | 2025.11 | 멀티모달 리더, Flash 버전 동시 출시 | 비공개 |
| LLaMA 3.1 405B | Meta | 2024.07 | 오픈소스(Open Source) 최대 규모 | 무료 (자체 운영 시) |
| LLaMA 4 Maverick | Meta | 2025.12 | 400B MoE, 오픈 가중치(Open Weights) | 무료 (자체 운영 시) |
| DeepSeek R1 | DeepSeek | 2025.01 | 순수 강화학습 기반 추론, 훈련비 $5.9M | 무료 (오픈소스) |
| DeepSeek V3.2 | DeepSeek | 2025.09 | 671B MoE, 추론+에이전트 워크로드 최적화 | 매우 저렴 |
| Grok 3 | xAI | 2025.02 | 실시간 X(구 트위터) 데이터 활용 | 비공개 |

> **쉽게 이해하기 -- "MoE(Mixture of Experts)란?"**
>
> MoE는 "전문가 혼합" 구조입니다. 671억 개의 매개변수(Parameter)를 가진 모델이라도,
> 한 번의 질문에는 370억 개만 활성화됩니다. 마치 대형 병원에 100명의 전문의가 있지만,
> 환자 한 명에게는 해당 분야 전문의 몇 명만 진료하는 것과 같습니다.
> 이 덕분에 모델이 크지만 빠르고 저렴하게 운영할 수 있습니다.

#### DeepSeek 쇼크 -- 오픈소스의 역습 (2025.01)

2025년 1월, 중국의 DeepSeek이 R1 모델을 공개했을 때 업계는 큰 충격을 받았습니다. 훈련 비용이 약 590만 달러(약 80억 원)에 불과하면서도, 수천억 원을 투자한 폐쇄형 모델과 대등한 추론 성능을 보여주었기 때문입니다. 이후 DeepSeek, Qwen, Mistral 등 5개 독립 오픈 모델 계열이 동시에 최전선(Frontier) 품질에 도달하면서, 오픈소스 AI 모델의 기업 도입이 급격히 늘어났습니다.

---

### 2.2.2 이미지 생성 모델

| 모델명 | 제공사 | 출시 시기 | 주요 특징 | 가격 |
|--------|--------|-----------|-----------|------|
| DALL-E 3 | OpenAI | 2023.10 | ChatGPT 통합, 텍스트 렌더링 우수 | ChatGPT Plus 포함 ($20/월) |
| GPT-4o 이미지 생성 | OpenAI | 2025.03 | GPT-4o 네이티브 이미지 생성, "지브리풍" 열풍 | ChatGPT Plus 포함 |
| Midjourney v7 | Midjourney | 2025.04 | 예술적 품질 최고, 시네마틱 감성 | $10~60/월 |
| Stable Diffusion 3.5 | Stability AI | 2025.하반기 | 오픈소스, 80억 파라미터, 1MP 해상도 | 무료 (자체 운영 시) |
| Flux 1.1 Pro | Black Forest Labs | 2025 | 사실주의 최강, 4.5초 생성, 기업가치 $3.25B | API 종량제 |
| Imagen 3 | Google | 2025 | Gemini 통합, 사실적 이미지 | Gemini 구독 포함 |

> **쉽게 이해하기 -- "오픈소스(Open Source)란?"**
>
> 오픈소스란 소프트웨어의 설계도(소스 코드)를 누구나 볼 수 있도록 공개하는 방식입니다.
> 무료로 사용할 수 있고, 기업이 자체 서버에서 운영할 수 있어 데이터 보안에 유리합니다.
> 반대로, OpenAI의 GPT나 Anthropic의 Claude처럼 코드를 공개하지 않는 방식을
> **폐쇄형(Closed Source / Proprietary)** 모델이라 합니다.

---

### 2.2.3 영상 생성 모델

2026년은 AI 영상 생성이 대중화된 원년입니다. 네이티브 오디오(자동 소리 생성), 립싱크(입 모양 동기화), 4K 해상도가 표준이 되었습니다.

| 모델명 | 제공사 | 출시 시기 | 주요 특징 | 가격 |
|--------|--------|-----------|-----------|------|
| Sora 2 | OpenAI | 2025.12 | 물리 법칙 준수, 최대 25초, 시네마틱 품질 | ChatGPT Plus $20/월, Pro $200/월 |
| Veo 3.1 | Google DeepMind | 2026.01 | 네이티브 4K, 수직 영상, 참조 이미지 4장 활용 | Vertex AI 종량제 |
| Kling 3.0 | Kuaishou (중국) | 2026.02 | 멀티샷(3~15초), 캐릭터 일관성, 4K | 구독제, MAU 1,200만, ARR $240M |
| Runway Gen-3 Alpha | Runway | 2024.06 | 크리에이터 중심, 모션 브러시 기능 | $12~76/월 |

---

### 2.2.4 음성 및 음악 생성 모델

| 모델명 | 제공사 | 출시 시기 | 주요 특징 | 비즈니스 규모 |
|--------|--------|-----------|-----------|--------------|
| ElevenLabs | ElevenLabs | 2023~ | 음성 합성(TTS/Voice Cloning) 선두, 기업가치 $11B | ARR $330M, $781M 투자 유치 |
| Eleven Music | ElevenLabs | 2025.08 | 음악 생성, Kobalt/Merlin 라이선스 확보 | 위 ElevenLabs에 포함 |
| Suno v5 | Suno | 2025.하반기 | 텍스트-투-음악, 보컬 품질 대폭 향상 | 1억 사용자, 기업가치 $2.4B+ |
| Udio | Udio | 2024~ | 음악 생성, UMG/WMG 라이선스 합의 (2025.10~11) | 비공개 |

---

### 2.2.5 추론 특화 모델 (Reasoning Models)

> **쉽게 이해하기 -- "추론 모델이란?"**
>
> 일반 AI 모델이 "직감적으로" 답을 내놓는다면, 추론 모델은 "생각하는 시간"을 갖습니다.
> 마치 수학 문제를 풀 때 풀이 과정을 단계별로 적어가며 푸는 것처럼,
> 모델이 내부적으로 사고 과정(Chain of Thought)을 거친 뒤 답을 제시합니다.
> 복잡한 코딩, 수학, 논리 문제에서 월등한 성능을 보입니다.

| 모델명 | 제공사 | 출시 시기 | 주요 특징 |
|--------|--------|-----------|-----------|
| o1 | OpenAI | 2024.09 | 최초의 상용 추론 모델, 수학/코딩 벤치마크 대폭 향상 |
| o3 | OpenAI | 2025.01 | o1 후속, ARC-AGI 벤치마크 돌파 |
| Claude 3.7 Sonnet (Extended Thinking) | Anthropic | 2025.02 | 확장 사고 모드, 사고 과정 투명 공개 |
| DeepSeek R1 | DeepSeek | 2025.01 | 순수 강화학습 추론, 오픈소스 |
| Gemini 2.5 Pro (Thinking) | Google | 2025.03 | 네이티브 추론 + 100만 토큰 컨텍스트 |

---

## 2.3 응용 서비스 (Application Services) 전체 지도

범용 모델이 "엔진"이라면, 응용 서비스는 특정 업무에 최적화된 "완성 제품"입니다. 같은 모델을 사용하더라도, 서비스마다 사용자 경험과 기능이 크게 다릅니다.

### 2.3.1 AI 코딩 도구

AI 코딩 도구 시장은 2025년 40~50억 달러에서 2027년 120~150억 달러로 3배 성장이 예상됩니다.

| 서비스명 | 기반 모델 | 출시 시기 | 주요 기능 | 가격 | 사용자/매출 |
|----------|----------|-----------|-----------|------|------------|
| GitHub Copilot | GPT-4o, Claude 3.5 Sonnet | 2022~ (지속 업데이트) | IDE 플러그인, 코드 자동완성, 채팅 | $10~39/월 | 470만 유료 구독자, 시장 점유율 42% |
| Cursor | Claude Opus 4.5, GPT-4o 등 | 2023~ | AI 네이티브 에디터, 에이전트 모드 | $20/월 | ARR $2B, 기업가치 $29.3B |
| Claude Code | Claude Opus 4.5/Sonnet 5 | 2025.02~ | 터미널 기반 에이전트, 코드베이스 이해 | API 종량제 | Anthropic 공식 도구 |
| Windsurf | 다중 모델 지원 | 2024~ | AI 네이티브 에디터, Cascade 에이전트 | $15/월 | 비공개 |
| Replit Agent | 다중 모델 | 2024~ | 브라우저 기반, 앱 전체 자동 생성 | $25/월 | 비공개 |

> **쉽게 이해하기 -- "에이전트(Agent) 모드란?"**
>
> 기존 AI 코딩 도구는 "한 줄씩" 코드를 제안했습니다.
> 에이전트 모드는 AI가 스스로 파일을 만들고, 수정하고, 테스트를 실행하며,
> 오류가 나면 자동으로 고치는 **자율적 작업 방식**입니다.
> 사람이 지시만 하면 AI가 여러 단계를 혼자 수행합니다.

---

### 2.3.2 AI 검색 서비스

기존 검색 엔진이 "링크 목록"을 보여주었다면, AI 검색은 질문에 대한 **직접 답변**을 출처와 함께 제공합니다.

| 서비스명 | 기반 모델 | 출시 시기 | 주요 기능 | 가격 |
|----------|----------|-----------|-----------|------|
| Perplexity AI | Claude, GPT, 자체 모델 혼합 | 2023~ | AI 기반 답변 + 출처 인용, Pro Search | 무료 / Pro $20/월 |
| ChatGPT Search | GPT-4o | 2024.10 | ChatGPT 내 실시간 웹 검색 통합 | ChatGPT Plus 포함 |
| Gemini Search (AI Overviews) | Gemini | 2024~ | Google 검색 결과 상단에 AI 요약 | 무료 |

---

### 2.3.3 AI 에이전트 (Autonomous Agents)

2025~2026년 AI 업계의 가장 큰 화두는 **에이전트(Agent)**입니다. Fortune Business Insights에 따르면, 글로벌 에이전트 AI 시장은 2026년 91.4억 달러에서 2034년 1,390억 달러로 성장할 전망입니다.

| 서비스명 | 기반 모델 | 출시 시기 | 주요 기능 | 비고 |
|----------|----------|-----------|-----------|------|
| Devin | 자체 모델 + Claude | 2024.03 발표 | 최초의 AI 소프트웨어 엔지니어, 자율 코딩 | Cognition AI, 기업가치 $2B+ |
| Manus | 자체 모델 | 2025.03 발표 | 범용 AI 에이전트, 웹 탐색+코딩+분석 | 2025.12 Meta에 $2~3B에 인수 |
| Perplexity Computer | Claude Opus 4.6, Gemini, Grok, GPT-5.2 | 2026.02 | 연구+코딩+배포 통합 에이전트 | 작업별 최적 모델 자동 선택 |
| Claude Agent SDK | Claude Opus 4.5+ | 2025.09 (SDK 출시) | 자율 에이전트 구축 프레임워크 | Python/Node.js SDK |
| CrewAI | 다중 모델 | 2024~ | 멀티 에이전트 오케스트레이션 프레임워크 | 오픈소스 |

---

### 2.3.4 AI 디자인 도구

| 서비스명 | 기반 모델 | 출시 시기 | 주요 기능 | 가격 |
|----------|----------|-----------|-----------|------|
| v0 | 자체 모델 + Claude/GPT | 2023~ | 텍스트 -> React UI 컴포넌트 자동 생성 | 무료~$30/월 |
| Figma AI (Figma Make) | 자체 모델 | Config 2025 발표 | 레이아웃 제안, 컴포넌트 자동 생성 | Figma 구독에 포함 |
| Canva AI | 다중 모델 | 2023~ | 편집 가능 레이어 생성, 3D 오브젝트 | 무료~$15/월 |

---

### 2.3.5 기업용 AI 도구 (Enterprise AI)

| 서비스명 | 기반 모델 | 출시 시기 | 주요 기능 | 가격 | 도입 현황 |
|----------|----------|-----------|-----------|------|----------|
| Microsoft 365 Copilot | GPT-4o 기반 | 2023.11~ | Word/Excel/PPT/Outlook/Teams AI 통합 | $30/월 (E7 번들 $99/월) | Fortune 500 중 70% 도입, 1,500만 유료 시트 |
| Notion AI | Claude 기반 | 2023~ | 문서 요약, 자동 작성, 프로젝트 계획 | $10/월 추가 | Notion 사용자 대상 |
| Slack AI | 다중 모델 | 2024~ | 채널 요약, 스레드 검색, 답변 제안 | Enterprise Grid 포함 | Salesforce 생태계 |

---

## 2.4 모델-서비스 매핑 테이블 (핵심 정리)

아래 표는 주요 응용 서비스가 어떤 범용 모델을 어떤 방식으로 활용하는지 한눈에 보여줍니다.

| 응용 서비스 | 기반 모델 | 활용 방식 | 출시일 | 비즈니스 효과 |
|------------|----------|----------|--------|--------------|
| GitHub Copilot | GPT-4o, Claude 3.5 Sonnet | 코드 자동완성 + 채팅 + 에이전트 | 2022~ | 470만 유료 구독자, 시장 점유율 42% |
| Cursor | Claude Opus 4.5, GPT-4o | AI 네이티브 에디터, 에이전트 모드 | 2023~ | ARR $2B, 기업가치 $29.3B |
| Claude Code | Claude Opus 4.5, Sonnet 5 | 터미널 에이전트, 코드베이스 전체 이해 | 2025.02 | Anthropic 핵심 제품 |
| Perplexity AI | Claude, GPT, Gemini 혼합 | RAG 기반 AI 검색, 출처 자동 인용 | 2023~ | 구독형 + 광고, 급성장 |
| Perplexity Computer | Claude Opus 4.6, Gemini, Grok, GPT-5.2 | 작업별 최적 모델 자동 선택 에이전트 | 2026.02 | 연구~배포 전 과정 자동화 |
| Devin | 자체 + Claude | 자율 소프트웨어 개발 에이전트 | 2024.03 | 기업가치 $2B+ |
| Manus | 자체 모델 | 범용 에이전트 (웹+코드+분석) | 2025.03 | Meta에 $2~3B 인수 |
| Microsoft 365 Copilot | GPT-4o 기반 커스텀 | Office 앱 내 AI 어시스턴트 | 2023.11 | Fortune 500 70% 도입, 1,500만 시트 |
| v0 (Vercel) | 자체 + Claude/GPT | 텍스트 -> React UI 생성 | 2023~ | 프론트엔드 개발 자동화 |
| Kling 3.0 | 자체 영상 모델 | 텍스트/이미지 -> 4K 영상 | 2026.02 | MAU 1,200만, ARR $240M |
| ElevenLabs | 자체 음성 모델 | 음성 합성, 음성 클로닝, 더빙 | 2023~ | ARR $330M, 기업가치 $11B |
| Suno v5 | 자체 음악 모델 | 텍스트 -> 풀 트랙 음악 생성 | 2025 | 1억 사용자, 기업가치 $2.4B+ |

---

## 2.5 카테고리별 경쟁 구도 요약

### AI 코딩 도구 -- "3강 구도"

```
GitHub Copilot (42% 점유율, 470만 유료)
       vs.
Cursor (18% 점유율, ARR $2B, 가장 빠른 성장)
       vs.
Windsurf / Claude Code / Replit (나머지 시장 쟁탈)
```

- **핵심 경쟁 축**: IDE 통합 vs. AI 네이티브 에디터 vs. 터미널 에이전트
- **시장 전망**: 2025년 $4~5B에서 2027년 $12~15B으로 3배 성장 예상
- **주목할 점**: Cursor는 24개월 만에 ARR $1B을 달성한 역대 가장 빠른 SaaS(Software as a Service) 기업 중 하나

### AI 검색 -- "전통 검색 vs. AI 네이티브"

```
Google (AI Overviews로 방어)
       vs.
Perplexity (AI 네이티브 검색의 선두)
       vs.
ChatGPT Search (OpenAI의 검색 진출)
```

- **핵심 변화**: 10개의 파란 링크 -> 하나의 종합 답변 + 출처
- **기업 시사점**: 마케팅/SEO 전략의 근본적 변화 필요

### AI 에이전트 -- "2026년의 가장 뜨거운 키워드"

```
Perplexity Computer (멀티모델 통합)
       vs.
Devin / Manus (자율 소프트웨어 개발)
       vs.
Claude Agent SDK / CrewAI (에이전트 구축 프레임워크)
       vs.
Microsoft Copilot Studio (기업 에이전트 플랫폼)
```

- **시장 규모**: 2026년 $9.1B에서 2034년 $139B (CAGR 40%+)
- **기업 시사점**: 100% 기업이 에이전트 AI 확대 계획 (CrewAI 설문, 2026.02)

### AI 영상 생성 -- "4강 대전"

```
Sora 2 (OpenAI, 시네마틱 물리 표현)
       vs.
Veo 3.1 (Google, 4K 네이티브, 전문 촬영 품질)
       vs.
Kling 3.0 (Kuaishou, 멀티샷, 가장 빠른 상용화)
       vs.
Runway Gen-3 (크리에이터 중심, 모션 제어)
```

- **핵심 변화**: 텍스트만으로 오디오 포함 영상 생성이 가능해짐
- **기업 시사점**: 마케팅 영상, 교육 콘텐츠 제작 비용 대폭 절감 가능

### 기업용 AI -- "Microsoft의 독주, 도전자 출현"

```
Microsoft 365 Copilot (Fortune 500 중 70% 도입)
       vs.
Google Workspace + Gemini
       vs.
Notion AI / Slack AI (특화 도구)
```

- **가격 변화**: Microsoft가 E7 번들($99/월)을 출시하며, AI를 기본 탑재 전략으로 전환
- **기업 시사점**: AI 도구 비용이 기존 소프트웨어 예산에 추가되는 것이 아니라, 기존 구독에 통합되는 추세

---

## 2.6 핵심 트렌드 5가지

### 1. 모델의 범용화(Commoditization)
2025년 하반기부터 5개 이상의 독립적인 오픈소스 모델 계열(DeepSeek, Qwen, LLaMA, Mistral, GLM)이 동시에 최전선 성능에 도달했습니다. 이제 "어떤 모델을 쓰느냐"보다 "어떻게 활용하느냐"가 더 중요해졌습니다.

### 2. 에이전트(Agent)의 부상
단순 질문-답변을 넘어, AI가 여러 단계의 작업을 자율적으로 수행하는 에이전트 패러다임이 확산되고 있습니다. Perplexity Computer처럼 여러 모델을 작업별로 자동 선택하는 "멀티모델 에이전트"가 등장했습니다.

### 3. 멀티모달(Multimodal)의 기본화
텍스트, 이미지, 영상, 음성을 하나의 모델에서 처리하는 것이 표준이 되었습니다. GPT-4o가 2024년 이 흐름을 열었고, 2026년에는 거의 모든 주요 모델이 멀티모달을 기본 지원합니다.

### 4. AI 코딩의 폭발적 성장
Cursor가 24개월 만에 ARR $1B을 달성한 것은 AI 코딩 도구에 대한 수요가 폭발적임을 보여줍니다. 개발자뿐 아니라 비개발자도 AI를 통해 간단한 프로그램을 만들 수 있는 "바이브 코딩(Vibe Coding)" 시대가 열리고 있습니다.

### 5. 기업 AI 도입의 가속화
Microsoft 365 Copilot이 Fortune 500의 70%에 도입되었고, 기업 AI 시장은 연 45% 이상 성장하고 있습니다. AI가 선택이 아닌 필수로 전환되는 시점입니다.

---

## 2.7 기업 임직원을 위한 시사점

| 구분 | 시사점 | 구체적 행동 |
|------|--------|------------|
| 문서 업무 | Microsoft 365 Copilot으로 보고서 초안, 데이터 분석 자동화 | Copilot 기본 기능 학습, 프롬프트 작성법 익히기 |
| 정보 검색 | Perplexity, ChatGPT 검색으로 리서치 시간 단축 | AI 검색 + 기존 검색 병행, 출처 확인 습관화 |
| 콘텐츠 제작 | Canva AI, Midjourney로 마케팅 이미지 생성 | 저작권 정책 확인, 브랜드 가이드라인 준수 |
| 영상 제작 | Sora, Kling으로 교육/마케팅 영상 초안 생성 | 내부 콘텐츠부터 시범 적용, 품질 검수 프로세스 마련 |
| 코딩/자동화 | Cursor, Claude Code로 간단한 자동화 도구 제작 | "바이브 코딩" 체험, IT 부서와 협업 |

---

## 용어 사전 (Glossary)

| 용어 | 영문 | 설명 |
|------|------|------|
| 범용 모델 | Foundation Model | AI 서비스의 핵심 엔진이 되는 거대 AI 모델 |
| 응용 서비스 | Application Service | 범용 모델을 활용하여 특정 문제를 해결하는 최종 제품 |
| 멀티모달 | Multimodal | 텍스트, 이미지, 음성 등 여러 유형의 데이터를 함께 처리하는 능력 |
| MoE | Mixture of Experts | 모델의 일부 파라미터만 활성화하여 효율적으로 운영하는 아키텍처 |
| 에이전트 | Agent | 여러 단계의 작업을 자율적으로 계획하고 수행하는 AI 시스템 |
| 추론 모델 | Reasoning Model | 내부 사고 과정을 거쳐 복잡한 문제를 풀어내는 AI 모델 |
| RAG | Retrieval-Augmented Generation | 외부 데이터를 검색하여 답변 생성에 활용하는 기법 |
| API | Application Programming Interface | 프로그램 간 통신을 위한 인터페이스 규약 |
| ARR | Annual Recurring Revenue | 연간 반복 매출, SaaS 기업의 핵심 성과 지표 |
| SaaS | Software as a Service | 인터넷을 통해 소프트웨어를 구독형으로 제공하는 방식 |
| 토큰 | Token | AI 모델이 텍스트를 처리하는 최소 단위 (대략 영어 단어 0.75개) |
| 오픈소스 | Open Source | 소스 코드를 공개하여 누구나 사용/수정할 수 있는 소프트웨어 |
| 바이브 코딩 | Vibe Coding | AI에게 자연어로 지시하여 프로그램을 만드는 방식 |
| 컨텍스트 윈도우 | Context Window | AI 모델이 한 번에 처리할 수 있는 텍스트의 최대 길이 |
| 환각 | Hallucination | AI 모델이 사실이 아닌 내용을 사실처럼 생성하는 현상 |

---

## 참고 자료 및 출처

- [AI Model Releases Timeline - LLM Stats](https://llm-stats.com/llm-updates)
- [2025 LLM Review - Atoms.dev](https://atoms.dev/blog/2025-llm-review-gpt-5-2-gemini-3-pro-claude-4-5)
- [The Year in LLMs 2025 - Simon Willison](https://simonwillison.net/2025/Dec/31/the-year-in-llms/)
- [Cursor Hits $2B ARR - TechBuzz](https://www.techbuzz.ai/articles/cursor-hits-2b-arr-doubles-revenue-in-just-3-months)
- [AI Coding Tools Compared 2026 - TLDL](https://www.tldl.io/resources/ai-coding-tools-2026)
- [Cursor AI Adoption Trends - Opsera](https://opsera.ai/blog/cursor-ai-adoption-trends-real-data-from-the-fastest-growing-coding-tool/)
- [General AI Agents 2026 Landscape - StartupHub](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/general-ai-agents-the-ultimate-guide-to-the-2026-landscape-meta-manus-kortix-more/)
- [Perplexity Computer Launch 2026 - Medium](https://medium.com/illumination/perplexity-computer-launch-2026-full-review-of-the-new-agentic-ai-tool-df227eb61c36)
- [State of AI Video Generation Feb 2026 - Cliprise](https://medium.com/@cliprise/the-state-of-ai-video-generation-in-february-2026-every-major-model-analyzed-6dbfedbe3a5c)
- [ElevenLabs $11B Valuation - CNBC](https://www.cnbc.com/2026/02/04/nvidia-backed-ai-startup-elevenlabs-11-billion-valuation.html)
- [Microsoft 365 Copilot Adoption - Stackmatix](https://www.stackmatix.com/blog/copilot-market-adoption-trends)
- [DeepSeek Open Source AI Revolution - Programming Helper](https://www.programming-helper.com/tech/deepseek-open-source-ai-models-2026-python-enterprise-adoption)
- [Midjourney v7 vs SD 3.5 - AIMarketwave](https://aimarketwave.com/media/midjourney-v7-vs-stable-diffusion-35-which-ai-image-generator-to-choose-in-2025)
- [Anthropic Claude Agent SDK - Official Docs](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Microsoft 365 E7 Bundle - CNBC](https://www.cnbc.com/2026/03/09/microsoft-office-365-e7-copilot-ai.html)

---

> **다음 장 안내**: 제3장에서는 생성형 AI의 핵심 원리와 작동 방식을 비전문가도 이해할 수 있도록 설명합니다.

---

*본 문서는 2026년 3월 18일 기준으로 작성되었습니다. AI 기술은 빠르게 변화하므로, 구체적인 수치와 가격은 각 서비스의 공식 페이지에서 최신 정보를 확인하시기 바랍니다.*
