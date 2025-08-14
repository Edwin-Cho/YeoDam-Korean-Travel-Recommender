"""Utility functions for the travel recommendation system."""

import os
import pickle
from typing import Dict, Any, Optional
from ..config import Config
from ..exceptions import TravelRecommendationError

def load_dynamic_mapping() -> Dict[str, Any]:
    """Load dynamic mapping from pickle file."""
    try:
        if os.path.exists(Config.DYNAMIC_MAPPING_FILE):
            with open(Config.DYNAMIC_MAPPING_FILE, "rb") as f:
                return pickle.load(f)
        return {}
    except Exception as e:
        raise TravelRecommendationError(f"동적 매핑 로드 실패: {str(e)}")

def save_dynamic_mapping(dynamic_mapping: Dict[str, Any]) -> None:
    """Save dynamic mapping to pickle file."""
    try:
        with open(Config.DYNAMIC_MAPPING_FILE, "wb") as f:
            pickle.dump(dynamic_mapping, f)
    except Exception as e:
        raise TravelRecommendationError(f"동적 매핑 저장 실패: {str(e)}")

def validate_coordinates(lat: Optional[float], lng: Optional[float]) -> bool:
    """Validate latitude and longitude coordinates."""
    if lat is None or lng is None:
        return False
    return -90 <= lat <= 90 and -180 <= lng <= 180

def format_location_string(lat: float, lng: float) -> str:
    """Format coordinates as location string."""
    return f"{lat},{lng}"

def safe_get_nested(data: Dict[str, Any], keys: list, default: Any = None) -> Any:
    """Safely get nested dictionary values."""
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data
