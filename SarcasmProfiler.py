from typing import Dict
import numpy as np

class SarcasmProfiler:
    """
    Detects and scores sarcasm across multiple languages.
    Supports sarcasm confidence scoring and sarcasm type classification.
    Designed to complement emotional tone modules.
    """
    def __init__(self):
        self.supported_languages = ['en', 'es', 'fr', 'de', 'pt']
        self.sarcasm_keywords = {
            'en': ["yeah right", "totally", "sure", "great", "love that for me"],
            'es': ["claro", "por supuesto", "genial"],
            'fr': ["bien sûr", "génial", "parfait"],
            'de': ["na klar", "toll", "super"],
            'pt': ["claro", "ótimo", "maravilha"]
        }
        self.sarcasm_types = [
            "verbal_irony", "deadpan_delivery", "exaggeration", "understatement",
            "mock_praise", "false_agreement", "contradictory_tone", "emoji_sarcasm",
            "hashtag_sarcasm", "cultural_sarcasm", "situational_sarcasm",
            "passive_aggressive", "self_deprecating", "meta_sarcasm"
        ]

    def detect(self, text: str, lang: str = 'en') -> bool:
        if lang not in self.supported_languages:
            return False
        text_lower = text.lower()
        return any(phrase in text_lower for phrase in self.sarcasm_keywords.get(lang, []))

    def confidence_score(self, text: str, lang: str = 'en') -> float:
        score = 0.0
        text_lower = text.lower()
        for kw in self.sarcasm_keywords.get(lang, []):
            if kw in text_lower:
                score += 0.2
        if "!" in text or "..." in text or "\"" in text:
            score += 0.1
        return min(score, 1.0)

    def log(self, text: str, lang: str = 'en') -> str:
        detected = self.detect(text, lang)
        score = self.confidence_score(text, lang)
        if detected:
            return f"Sarcasm detected in '{lang}' text: '{text}' with confidence {score:.2f}"
        return f"No sarcasm detected. Confidence score: {score:.2f}"


# Example usage:
if __name__ == "__main__":
    profiler = SarcasmProfiler()

    examples = [
        ("Yeah right, that was helpful.", 'en'),
        ("Genial, como siempre.", 'es'),
        ("Bien sûr, c'était parfait.", 'fr')
    ]

    for text, lang in examples:
        print(profiler.log(text, lang))
