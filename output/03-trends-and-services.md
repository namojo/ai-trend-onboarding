# 제3장: AI 기술 트렌드와 응용 서비스 (2025~2026)

> **챕터 요약**: 이 장에서는 2025년 초부터 2026년 3월 현재까지의 AI 생태계를 **범용 모델(Foundation Models)**과 **응용 서비스(Application Services)**로 명확히 구분하여 정리합니다. 각 모델의 특징과 가격을 살펴보고, 응용 서비스가 어떤 기반 모델을 어떻게 활용하는지 매핑 테이블로 제시합니다. 마지막으로 비즈니스 효과와 투자 동향, 그리고 실패 사례까지 포함하여 AI 산업의 전체 그림을 그려봅니다.

---

## 3.1 범용 모델과 응용 서비스의 차이

AI 산업을 이해하려면 **범용 모델(Foundation Model)**과 **응용 서비스(Application Service)**를 구분하는 것이 매우 중요합니다.

| 구분 | 범용 모델 (Foundation Model) | 응용 서비스 (Application Service) |
|------|------|------|
| **정의** | API나 플랫폼으로 제공되는 기반 AI 모델 | 범용 모델을 활용해 특정 문제를 해결하는 서비스 |
| **예시** | GPT-5, Claude Opus 4.5, Gemini 3 Pro | Cursor, Perplexity, Microsoft 365 Copilot |
| **제공 형태** | API, SDK, 모델 웨이트 다운로드 | 웹앱, 데스크톱 앱, 브라우저 확장 |
| **사용자** | 개발자, 기업 | 최종 사용자(일반인 포함) |
| **비유** | 엔진 | 자동차 |

쉽게 말해, 범용 모델은 **"엔진"**이고 응용 서비스는 그 엔진을 탑재한 **"자동차"**입니다. 같은 엔진이라도 스포츠카, 트럭, 버스 등 다양한 차량이 만들어지듯, 하나의 범용 모델 위에 수많은 응용 서비스가 구축됩니다.

---

## 3.2 범용 모델 (Foundation Models) 총정리

### A. 텍스트 생성 모델

2025~2026년은 텍스트 생성 모델의 폭발적 발전이 이루어진 시기입니다. 특히 2025년 하반기에는 25일 만에 주요 4개사가 차세대 모델을 연달아 출시하는 이례적인 경쟁이 벌어졌습니다.

| 모델명 | 제공사 | 출시일 | 주요 특징 | API 가격 (입력/출력, /1M 토큰) |
|--------|--------|--------|-----------|-------------------------------|
| **GPT-4.5** | OpenAI | 2025.02 | 연구 프리뷰, 향상된 창의성과 EQ | $75 / $150 |
| **GPT-5** | OpenAI | 2025.08 | 멀티모달 통합, 추론 능력 대폭 향상 | $10 / $30 |
| **GPT-5.2** | OpenAI | 2025.12 | 코드 특화(Codex), 리포 단위 추론 | $3 / $15 |
| **GPT-5.4** | OpenAI | 2026.03 | 최신 플래그십, 추론+속도 균형 | $2.50 / $10 |
| **Claude Opus 4.5** | Anthropic | 2025.11 | 최고 수준 코딩/분석, 200K 컨텍스트 | $15 / $75 |
| **Claude Sonnet 4.6** | Anthropic | 2026.02 | 코딩 최적화, 가성비 최고 | $3 / $15 |
| **Gemini 2.5 Pro** | Google | 2025.Q2 | 강화된 추론, 100만 토큰 컨텍스트 | $3.50 / $10.50 |
| **Gemini 3 Pro** | Google | 2025.11 | 멀티모달 통합, 네이티브 도구 사용 | $5 / $15 |
| **LLaMA 4** | Meta | 2025.Q3 | 오픈소스, 10M 컨텍스트, 무료 | 무료 (오픈 웨이트) |
| **DeepSeek V3.2** | DeepSeek | 2025.H2 | MoE 671B, Elo 1421, 오픈소스 | 무료 (오픈 웨이트) |
| **Grok 4.1** | xAI | 2025.11 | 314B 파라미터, Apache 2.0 라이선스 | 무료 (오픈 웨이트) |

