class EmotionalVector:
    def __init__(self, tone=0.0, trust=0.0, volatility=0.0):
        self.tone = tone        # -1 (hostile) to +1 (friendly)
        self.trust = trust      # 0 (no trust) to +1 (full trust)
        self.volatility = volatility  # 0 (stable) to +1 (chaotic)

    def as_vector(self):
        return [self.tone, self.trust, self.volatility]

    def update(self, delta_tone=0.0, delta_trust=0.0, delta_volatility=0.0):
        self.tone = max(-1.0, min(1.0, self.tone + delta_tone))
        self.trust = max(0.0, min(1.0, self.trust + delta_trust))
        self.volatility = max(0.0, min(1.0, self.volatility + delta_volatility))

    def __str__(self):
        return f"Tone: {self.tone:.2f}, Trust: {self.trust:.2f}, Volatility: {self.volatility:.2f}"
