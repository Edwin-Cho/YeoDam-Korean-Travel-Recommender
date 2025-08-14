# Yeodam - 한국 여행 추천 시스템

> **English Documentation**: [README.md](README.md)

AI 기반 한국 여행 추천 시스템으로, Google Places API와 OpenAI를 활용하여 사용자 선호도에 맞는 장소와 맛집을 추천합니다.

## 주요 기능

- **위치 기반 검색**: 한국 어떤 지역이든 주변 장소와 맛집 검색
- **AI 키워드 확장**: OpenAI를 활용한 지능형 키워드 확장
- **스마트 카테고리 매핑**: 한국어 키워드를 Google Places 카테고리로 자동 매핑
- **평점 필터링**: 3.5점 이상의 장소만 추천
- **한국어 번역**: 검색 결과를 한국어로 번역
- **모듈화된 아키텍처**: 깔끔하고 유지보수 가능한 코드 구조

## 프로젝트 구조

```
yeodam/
├── src/
│   └── yeodam/
│       ├── __init__.py          # 패키지 초기화
│       ├── config.py            # 설정 및 카테고리 매핑
│       ├── exceptions.py        # 커스텀 예외 클래스
│       ├── services/            # 외부 API 서비스
│       │   ├── __init__.py
│       │   ├── geocoding_service.py    # 위치 좌표 검색
│       │   ├── places_service.py       # Google Places API 작업
│       │   └── translation_service.py  # 번역 서비스
│       ├── processors/          # 데이터 처리
│       │   ├── __init__.py
│       │   └── keyword_processor.py    # 키워드 처리 및 확장
│       └── utils/               # 유틸리티
│           ├── __init__.py
│           ├── utils.py         # 공통 유틸리티 함수
│           └── display_service.py      # 결과 표시 포맷팅
├── travel_recommender.py        # 메인 실행 파일
├── requirements.txt
├── setup.py
├── .env.example
└── README.md
```

## 설치 및 설정

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정
`.env.example` 파일을 `.env`로 복사하고 API 키를 설정하세요:

```bash
cp .env.example .env
```

`.env` 파일을 편집하여 실제 API 키를 입력하세요:
```
GOOGLE_API_KEY=실제_구글_API_키
OPENAI_API_KEY=실제_오픈AI_API_키
```

### 3. API 키 발급 방법

#### Google Places API 키:
1. [Google Cloud Console](https://console.cloud.google.com/)에 접속
2. 새 프로젝트 생성 또는 기존 프로젝트 선택
3. "API 및 서비스" > "라이브러리"로 이동
4. "Places API"와 "Geocoding API" 활성화
5. "사용자 인증 정보" > "사용자 인증 정보 만들기" > "API 키" 선택

#### OpenAI API 키:
1. [OpenAI 플랫폼](https://platform.openai.com/)에 가입
2. "API Keys" 섹션으로 이동
3. "Create new secret key" 클릭

### 4. 애플리케이션 실행
```bash
python travel_recommender.py
```

## 사용 방법

1. 위치 입력 (예: "제주", "서울", "부산")
2. 여행 선호도를 쉼표로 구분하여 입력 (예: "박물관, 카페, 공원")
3. 검색 반경을 미터 단위로 설정 (기본값: 20000)
4. 카테고리별 최대 결과 수 설정 (기본값: 10)

시스템이 수행하는 작업:
- AI를 사용하여 키워드 확장
- 적절한 장소 카테고리에 매핑
- 장소와 맛집 검색
- 포맷된 테이블로 결과 표시

## 지원 키워드 예시

다음과 같은 한국어 키워드들을 지원합니다:
- **문화/관광**: 박물관, 미술관, 관광지, 놀이공원, 동물원, 수족관
- **자연**: 공원, 해변, 산, 캠핑장
- **음식**: 카페, 레스토랑, 바, 클럽
- **쇼핑**: 쇼핑몰, 상점
- **숙박**: 호텔, 숙박시설
- **교통**: 지하철역, 버스정류장, 공항
- **편의시설**: 병원, 약국, 은행, ATM, 주유소
- **종교**: 교회, 사원, 모스크
- **스포츠/레저**: 체육관, 스파, 스키, 서핑, 자전거
- **교육**: 도서관, 학교, 대학교
- **엔터테인먼트**: 영화관

## 기존 버전 대비 개선사항

- **모듈화된 설계**: 관심사를 집중된 클래스로 분리
- **향상된 오류 처리**: 의미 있는 메시지를 가진 커스텀 예외
- **타입 힌트**: 개선된 코드 문서화 및 IDE 지원
- **설정 관리**: 중앙화된 설정
- **깔끔한 API**: 컴포넌트 간 단순화된 인터페이스
- **유지보수성**: 테스트, 디버깅, 확장이 더 쉬움

## 보안 주의사항

⚠️ **중요**: API 키를 안전하게 관리하세요
- `.env` 파일을 절대 Git에 커밋하지 마세요
- API 키를 코드에 직접 하드코딩하지 마세요
- 프로덕션 환경에서는 환경 변수나 보안 키 관리 서비스를 사용하세요

## 문제 해결

### 일반적인 오류들:

1. **API 키 오류**:
   ```
   환경 변수 'GOOGLE_API_KEY'가 설정되지 않았습니다.
   ```
   → `.env` 파일에 올바른 API 키가 설정되어 있는지 확인하세요.

2. **모듈 import 오류**:
   ```
   ModuleNotFoundError: No module named 'requests'
   ```
   → `pip install -r requirements.txt`를 실행하세요.

3. **API 할당량 초과**:
   → Google Cloud Console에서 API 사용량을 확인하고 결제 정보를 설정하세요.

## 라이선스

이 프로젝트는 개인 및 교육 목적으로 자유롭게 사용할 수 있습니다.

## 기여하기

버그 리포트나 기능 제안은 GitHub Issues를 통해 제출해 주세요.

---

**참고**: 이 시스템은 외부 API(Google Places, OpenAI)를 사용하므로 인터넷 연결이 필요하며, API 사용에 따른 비용이 발생할 수 있습니다.
