class InsightMatcher:
    def __init__(self, insights):
        self.insights = insights

    def match(self, trade_plan):
        results = []
        for insight in self.insights:
            common_tags = set(insight.tags).intersection(trade_plan.tags)
            results.append((insight, len(common_tags), common_tags))
        return results
