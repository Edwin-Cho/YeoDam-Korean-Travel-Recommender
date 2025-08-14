"""Configuration settings for the travel recommendation system."""

import os
from typing import Dict, List

class Config:
    """Application configuration settings."""
    
    # File paths
    DYNAMIC_MAPPING_FILE = "dynamic_mapping.pkl"
    
    # API settings
    GOOGLE_PLACES_BASE_URL = "https://maps.googleapis.com/maps/api/place"
    GOOGLE_GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"
    
    # Default values
    DEFAULT_RADIUS = 20000
    DEFAULT_MAX_RESULTS = 10
    MIN_RATING = 3.5
    
    # API Keys (loaded from environment)
    @property
    def google_api_key(self) -> str:
        key = os.getenv("GOOGLE_API_KEY")
        if not key:
            raise ValueError("환경 변수 'GOOGLE_API_KEY'가 설정되지 않았습니다.")
        return key
    
    @property
    def openai_api_key(self) -> str:
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            raise ValueError("환경 변수 'OPENAI_API_KEY'가 설정되지 않았습니다.")
        return key

# Category mappings - 한국 여행에 특화된 포괄적인 키워드 매핑
CATEGORY_MAPPINGS: Dict[str, List[str]] = {
    # 여행 목적
    "식도락": ["restaurant", "tourist_attraction"],
    "맛집": ["restaurant"],
    "힐링": ["spa", "tourist_attraction"],
    "관광": ["tourist_attraction"],
    "사진": ["tourist_attraction", "point_of_interest"],
    "액티비티": ["tourist_attraction", "point_of_interest"],
    "체험": ["tourist_attraction", "point_of_interest"],
    "역사": ["museum", "tourist_attraction"],
    "자연": ["natural_feature", "tourist_attraction"],
    "도심": ["tourist_attraction", "point_of_interest"],
    "동행": ["tourist_attraction"],

    # 동행자
    "커플": ["tourist_attraction"],
    "우정": ["tourist_attraction"],
    "가족": ["tourist_attraction"],

    # 계절
    "봄": ["tourist_attraction", "park"],
    "여름": ["tourist_attraction", "natural_feature"],
    "가을": ["tourist_attraction", "park"],
    "겨울": ["tourist_attraction", "natural_feature"],

    # 지역
    "경기도": ["tourist_attraction"],
    "강원도": ["tourist_attraction"],
    "전라도": ["tourist_attraction"],
    "경상도": ["tourist_attraction"],
    "충청도": ["tourist_attraction"],
    "제주도": ["tourist_attraction"],
    "한국의": ["tourist_attraction"],
    "북적이는": ["tourist_attraction"],
    "전통": ["tourist_attraction", "museum"],
    "블루레이스": ["tourist_attraction", "natural_feature"],

    # 예산
    "가성비": ["tourist_attraction"],
    "가심비": ["tourist_attraction"],

    # 자연
    "바다": ["natural_feature", "tourist_attraction"],
    "산": ["natural_feature", "park"],
    "호수": ["natural_feature", "park"],
    "계곡": ["natural_feature", "park"],
    "폭포": ["natural_feature", "tourist_attraction"],
    "숲": ["natural_feature", "park"],
    "섬": ["natural_feature", "tourist_attraction"],
    "해변": ["natural_feature", "tourist_attraction"],
    "국립공원": ["park", "natural_feature"],
    "생태공원": ["park", "natural_feature"],

    # 문화 및 역사
    "유적지": ["museum", "tourist_attraction"],
    "궁궐": ["museum", "tourist_attraction"],
    "성": ["museum", "tourist_attraction"],
    "전통마을": ["museum", "tourist_attraction"],
    "사원": ["place_of_worship", "tourist_attraction"],
    "교회": ["place_of_worship", "tourist_attraction"],
    "사찰": ["place_of_worship", "tourist_attraction"],
    "고궁": ["museum", "tourist_attraction"],
    "역사박물관": ["museum"],
    "기념관": ["museum"],
    "문화유산": ["museum", "tourist_attraction"],
    "향교": ["museum", "tourist_attraction"],
    "서원": ["museum", "tourist_attraction"],

    # 도시 명소
    "전망대": ["tourist_attraction", "point_of_interest"],
    "스카이라인": ["tourist_attraction", "natural_feature"],
    "타워": ["tourist_attraction", "point_of_interest"],
    "거리": ["tourist_attraction", "shopping_mall"],
    "시장": ["shopping_mall", "tourist_attraction"],
    "광장": ["tourist_attraction", "point_of_interest"],
    "분수": ["tourist_attraction", "point_of_interest"],
    "도심": ["tourist_attraction", "point_of_interest"],
    "야경": ["tourist_attraction", "point_of_interest"],
    "벽화마을": ["tourist_attraction", "art_gallery"],

    # 테마파크 및 엔터테인먼트
    "놀이공원": ["amusement_park", "tourist_attraction"],
    "워터파크": ["amusement_park", "tourist_attraction"],
    "동물원": ["zoo", "tourist_attraction"],
    "수족관": ["aquarium", "tourist_attraction"],
    "식물원": ["park", "tourist_attraction"],
    "미술관": ["museum", "art_gallery"],
    "극장": ["movie_theater", "point_of_interest"],
    "테마파크": ["amusement_park", "tourist_attraction"],
    "체험마을": ["tourist_attraction", "point_of_interest"],

    # 액티비티
    "하이킹": ["natural_feature", "park"],
    "등산": ["natural_feature", "park"],
    "캠핑": ["campground", "natural_feature"],
    "자전거": ["park", "point_of_interest"],
    "스키": ["natural_feature", "tourist_attraction"],
    "서핑": ["natural_feature", "tourist_attraction"],
    "패러글라이딩": ["natural_feature", "tourist_attraction"],
    "윈드서핑": ["natural_feature", "tourist_attraction"],
    "템플스테이": ["place_of_worship", "tourist_attraction"],
    "한옥스테이": ["lodging", "tourist_attraction"],

    # 축제 및 이벤트
    "축제": ["tourist_attraction", "point_of_interest"],
    "공연": ["point_of_interest", "tourist_attraction"],
    "불꽃놀이": ["tourist_attraction", "point_of_interest"],
    "전시회": ["museum", "art_gallery"],
    "문화축제": ["tourist_attraction", "point_of_interest"],
    "음악축제": ["tourist_attraction", "point_of_interest"],

    # 쇼핑 및 상업
    "쇼핑몰": ["shopping_mall"],
    "아울렛": ["shopping_mall"],
    "백화점": ["shopping_mall"],
    "전통시장": ["shopping_mall", "tourist_attraction"],
    "면세점": ["shopping_mall"],
    "지하상가": ["shopping_mall"],

    # 휴식 및 힐링
    "스파": ["spa"],
    "온천": ["spa"],
    "힐링": ["natural_feature", "spa"],
    "요가": ["natural_feature", "spa"],
    "명상": ["natural_feature", "spa"],
    "찜질방": ["spa"],
    "한방체험": ["spa", "tourist_attraction"],

    # 지역명소
    "랜드마크": ["tourist_attraction", "point_of_interest"],
    "포토존": ["tourist_attraction", "point_of_interest"],
    "전통가옥": ["museum", "tourist_attraction"],
    "박물관": ["museum"],
    "역사적 건축물": ["museum", "tourist_attraction"],
    "근대건축물": ["museum", "tourist_attraction"],
    "문화거리": ["tourist_attraction", "shopping_mall"],

    # 교통
    "케이블카": ["tourist_attraction", "point_of_interest"],
    "기차역": ["point_of_interest", "tourist_attraction"],
    "항구": ["natural_feature", "tourist_attraction"],
    "등대": ["tourist_attraction", "point_of_interest"],
    "공항": ["point_of_interest"],
    "레일바이크": ["tourist_attraction", "point_of_interest"],
    "유람선": ["tourist_attraction", "point_of_interest"],

    # 먹거리 여행
    "푸드트럭": ["restaurant", "tourist_attraction"],
    "길거리 음식": ["restaurant", "tourist_attraction"],
    "전통 음식": ["restaurant", "tourist_attraction"],
    "야시장": ["shopping_mall", "tourist_attraction"],
    "카페거리": ["cafe", "tourist_attraction"],
    "맛집거리": ["restaurant", "tourist_attraction"],

    # 기본 카테고리 (기존 유지)
    "카페": ["cafe"],
    "레스토랑": ["restaurant"],
    "바": ["bar"],
    "클럽": ["night_club"],
    "호텔": ["lodging"],
    "병원": ["hospital"],
    "약국": ["pharmacy"],
    "은행": ["bank"],
    "ATM": ["atm"],
    "주유소": ["gas_station"],
    "지하철역": ["subway_station"],
    "버스정류장": ["bus_station"],
    "체육관": ["gym"],
    "영화관": ["movie_theater"],
    "도서관": ["library"],
    "학교": ["school"],
    "대학교": ["university"],

    # 기타
    "밤하늘": ["natural_feature", "tourist_attraction"],
    "별보기": ["natural_feature", "tourist_attraction"],
    "피크닉": ["natural_feature", "park"],
    "공연장": ["tourist_attraction", "point_of_interest"],
    "문화센터": ["point_of_interest", "tourist_attraction"],
    "천문대": ["tourist_attraction", "point_of_interest"],
    "캘리그래피": ["tourist_attraction", "art_gallery"],
    "한류": ["tourist_attraction", "point_of_interest"],
    "드라마 촬영지": ["tourist_attraction", "point_of_interest"],
    "인생샷": ["tourist_attraction", "point_of_interest"]
}
