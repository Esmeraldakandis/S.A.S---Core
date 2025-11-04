class EmotionalDeltaTracker:
    def __init__(self):
        self.history = []

    def record(self, vector):
        """Store a snapshot of the emotional vector."""
        self.history.append(vector[:])  # store a copy

    def get_delta(self):
        """Return the change between the last two emotional states."""
        if len(self.history) < 2:
            return [0.0, 0.0, 0.0]
        prev = self.history[-2]
        curr = self.history[-1]
        return [curr[i] - prev[i] for i in range(3)]

    def is_spiking(self, threshold=0.5):
        """Detect if any emotional dimension changed too rapidly."""
        delta = self.get_delta()
        return any(abs(d) > threshold for d in delta)