> **핵심 트렌드**: 2025년 하반기부터 오픈소스 모델(DeepSeek, LLaMA, Grok)이 상용 모델과 벤치마크에서 대등한 성능을 보이기 시작했습니다. DeepSeek R1은 약 590만 달러의 훈련 비용으로 프론티어 추론 성능을 달성하여 업계에 큰 충격을 주었습니다.

### B. 추론 특화 모델 (Reasoning Models)

2024년 말 OpenAI의 o1 출시를 기점으로, "생각하는 AI" 패러다임이 등장했습니다. 답변 전에 추가 연산 시간을 투입하여 복잡한 다단계 문제를 풀어내는 방식입니다.

| 모델명 | 제공사 | 출시일 | 주요 특징 | API 가격 |
|--------|--------|--------|-----------|----------|
| **o1** | OpenAI | 2024.12 | 최초 추론 특화 모델, 수학/코딩 탁월 | $15 / $60 |
| **o3** | OpenAI | 2025.Q1 | o1 후속, 더 빠르고 정확한 추론 | $10 / $40 |
| **o3-mini** | OpenAI | 2025.Q1 | 경량 추론, 비용 효율적 | $1.10 / $4.40 |
| **o3 Pro** | OpenAI | 2025.H2 | 최고 수준 추론, 프로 전용 | $150 / $600 |
| **DeepSeek R1** | DeepSeek | 2025.01 | 순수 RL 기반 추론, MIT 라이선스 | 무료 (오픈 웨이트) |

### C. 이미지 생성 모델

| 모델명 | 제공사 | 출시일 | 주요 특징 | 가격 |
|--------|--------|--------|-----------|------|
| **DALL-E 3.5** | OpenAI | 2025.H1 | 복잡한 장면 이해력 최고, ChatGPT 통합 | API $0.04~0.08/장 |
| **Midjourney v7** | Midjourney | 2025.04 | 아키텍처 재설계, 손/해부학 개선, 텍스트 렌더링 | $10~60/월 구독 |
| **Stable Diffusion 3.5** | Stability AI | 2025.H1 | 오픈소스, 커스터마이징 자유도 최고 | 무료 (로컬 실행) |
| **Flux Pro** | Black Forest Labs | 2025 | 가장 사실적인 사진 품질, 4.5초 생성 | API 종량제 |
| **Ideogram 2.0** | Ideogram | 2025 | 이미지 내 텍스트 렌더링 정확도 1위 | 프리미엄 구독 |
| **Imagen 4** | Google | 2026.Q1 | Gemini 생태계 통합, 고품질 | API 연동 |

> **선택 가이드**: 예술적 이미지는 **Midjourney**, 사실적 사진은 **Flux**, 텍스트 포함 이미지는 **Ideogram**, 손쉬운 사용은 **DALL-E**, 기술적 커스터마이징은 **Stable Diffusion**이 적합합니다.

### D. 영상 생성 모델

2026년은 AI 영상 생성이 메인스트림으로 진입한 해입니다. 텍스트 프롬프트만으로 네이티브 오디오, 립싱크, 효과음이 포함된 시네마틱 영상을 만들 수 있게 되었습니다.

| 모델명 | 제공사 | 출시일 | 주요 특징 | 비고 |
|--------|--------|--------|-----------|------|
| **Sora 2** | OpenAI | 2025.09 | 정밀한 프롬프트 추종, 세밀한 다이내믹스 | ChatGPT Plus 통합 |
| **Veo 3.1** | Google | 2026.01 | 네이티브 4K, 세로 영상 지원, 동기화 오디오 | YouTube 생태계 연동 |
| **Kling 3.0** | Kuaishou (중국) | 2026.02 | 멀티샷 시퀀스(3-15초), 카메라 앵글간 피사체 일관성 | 다중 캐릭터 음성 |
| **Runway Gen-4.5** | Runway | 2025.11 | 텍스트-비디오 리더보드 1위 (Elo 1,247) | 전문가용 편집 도구 |
| **Pika 2.0** | Pika Labs | 2025 | 간편한 UX, 빠른 생성 | 소셜 미디어 특화 |

