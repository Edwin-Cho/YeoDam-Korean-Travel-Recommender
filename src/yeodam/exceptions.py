"""Custom exceptions for the travel recommendation system."""

class YeodamError(Exception):
    """Base exception for Yeodam travel recommendation system."""
    pass

class TravelRecommendationError(YeodamError):
    """Base exception for travel recommendation system."""
    pass

class APIError(YeodamError):
    """Raised when API calls fail."""
    pass

class ConfigurationError(YeodamError):
    """Raised when configuration is invalid."""
    pass

class LocationNotFoundError(APIError):
    """Raised when location coordinates cannot be found."""
    pass

class TranslationError(YeodamError):
    """Raised when translation fails."""
    pass

class KeywordProcessingError(YeodamError):
    """Raised when keyword processing fails."""
    pass
