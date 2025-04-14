class Insight:
    def __init__(self, text, tags, confidence, time_horizon):
        self.text = text
        self.tags = tags
        self.confidence = confidence
        self.time_horizon = time_horizon

    def __repr__(self):
        return f"Insight(text='{self.text}', tags={self.tags})"