### E. 음성/음악 생성 모델

| 모델명 | 제공사 | 출시일 | 주요 특징 | 가격 |
|--------|--------|--------|-----------|------|
| **ElevenLabs** | ElevenLabs | 2023~ (지속 업데이트) | 세계 최고 수준 AI 음성 합성, 음성 클로닝 | 무료~$99/월 |
| **Eleven Music** | ElevenLabs | 2025.08 | Merlin/Kobalt 라이선싱, 상용 가능 AI 음악 | 구독 포함 |
| **Suno v5** | Suno | 2025~2026 | 텍스트→완성곡(보컬+악기+프로덕션) | 무료~$24/월 |
| **Udio v1.5** | Udio | 2025 | 업계 최고 보컬 품질, 세밀한 제어 | 무료~$30/월 |

### F. 코드 특화 모델

| 모델명 | 제공사 | 출시일 | 주요 특징 |
|--------|--------|--------|-----------|
| **GPT-5.2 Codex** | OpenAI | 2025.H2 | 리포 단위 추론, 장기 코딩 태스크 |
| **Claude Sonnet 4.6** | Anthropic | 2026.02 | 코딩 벤치마크 최상위, $3/$15 가성비 |
| **Codex CLI** | OpenAI (오픈소스) | 2025 | 터미널 기반 에이전트 코딩, 로컬 실행 |
| **Claude Code** | Anthropic | 2025.02 (프리뷰) → 2025.05 (정식) | CLI 기반 코드베이스 전체 이해, 멀티스텝 워크플로 |

---

## 3.3 응용 서비스 (Application Services) 총정리

### A. AI 코딩 도구

AI 코딩 도구는 2025~2026년 가장 폭발적으로 성장한 카테고리입니다. "바이브 코딩(Vibe Coding)"이라는 신조어가 등장할 만큼, AI와 함께 코딩하는 것이 표준이 되었습니다.

| 서비스명 | 제공사 | 형태 | 기반 모델 | 가격 | 주요 특징 |
|----------|--------|------|-----------|------|-----------|
| **Cursor** | Anysphere | IDE (VS Code 포크) | Claude, GPT, 자체 모델 혼합 | 무료 / $19/월 Pro | 최고의 올인원 IDE 경험, 자동완성+에이전트 |
| **GitHub Copilot** | GitHub (Microsoft) | IDE 확장 | GPT-5 계열, Claude | $10~39/월 | 엔터프라이즈 표준, 코드 리뷰 자동화 |
| **Windsurf** | Codeium | IDE | 자체 모델 + Claude/GPT | 무료 / $15/월 Pro | 인라인 완성 품질 최고, 저렴한 가격 |
| **Claude Code** | Anthropic | CLI 도구 | Claude Sonnet/Opus | 무료 / $25/월 Pro | 터미널 기반, 코드베이스 전체 이해 |
| **Replit Agent** | Replit | 웹 IDE | 자체 모델 + GPT | 무료~$25/월 | 브라우저 기반, 즉시 배포 |
| **Codex CLI** | OpenAI (오픈소스) | CLI 도구 | GPT-5 Codex | 무료 (API 비용 별도) | 오픈소스, 로컬 에이전트 |

> **시장 동향**: Cursor는 출시 24개월 만에 ARR 10억 달러를 돌파하며 B2B SaaS 역사상 최고속 성장을 기록했습니다. 2026년 3월 기준 ARR 20억 달러를 넘어섰으며, 기업가치는 293억 달러에 달합니다.

### B. AI 검색

| 서비스명 | 제공사 | 기반 모델 | 주요 특징 | 사용자 수 |
|----------|--------|-----------|-----------|-----------|
| **Perplexity** | Perplexity AI | GPT, Claude, 자체 모델 | 출처 기반 답변, 실시간 검색 | 월 4,500만 (2025 중반) |
| **ChatGPT Search (Atlas)** | OpenAI | GPT-5 계열 | 대화형 검색, 웹 브라우징 통합 | ChatGPT 내장 |
| **Gemini** | Google | Gemini 3 | Google 검색 통합, 멀티모달 | Google 생태계 연동 |
| **Arc Search** | The Browser Company | 다중 모델 | 브라우저 네이티브 AI 검색 | - |

