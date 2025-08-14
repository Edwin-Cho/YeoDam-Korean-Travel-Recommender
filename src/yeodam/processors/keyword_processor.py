"""Keyword processing service for travel recommendations."""

from openai import OpenAI
from typing import List, Dict, Any
from fuzzywuzzy import process
from ..config import CATEGORY_MAPPINGS
from ..exceptions import KeywordProcessingError
from ..utils.utils import load_dynamic_mapping, save_dynamic_mapping

class KeywordProcessor:
    """Service for processing and expanding travel keywords."""
    
    def __init__(self, openai_api_key: str):
        self.client = OpenAI(api_key=openai_api_key)
        self.dynamic_mapping = load_dynamic_mapping()
    
    def expand_keywords(self, keywords: List[str]) -> List[str]:
        """
        Expand keywords using AI to include related terms.
        
        Args:
            keywords: List of original keywords
            
        Returns:
            List of expanded keywords
            
        Raises:
            KeywordProcessingError: If keyword expansion fails
        """
        if not keywords:
            return keywords
        
        try:
            keywords_str = ", ".join(keywords)
            prompt = f"""
            다음 여행 키워드들과 관련된 추가 키워드들을 제안해주세요: {keywords_str}
            
            관련 키워드들을 쉼표로 구분하여 나열해주세요. 원래 키워드도 포함해주세요.
            예시: 박물관, 미술관, 전시관, 문화센터
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            
            expanded_text = response.choices[0].message.content.strip()
            expanded_keywords = [kw.strip() for kw in expanded_text.split(",")]
            
            # Remove duplicates while preserving order
            unique_keywords = []
            seen = set()
            for kw in expanded_keywords:
                if kw and kw not in seen:
                    unique_keywords.append(kw)
                    seen.add(kw)
            
            return unique_keywords
            
        except Exception as e:
            raise KeywordProcessingError(f"키워드 확장 실패: {str(e)}")
    
    def map_keywords_to_categories(self, keywords: List[str], 
                                 default_category: List[str] = None) -> List[str]:
        """
        Map keywords to Google Places categories using fuzzy matching.
        
        Args:
            keywords: List of keywords to map
            default_category: Default categories if no match found
            
        Returns:
            List of mapped categories
        """
        if default_category is None:
            default_category = ["tourist_attraction"]
        
        mapped_categories = set()
        
        for keyword in keywords:
            # Check dynamic mapping first
            if keyword in self.dynamic_mapping:
                mapped_categories.update(self.dynamic_mapping[keyword])
                continue
            
            # Use fuzzy matching for static mappings
            best_match = process.extractOne(keyword, CATEGORY_MAPPINGS.keys())
            
            if best_match and best_match[1] >= 70:  # 70% similarity threshold
                matched_key = best_match[0]
                categories = CATEGORY_MAPPINGS[matched_key]
                mapped_categories.update(categories)
                
                # Save to dynamic mapping for future use
                self.dynamic_mapping[keyword] = categories
            else:
                # Use default category
                mapped_categories.update(default_category)
        
        # Save updated dynamic mapping
        try:
            save_dynamic_mapping(self.dynamic_mapping)
        except Exception as e:
            print(f"동적 매핑 저장 중 오류: {str(e)}")
        
        return list(mapped_categories)
