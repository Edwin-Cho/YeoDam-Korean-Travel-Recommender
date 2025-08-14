"""Display service for showing search results."""

import pandas as pd
from typing import List, Dict, Any
from IPython.display import display
from ..services.translation_service import TranslationService

class DisplayService:
    """Service for displaying search results in formatted tables."""
    
    def __init__(self):
        self.translator = TranslationService()
    
    def display_results(self, places: List[Dict[str, Any]], 
                       restaurants: List[Dict[str, Any]]) -> None:
        """
        Display places and restaurants in formatted DataFrames.
        
        Args:
            places: List of place details
            restaurants: List of restaurant details
        """
        self._display_places(places)
        self._display_restaurants(restaurants)
    
    def _display_places(self, places: List[Dict[str, Any]]) -> None:
        """Display places in a DataFrame."""
        if not places:
            print("추천 장소가 없습니다.")
            return
        
        print("추천 장소:")
        places_data = []
        
        for place in places:
            translated_name = self.translator.translate_text(place.get('name', '정보 없음'))
            translated_address = self.translator.translate_text(place.get('formatted_address', '주소 정보가 제공되지 않음'))
            
            places_data.append({
                "이름": translated_name,
                "주소": translated_address,
                "평점": place.get('rating', 0),
                "리뷰 수": place.get('user_ratings_total', '정보 없음'),
                "URL": place.get('url', 'URL 정보가 제공되지 않음')
            })
        
        places_df = pd.DataFrame(places_data)
        display(places_df)
    
    def _display_restaurants(self, restaurants: List[Dict[str, Any]]) -> None:
        """Display restaurants in a DataFrame."""
        if not restaurants:
            print("추천 맛집이 없습니다.")
            return
        
        print("\n추천 맛집:")
        restaurants_data = []
        
        for restaurant in restaurants:
            translated_name = self.translator.translate_text(restaurant.get('name', '정보 없음'))
            translated_address = self.translator.translate_text(restaurant.get('formatted_address', '주소 정보가 제공되지 않음'))
            
            restaurants_data.append({
                "이름": translated_name,
                "주소": translated_address,
                "평점": restaurant.get('rating', 0),
                "리뷰 수": restaurant.get('user_ratings_total', '정보 없음'),
                "URL": restaurant.get('url', 'URL 정보가 제공되지 않음')
            })
        
        restaurants_df = pd.DataFrame(restaurants_data)
        display(restaurants_df)
