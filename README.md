# Yeodam - Korean Travel Recommendation System

> **한국어 문서**: [README_KR.md](README_KR.md)

An AI-powered Korean travel recommendation system that uses Google Places API and OpenAI to suggest places and restaurants based on user preferences.

## Features

- **Location-based search**: Find places and restaurants near any location in Korea
- **AI keyword expansion**: Intelligent keyword expansion using OpenAI
- **Smart category mapping**: Automatic mapping of Korean keywords to Google Places categories
- **Rating filtering**: Only recommend places with ratings ≥ 3.5
- **Korean translation**: Translate search results to Korean
- **Modular architecture**: Clean, maintainable code structure

## Project Structure

```
yeodam/
├── src/
│   └── yeodam/
│       ├── __init__.py          # Package initialization
│       ├── config.py            # Configuration and category mappings
│       ├── exceptions.py        # Custom exception classes
│       ├── services/            # External API services
│       │   ├── __init__.py
│       │   ├── geocoding_service.py    # Location coordinate retrieval
│       │   ├── places_service.py       # Google Places API operations
│       │   └── translation_service.py  # Translation service
│       ├── processors/          # Data processing
│       │   ├── __init__.py
│       │   └── keyword_processor.py    # Keyword processing and expansion
│       └── utils/               # Utilities
│           ├── __init__.py
│           ├── utils.py         # Common utility functions
│           └── display_service.py      # Result display formatting
├── travel_recommender.py        # Main execution file
├── requirements.txt
├── setup.py
├── .env.example
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env` file:
```
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

3. Run the application:
```bash
python travel_recommender.py
```

## Usage

1. Enter a location (e.g., "제주", "서울", "부산")
2. Enter travel preferences separated by commas (e.g., "박물관, 카페, 공원")
3. Set search radius in meters (default: 20000)
4. Set maximum results per category (default: 10)

The system will:
- Expand your keywords using AI
- Map them to appropriate place categories
- Search for places and restaurants
- Display results in formatted tables

## Improvements from Original

- **Modular design**: Separated concerns into focused classes
- **Better error handling**: Custom exceptions with meaningful messages
- **Type hints**: Improved code documentation and IDE support
- **Configuration management**: Centralized settings
- **Cleaner API**: Simplified interfaces between components
- **Maintainability**: Easier to test, debug, and extend
