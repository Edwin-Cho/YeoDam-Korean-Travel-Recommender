"""
Refactored Travel Recommendation System

A modular travel recommendation system that uses Google Places API
and OpenAI to suggest places and restaurants based on user preferences.
"""

import os
from dotenv import load_dotenv
from typing import List, Tuple

from src.yeodam.config import Config
from src.yeodam.exceptions import YeodamError as TravelRecommendationError, APIError, ConfigurationError
from src.yeodam.services.geocoding_service import GeocodingService
from src.yeodam.services.places_service import PlacesService
from src.yeodam.processors.keyword_processor import KeywordProcessor
from src.yeodam.utils.display_service import DisplayService

# LocationNotFoundError는 APIError의 하위 클래스로 처리
LocationNotFoundError = APIError

class TravelRecommender:
    """Main travel recommendation system."""
    
    def __init__(self):
        """Initialize the travel recommender with all required services."""
        load_dotenv()
        self.config = Config()
        
        # Initialize services
        self.geocoding_service = GeocodingService(self.config.google_api_key)
        self.places_service = PlacesService(self.config.google_api_key)
        self.keyword_processor = KeywordProcessor(self.config.openai_api_key)
        self.display_service = DisplayService()
    
    def get_user_input(self) -> Tuple[str, List[str], int, int]:
        """
        Get user input for location, preferences, radius, and max results.
        
        Returns:
            Tuple of (location, preferences, radius, max_results)
        """
        location = input("검색할 지역을 입력하세요 (예: 제주, 서울, 부산): ").strip()
        
        preferences_input = input("여행 선호 키워드를 입력하세요 (쉼표로 구분): ").strip()
        preferences = [kw.strip() for kw in preferences_input.split(",") if kw.strip()]
        
        radius_input = input(f"검색 반경(미터 단위)을 입력하세요 (기본값 {self.config.DEFAULT_RADIUS}): ").strip()
        radius = int(radius_input) if radius_input.isdigit() else self.config.DEFAULT_RADIUS
        
        max_results_input = input(f"최대 결과 개수를 입력하세요 (기본값 {self.config.DEFAULT_MAX_RESULTS}): ").strip()
        max_results = int(max_results_input) if max_results_input.isdigit() else self.config.DEFAULT_MAX_RESULTS
        
        return location, preferences, radius, max_results
    
    def process_recommendations(self, location_name: str, preferences: List[str], 
                              radius: int, max_results: int) -> None:
        """
        Process travel recommendations based on user input.
        
        Args:
            location_name: Name of the location to search
            preferences: List of user preferences
            radius: Search radius in meters
            max_results: Maximum number of results
        """
        try:
            # Get location coordinates
            print(f"'{location_name}' 위치 정보를 가져오는 중...")
            location_coords = self.geocoding_service.get_location_coordinates(location_name)
            print(f"위치 좌표: {location_coords}")
            
            # Expand keywords
            print("키워드를 확장하는 중...")
            expanded_preferences = self.keyword_processor.expand_keywords(preferences)
            print(f"확장된 키워드: {expanded_preferences}")
            
            # Map keywords to categories
            categories = self.keyword_processor.map_keywords_to_categories(expanded_preferences)
            print(f"매핑된 카테고리: {categories}")
            
            # Search for places and restaurants
            print("장소와 레스토랑을 검색하는 중...")
            places, restaurants = self.places_service.get_places_by_categories(
                categories, location_coords, radius, max_results
            )
            
            # Display results
            print(f"\n검색 완료! 장소 {len(places)}개, 레스토랑 {len(restaurants)}개를 찾았습니다.\n")
            self.display_service.display_results(places, restaurants)
            
        except LocationNotFoundError as e:
            print(f"위치 오류: {str(e)}")
        except APIError as e:
            print(f"API 오류: {str(e)}")
        except TravelRecommendationError as e:
            print(f"시스템 오류: {str(e)}")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {str(e)}")
    
    def run(self) -> None:
        """Run the travel recommendation system."""
        print("=== 여행 추천 시스템 ===")
        print("여행지와 선호도를 입력하면 맞춤형 장소와 맛집을 추천해드립니다!\n")
        
        try:
            location, preferences, radius, max_results = self.get_user_input()
            
            if not location:
                print("위치를 입력해주세요.")
                return
            
            if not preferences:
                print("선호 키워드를 입력해주세요.")
                return
            
            self.process_recommendations(location, preferences, radius, max_results)
            
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
        except Exception as e:
            print(f"프로그램 실행 중 오류가 발생했습니다: {str(e)}")

def main():
    """Main entry point."""
    try:
        recommender = TravelRecommender()
        recommender.run()
    except Exception as e:
        print(f"시스템 초기화 실패: {str(e)}")
        print("환경 변수 설정을 확인해주세요.")

if __name__ == "__main__":
    main()