### C. AI 에이전트

2025~2026년 AI 에이전트 시장은 37억 달러에서 73.8억 달러로 2년 만에 2배 성장했으며, 2032년에는 1,036억 달러 규모로 전망됩니다.

| 서비스명 | 제공사 | 출시일 | 기반 모델 | 주요 특징 |
|----------|--------|--------|-----------|-----------|
| **Devin** | Cognition | 2024 (프리뷰) → 2025 (정식) | 자체 모델 + Claude/GPT | 완전 자율 코딩 에이전트, 환경 구축~배포 |
| **Manus** | Manus AI (중국) | 2025.03 | 다중 모델 | GAIA 벤치마크 기록 경신, 72시간 내 18만 사용자 |
| **AutoGPT** | 오픈소스 커뮤니티 | 2023~ | GPT 계열 | 자율 에이전트 프레임워크, 프로토타이핑용 |
| **CrewAI** | CrewAI | 2024~ | 다중 모델 | 멀티에이전트 팀 구성, Fortune 500 40% 채택 |
| **LangChain/LangGraph** | LangChain | 2023~ | 다중 모델 | 에이전트 프레임워크, GitHub 87K 스타 |

> **주목할 인수**: 2025년 12월, Meta가 Manus를 20~30억 달러에 인수한다고 발표했습니다.

### D. AI 디자인 도구

| 서비스명 | 제공사 | 기반 모델 | 주요 특징 | 가격 |
|----------|--------|-----------|-----------|------|
| **v0** | Vercel | Claude, GPT | 텍스트→React UI 컴포넌트, 즉시 배포 가능 | 무료~$20/월 |
| **Figma AI** | Figma | 자체 + 외부 모델 | 레이아웃 제안, 컴포넌트 자동 생성, 디자인 시스템 관리 | Figma 구독 포함 |
| **Canva AI** | Canva | 자체 + 외부 모델 | 편집 가능 레이어 디자인 생성, 3D 오브젝트, 브랜드 키트 | 무료~$13/월 |

### E. AI 영상 편집 도구

| 서비스명 | 제공사 | 주요 특징 | 타겟 사용자 |
|----------|--------|-----------|-------------|
| **CapCut AI** | ByteDance | 자동 자막(95% 정확도), 350+ AI 음성, 스크립트→영상 | 소셜미디어 크리에이터 |
| **Descript** | Descript | 트랜스크립트 기반 편집("문서처럼 편집"), AI 음성 오버더빙 | 팟캐스트/인터뷰 제작자 |

### F. 업무 자동화 도구

| 서비스명 | 제공사 | 기반 모델 | 주요 특징 |
|----------|--------|-----------|-----------|
| **Microsoft 365 Copilot** | Microsoft | GPT-5 계열 + Claude (Cowork) | Word/Excel/PPT/Teams AI 통합, 에이전트 스토어 |
| **Notion AI** | Notion | Claude + 자체 모델 | 문서 요약/작성/번역, Q&A |
| **Slack AI** | Salesforce | Claude | 채널 요약, 스레드 검색, 자동 응답 |
| **Zapier AI** | Zapier | GPT 계열 | 자연어로 자동화 워크플로 구축 |

### G. AI 하드웨어 (실패 사례 분석)

| 제품명 | 제공사 | 출시일 | 가격 | 결과 | 교훈 |
|--------|--------|--------|------|------|------|
| **Humane AI Pin** | Humane | 2024 | $699 + $24/월 | **완전 실패**: 2025.02 HP가 1.16억 달러에 인수, 서버 종료로 기기 벽돌화 | 스마트폰 대체는 시기상조, 기존 UX 무시 |
| **Rabbit R1** | Rabbit | 2024 | $199 | **부분 실패**: 10만 대 사전예약, 5개월 후 활성 사용자 5,000명 (95% 이탈) | "너무 일찍 출시" - 창업자 본인 인정 |

