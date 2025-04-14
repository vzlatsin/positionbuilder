class TradePlan:
    def __init__(self, description, tags):
        self.description = description
        self.tags = tags

    def __repr__(self):
        return f"TradePlan(description='{self.description}', tags={self.tags})"
