"""Translation service for text translation."""

from deep_translator import GoogleTranslator
from typing import Optional
from ..exceptions import TranslationError

class TranslationService:
    """Service for text translation using Google Translator."""
    
    def __init__(self):
        self.translator = GoogleTranslator()
    
    def translate_text(self, text: str, target_language: str = 'ko') -> str:
        """
        Translate text to target language.
        
        Args:
            text: Text to translate
            target_language: Target language code (default: 'ko')
            
        Returns:
            Translated text
            
        Raises:
            TranslationError: If translation fails
        """
        if not text or not text.strip():
            return text
        
        try:
            # Skip translation if text is already in Korean (simple heuristic)
            if self._is_korean(text):
                return text
            
            translated = self.translator.translate(text, target=target_language)
            return translated if translated else text
            
        except Exception as e:
            raise TranslationError(f"번역 실패: {str(e)}")
    
    def _is_korean(self, text: str) -> bool:
        """Check if text contains Korean characters."""
        korean_chars = 0
        total_chars = len([c for c in text if c.isalpha()])
        
        if total_chars == 0:
            return False
        
        for char in text:
            if '\uac00' <= char <= '\ud7af':  # Korean syllables
                korean_chars += 1
        
        # If more than 50% of alphabetic characters are Korean, consider it Korean
        return korean_chars / total_chars > 0.5