> **교훈**: 두 제품 모두 기술적 결함이 아니라, 스마트폰이 이미 동일한 기능을 제공할 수 있다는 근본적 문제에 부딪혔습니다. "스마트폰이 곧 같은 기능을 제공할 텐데, 소비자가 별도 기기를 살 이유가 없다"는 것이 전문가들의 공통된 분석입니다.

---

## 3.4 모델-서비스 매핑 테이블 (핵심)

아래 테이블은 각 응용 서비스가 어떤 범용 모델을 어떻게 활용하는지를 보여줍니다. 이것이 바로 현대 AI 산업의 **"엔진-자동차" 관계**입니다.

| 응용 서비스 | 기반 모델 | 활용 방식 | 카테고리 | 출시/업데이트 | 비즈니스 효과 |
|-------------|-----------|-----------|----------|---------------|---------------|
| **Cursor** | Claude Sonnet/Opus, GPT-5, 자체 모델 | API 호출 + 자체 파인튜닝 | AI 코딩 | 2023~ (지속 업데이트) | ARR $20억+ (2026.03), 기업가치 $293억 |
| **GitHub Copilot** | GPT-5 계열, Claude | API 호출 + 파인튜닝 | AI 코딩 | 2021~ (지속 업데이트) | 엔터프라이즈 고객 다수, MS 생태계 통합 |
| **Windsurf** | Claude, GPT, 자체 모델 | API 호출 + 자체 최적화 | AI 코딩 | 2024~ | Cursor 대비 저가 포지셔닝 |
| **Claude Code** | Claude Sonnet 4.6 / Opus 4.5 | 직접 통합 (자사 모델) | AI 코딩 | 2025.02 (프리뷰) → 2025.05 (정식) | Anthropic 매출 성장 기여 |
| **Perplexity** | GPT, Claude, 자체 모델 | API 호출 + RAG 파이프라인 | AI 검색 | 2022~ | ARR $2억 (2026.02), 기업가치 $212억 |
| **ChatGPT (Atlas)** | GPT-5 계열 | 직접 통합 (자사 모델) | AI 검색/대화 | 2022~ | OpenAI ARR $250억 (2026.02) |
| **Gemini** | Gemini 3 Pro | 직접 통합 (자사 모델) | AI 검색/대화 | 2023~ | 시장점유율 18.2%로 급성장 |
| **Devin** | Claude, GPT + 자체 모델 | API 호출 + 자체 에이전트 로직 | AI 에이전트 | 2024~2025 | 완전 자율 코딩 선도 |
| **Manus** | 다중 모델 조합 | API 호출 + 에이전트 오케스트레이션 | AI 에이전트 | 2025.03 | 72시간 내 18만 사용자, Meta 인수($20-30억) |
| **v0** | Claude, GPT | API 호출 | AI 디자인 | 2023~ | Vercel 생태계 확장 |
| **Microsoft 365 Copilot** | GPT-5 + Claude (Cowork) | API 호출 + 깊은 제품 통합 | 업무 자동화 | 2023~ | Microsoft 클라우드 매출 견인 |
| **Notion AI** | Claude + 자체 모델 | API 호출 | 업무 자동화 | 2023~ | Notion 유료 전환율 향상 |
| **Slack AI** | Claude | API 호출 | 업무 자동화 | 2024~ | Salesforce AI 전략 핵심 |
| **CapCut AI** | 자체 모델 (ByteDance) | 자체 모델 통합 | 영상 편집 | 2023~ | TikTok 생태계 시너지 |
| **Suno** | 자체 음악 생성 모델 | 자체 모델 | 음악 생성 | 2023~ | 빠르게 성장 중 |
| **ElevenLabs** | 자체 음성/음악 모델 | 자체 모델 | 음성/음악 | 2023~ | 상용 음악 라이선싱 최초 확보 |

---

## 3.5 비즈니스 효과와 투자 동향

### A. 주요 AI 기업 매출 및 기업가치

