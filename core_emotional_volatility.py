
from typing import List, Dict
import numpy as np

class VolatilityAnalyzer:
    """
    Tracks emotional volatility based on tone and trust vectors over time.
    Flags unstable emotional patterns.
    """
    def __init__(self, history_window: int = 5):
        self.history_window = history_window
        self.tone_history: List[np.ndarray] = []
        self.trust_history: List[np.ndarray] = []

    def update(self, tone_vector: np.ndarray, trust_vector: np.ndarray):
        self.tone_history.append(tone_vector)
        self.trust_history.append(trust_vector)

        if len(self.tone_history) > self.history_window:
            self.tone_history.pop(0)
            self.trust_history.pop(0)

    def calculate_volatility(self) -> float:
        if len(self.tone_history) < 2:
            return 0.0

        tone_changes = [np.linalg.norm(self.tone_history[i] - self.tone_history[i-1])
                        for i in range(1, len(self.tone_history))]
        trust_changes = [np.linalg.norm(self.trust_history[i] - self.trust_history[i-1])
                         for i in range(1, len(self.trust_history))]

        volatility_score = np.mean(tone_changes + trust_changes)
        return volatility_score

    def is_unstable(self, threshold: float = 1.5) -> bool:
        return self.calculate_volatility() > threshold


class ToneTranslator:
    """
    Converts tone vectors into readable emotional summaries.
    """
    def __init__(self):
        self.emotion_labels = ['Calm', 'Frustrated', 'Hopeful', 'Anxious', 'Confident']

    def translate(self, tone_vector: np.ndarray) -> str:
        dominant_index = int(np.argmax(tone_vector))
        dominant_emotion = self.emotion_labels[dominant_index]
        confidence = tone_vector[dominant_index]

        return f"Tone is '{dominant_emotion}' with confidence level {confidence:.2f}."


# Example usage:
if __name__ == "__main__":
    analyzer = VolatilityAnalyzer()
    translator = ToneTranslator()

    # Simulated tone and trust vectors
    tone_vecs = [np.array([0.1, 0.3, 0.2, 0.1, 0.3]),
                 np.array([0.2, 0.4, 0.1, 0.1, 0.2]),
                 np.array([0.3, 0.2, 0.1, 0.2, 0.2])]

    trust_vecs = [np.array([0.5, 0.5]),
                  np.array([0.4, 0.6]),
                  np.array([0.3, 0.7])]

    for tone, trust in zip(tone_vecs, trust_vecs):
        analyzer.update(tone, trust)
        print(translator.translate(tone))

    print("Volatility Score:", analyzer.calculate_volatility())
    print("Is Unstable:", analyzer.is_unstable())
