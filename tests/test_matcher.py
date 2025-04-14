import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.insights.insight import Insight
from core.trades.trade_plan import TradePlan
from core.trades.insight_matcher import InsightMatcher


def test_insight_matcher():
    insights = [
        Insight("Dividends will outperform", ["dividends", "macro"], "High", "3M"),
        Insight("Avoid tech", ["avoid", "tech"], "Medium", "1M")
    ]
    trade = TradePlan("Buy VHY ETF", ["dividends", "yield"])
    matcher = InsightMatcher(insights)

    matches = matcher.match(trade)
    assert matches[0][1] == 1
    assert matches[1][1] == 0