| 기업/서비스 | ARR (연환산매출) | 기업가치 | 주요 투자자 | 비고 |
|-------------|-----------------|----------|-------------|------|
| **OpenAI** | $250억 (2026.02) | $7,500-8,300억 | Microsoft, SoftBank, Thrive | 2025 매출 $130억, 적자 $85억 |
| **Anthropic** | $190억 (2026.03) | $3,500억+ | Google, GIC, Sequoia, ICONIQ | 연간 10배 성장, 2026 중반 OpenAI 추월 전망 |
| **Cursor (Anysphere)** | $20억+ (2026.03) | $293억 | Thrive, a16z, NVIDIA, Google | B2B SaaS 역사상 최고속 성장 |
| **Perplexity** | $2억 (2026.02), 연말 $6.5억 전망 | $212억 | 다수 VC | 전년 대비 800% 성장 |
| **Midjourney** | 약 $3억 (추정) | 비공개 (자체 수익) | 외부 투자 없음 | 11명의 직원으로 운영 |

### B. 주요 투자/인수 동향 (2025~2026)

| 시기 | 이벤트 | 금액 | 의미 |
|------|--------|------|------|
| 2025.03 | OpenAI 시리즈 펀딩 | $400억 (기업가치 $3,000억) | AI 사상 최대 펀딩 라운드 |
| 2025.09 | Anthropic 시리즈 F | $130억 (기업가치 $1,830억) | 6개월 만에 기업가치 3배 |
| 2025.11 | Cursor 시리즈 D | $23억 (기업가치 $293억) | AI 코딩 도구의 가치 입증 |
| 2025.12 | Meta의 Manus 인수 발표 | $20-30억 | 빅테크의 AI 에이전트 확보 경쟁 |
| 2026.초 | Anthropic 추가 라운드 진행 중 | $200억+ (기업가치 $3,500억) | GIC, Coatue 주도 |
| 2025.08 | OpenAI 세컨더리 주식 매각 | $60억 (기업가치 $5,000억) | 직원 유동성 제공 |

### C. 산업별 AI 도입 현황

| 산업 | 주요 활용 분야 | 대표 사례 |
|------|---------------|-----------|
| **소프트웨어 개발** | AI 코딩 도구, 코드 리뷰, 테스트 자동화 | Cursor, GitHub Copilot 도입 기업 급증 |
| **마케팅/광고** | 콘텐츠 생성, 개인화, 광고 카피 | Canva AI, Midjourney 활용 |
| **금융** | 리스크 분석, 고객 서비스, 문서 처리 | 대형 은행 Claude/GPT API 도입 |
| **헬스케어** | 의료 영상 분석, 진단 보조, 신약 개발 | Google Health AI, 의료 특화 LLM |
| **미디어/엔터테인먼트** | 영상 생성, 음악 제작, 더빙/번역 | Sora, ElevenLabs 활용 |
| **법률** | 계약서 분석, 판례 검색, 문서 작성 | Harvey AI (GPT 기반 법률 AI) |
| **교육** | 개인화 학습, 튜터링, 콘텐츠 제작 | Khan Academy Khanmigo |

### D. 시장 점유율 변화

주목할 변화로, ChatGPT의 AI 어시스턴트 시장 점유율이 87%에서 68%로 하락한 반면, Gemini가 18.2%로 급성장했습니다. 이는 Google의 검색 생태계 통합과 Android 기본 탑재 효과로 분석됩니다. 다양한 전문 에이전트와 검색 서비스의 등장으로 시장이 분화되고 있습니다.

---

## 3.6 핵심 트렌드 요약

### 1. 오픈소스의 반격
DeepSeek R1이 590만 달러라는 파격적인 훈련 비용으로 프론티어 성능을 달성하면서, "AI 개발에는 수십억 달러가 필요하다"는 통념을 깨뜨렸습니다. LLaMA 4, Grok, Qwen 3 등 오픈소스 모델들이 상용 모델과 대등한 성능을 보여주고 있습니다.

### 2. 에이전트의 시대
2025년은 AI가 "대화"에서 "행동"으로 전환된 해입니다. Devin, Manus, Claude Code 등이 단순한 응답을 넘어 실제 작업을 수행하는 에이전트로 진화했습니다. Microsoft Agent 365 같은 엔터프라이즈 에이전트 플랫폼도 등장했습니다.

