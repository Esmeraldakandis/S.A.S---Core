class SarcasmVectorTypes:
    """
    Defines and simulates various types of sarcasm vectors.
    Useful for classification, simulation, and emotional agent training.
    """
    def __init__(self):
        self.types = {
            "verbal_irony": "Saying the opposite of what is meant.",
            "deadpan_delivery": "Emotionless tone with absurd content.",
            "exaggeration": "Over-the-top praise or criticism.",
            "understatement": "Downplaying something serious.",
            "mock_praise": "Complimenting something clearly bad.",
            "false_agreement": "Pretending to agree with something ridiculous.",
            "contradictory_tone": "Positive tone with negative context.",
            "emoji_sarcasm": "Use of 🙄, 😒, 😂 to signal sarcasm.",
            "hashtag_sarcasm": "Ironic hashtags like #blessed after a disaster.",
            "cultural_sarcasm": "Region-specific sarcasm (e.g., British dry wit).",
            "situational_sarcasm": "Sarcasm triggered by context (e.g., 'Great timing!').",
            "passive_aggressive": "Sarcasm masked as politeness.",
            "self_deprecating": "Sarcasm aimed at oneself.",
            "meta_sarcasm": "Sarcasm about sarcasm."
        }

    def list_types(self):
        return list(self.types.keys())

    def describe(self, sarcasm_type: str) -> str:
        return self.types.get(sarcasm_type, "Unknown sarcasm type.")

    def simulate(self, sarcasm_type: str) -> str:
        examples = {
            "verbal_irony": "Oh yeah, that was *super* helpful.",
            "deadpan_delivery": "I just love when my internet dies mid-meeting.",
            "exaggeration": "This is literally the best coffee in the galaxy.",
            "understatement": "It’s just a tiny scratch... on a totaled car.",
            "mock_praise": "Wow, you really nailed that... like a wrecking ball.",
            "false_agreement": "Sure, let’s all pretend that made sense.",
            "contradictory_tone": "Amazing job... for someone who didn’t try.",
            "emoji_sarcasm": "Thanks 🙄 really appreciate that.",
            "hashtag_sarcasm": "Lost my job today #blessed.",
            "cultural_sarcasm": "Oh brilliant, another rainy day in paradise.",
            "situational_sarcasm": "Perfect timing, as always.",
            "passive_aggressive": "No worries, I’ll just do your part too.",
            "self_deprecating": "I’m so good at this I should teach a class... on failure.",
            "meta_sarcasm": "Wow, such a clever sarcastic remark. Groundbreaking."
        }
        return examples.get(sarcasm_type, "No simulation available.")


# Example usage:
if __name__ == "__main__":
    vectors = SarcasmVectorTypes()
    for t in vectors.list_types():
        print(f"{t}: {vectors.describe(t)}")
        print(f"Example: {vectors.simulate(t)}\n")
