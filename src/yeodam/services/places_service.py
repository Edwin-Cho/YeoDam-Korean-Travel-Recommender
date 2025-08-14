"""Google Places API service for place search and details."""

import requests
from typing import List, Dict, Any, Optional, Tuple
from ..config import Config
from ..exceptions import APIError
from ..utils.utils import safe_get_nested

class PlacesService:
    """Service for Google Places API operations."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.config = Config()
    
    def get_place_details(self, place_id: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information for a place.
        
        Args:
            place_id: Google Places place ID
            
        Returns:
            Place details dictionary or None if rating < MIN_RATING
            
        Raises:
            APIError: If API request fails
        """
        url = f"{self.config.GOOGLE_PLACES_BASE_URL}/details/json"
        params = {
            "place_id": place_id,
            "key": self.api_key,
            "fields": "name,rating,user_ratings_total,formatted_address,vicinity,url,geometry"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            result = data.get('result', {})
            
            if not result:
                return None
            
            rating = result.get('rating', 0)
            if rating < self.config.MIN_RATING:
                return None
            
            return {
                "name": result.get('name', '정보 없음'),
                "rating": rating,
                "user_ratings_total": result.get('user_ratings_total', '정보 없음'),
                "formatted_address": result.get('formatted_address') or result.get('vicinity', '주소 정보가 제공되지 않음'),
                "url": result.get('url', 'URL 정보가 제공되지 않음'),
                "geometry": result.get('geometry', {})
            }
            
        except requests.RequestException as e:
            raise APIError(f"Place details API 요청 실패: {str(e)}")
    
    def search_nearby_places(self, location: str, radius: int, place_type: str) -> List[Dict[str, Any]]:
        """
        Search for nearby places of a specific type.
        
        Args:
            location: Location coordinates as "lat,lng"
            radius: Search radius in meters
            place_type: Google Places type
            
        Returns:
            List of place dictionaries
            
        Raises:
            APIError: If API request fails
        """
        url = f"{self.config.GOOGLE_PLACES_BASE_URL}/nearbysearch/json"
        params = {
            "location": location,
            "radius": radius,
            "type": place_type,
            "key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get('results', [])
            
        except requests.RequestException as e:
            raise APIError(f"Nearby search API 요청 실패: {str(e)}")
    
    def get_places_by_categories(self, categories: List[str], location: str, 
                                radius: int, max_results: int) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Get places and restaurants by categories.
        
        Args:
            categories: List of place categories
            location: Location coordinates as "lat,lng"
            radius: Search radius in meters
            max_results: Maximum number of results per category
            
        Returns:
            Tuple of (places, restaurants) lists
            
        Raises:
            APIError: If API requests fail
        """
        all_places = []
        restaurants = []
        seen_place_ids = set()
        seen_restaurant_ids = set()
        
        # Search for places by category
        for category in categories:
            try:
                results = self.search_nearby_places(location, radius, category)
                
                for place in results[:max_results]:
                    place_id = place.get('place_id')
                    if place_id and place_id not in seen_place_ids:
                        place_details = self.get_place_details(place_id)
                        if place_details:
                            all_places.append(place_details)
                            seen_place_ids.add(place_id)
                            
            except APIError as e:
                print(f"카테고리 '{category}' 검색 중 오류: {str(e)}")
                continue
        
        # Search for restaurants
        try:
            restaurant_results = self.search_nearby_places(location, radius, "restaurant")
            
            for restaurant in restaurant_results[:max_results]:
                place_id = restaurant.get('place_id')
                if place_id and place_id not in seen_restaurant_ids:
                    restaurant_details = self.get_place_details(place_id)
                    if restaurant_details:
                        restaurants.append(restaurant_details)
                        seen_restaurant_ids.add(place_id)
                        
        except APIError as e:
            print(f"레스토랑 검색 중 오류: {str(e)}")
        
        return all_places, restaurants