### 3. 멀티모달의 일상화
텍스트, 이미지, 영상, 음성, 코드를 넘나드는 멀티모달 능력이 기본이 되었습니다. GPT-5와 Gemini 3은 출시 시점부터 네이티브 멀티모달을 지원합니다.

### 4. AI 비용의 급격한 하락
GPT-4 대비 GPT-5.4의 API 가격은 약 1/20로 하락했습니다. 오픈소스 모델은 무료로 사용할 수 있어, AI 도입의 경제적 장벽이 크게 낮아졌습니다.

### 5. 바이브 코딩(Vibe Coding)의 부상
AI와 대화하며 코드를 작성하는 "바이브 코딩"이 2025년 최대 유행어가 되었습니다. 비개발자도 v0, Replit Agent 등을 통해 웹 앱을 만들 수 있게 되면서, "5만 달러와 6개월이 필요했던 제품 출시가 노트북 하나와 주말 하나면 가능한 시대"가 되었습니다.

---

## 3.7 참고 출처

- [OpenAI Crosses $12 Billion ARR - SaaStr](https://www.saastr.com/openai-crosses-12-billion-arr-the-3-year-sprint-that-redefined-whats-possible-in-scaling-software/)
- [Anthropic Revenue & Funding - Sacra](https://sacra.com/c/anthropic/)
- [Anthropic Could Surpass OpenAI - Epoch AI](https://epoch.ai/data-insights/anthropic-openai-revenue)
- [Cursor $2.3B Series D - CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html)
- [Cursor Surpasses $2B ARR - TechCrunch](https://techcrunch.com/2026/03/02/cursor-has-reportedly-surpassed-2b-in-annualized-revenue/)
- [Perplexity AI Statistics - DemandSage](https://www.demandsage.com/perplexity-ai-statistics/)
- [AI Video Generation State 2026 - Cliprise](https://medium.com/@cliprise/the-state-of-ai-video-generation-in-february-2026-every-major-model-analyzed-6dbfedbe3a5c)
- [AI Coding Tools Compared 2026 - TLDL](https://www.tldl.io/resources/ai-coding-tools-2026)
- [Cursor vs Windsurf vs Claude Code - DEV Community](https://dev.to/pockit_tools/cursor-vs-windsurf-vs-claude-code-in-2026-the-honest-comparison-after-using-all-three-3gof)
- [Humane AI Pin Dead - TechRadar](https://www.techradar.com/computing/artificial-intelligence/with-the-humane-ai-pin-now-dead-what-does-the-rabbit-r1-need-to-do-to-survive)
- [AI Agent Market 2026 - USAII](https://www.usaii.org/ai-insights/ai-agents-in-2026-a-comparative-guide-to-tools-frameworks-and-platforms)
- [Manus AI Wikipedia](https://en.wikipedia.org/wiki/Manus_(AI_agent))
- [ElevenLabs AI Music - TechCrunch](https://techcrunch.com/2025/08/05/elevenlabs-launches-an-ai-music-generator-which-it-claims-is-cleared-for-commercial-use/)
- [Open Source AI Models 2025 - Red Hat](https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025)
- [Top AI Coding Assistants 2026 - Deepak Gupta](https://guptadeepak.com/top-5-ai-coding-assistants-of-2026-cursor-copilot-windsurf-claude-code-and-tabnine-compared/)
- [Microsoft 365 Copilot Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/powering-frontier-transformation-with-copilot-and-agents/)
- [AI Image Generation 2026 - Gradually AI](https://www.gradually.ai/en/ai-image-models/)
- [2025 LLM Review - Atoms.dev](https://atoms.dev/blog/2025-llm-review-gpt-5-2-gemini-3-pro-claude-4-5)
- [Suno vs Udio vs ElevenLabs - VoteMyAI](https://www.votemyai.com/blog/suno-vs-udio-vs-elevenlabs.html)
- [Agentic AI Frameworks 2026 - AlphaMatch](https://www.alphamatch.ai/blog/top-agentic-ai-frameworks-2026)

---

> **다음 장 예고**: 제4장에서는 이러한 AI 도구들을 실제 업무에서 어떻게 활용하는지, 실습 위주의 가이드를 다룹니다.
