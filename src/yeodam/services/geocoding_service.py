"""Geocoding service for location coordinate retrieval."""

import requests
from typing import Optional, Tuple
from ..config import Config
from ..exceptions import APIError, LocationNotFoundError
from ..utils.utils import validate_coordinates, format_location_string, safe_get_nested

class GeocodingService:
    """Service for geocoding location names to coordinates."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.config = Config()
    
    def get_location_coordinates(self, location: str) -> str:
        """
        Get coordinates for a location name.
        
        Args:
            location: Location name to geocode
            
        Returns:
            Formatted coordinate string "lat,lng"
            
        Raises:
            LocationNotFoundError: If location cannot be found
            APIError: If API request fails
        """
        params = {
            "address": location,
            "key": self.api_key
        }
        
        try:
            response = requests.get(self.config.GOOGLE_GEOCODING_URL, params=params)
            response.raise_for_status()
            
            data = response.json()
            results = data.get('results', [])
            
            if not results:
                raise LocationNotFoundError(f"위치를 찾을 수 없습니다: {location}")
            
            geometry = safe_get_nested(results[0], ['geometry', 'location'])
            if not geometry:
                raise LocationNotFoundError(f"좌표 정보를 찾을 수 없습니다: {location}")
            
            lat = geometry.get('lat')
            lng = geometry.get('lng')
            
            if not validate_coordinates(lat, lng):
                raise LocationNotFoundError(f"유효하지 않은 좌표입니다: {location}")
            
            return format_location_string(lat, lng)
            
        except requests.RequestException as e:
            raise APIError(f"Geocoding API 요청 실패: {str(e)}")
        except Exception as e:
            raise APIError(f"예상치 못한 오류: {str(e)}")
