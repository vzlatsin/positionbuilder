import argparse
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.db.database_manager import DatabaseManager

def add_insight(text, tags, confidence, horizon, implication):
    db = DatabaseManager()
    query = """
        INSERT INTO insights (text, tags, confidence, time_horizon, implication)
        VALUES (?, ?, ?, ?, ?)
    """
    tag_str = ",".join(tags)
    db.execute_query(query, (text, tag_str, confidence, horizon, implication))
    print("✅ Insight added.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a new insight to the journal.")
    parser.add_argument("--text", required=True, help="The main insight text")
    parser.add_argument("--tags", required=True, help="Comma-separated list of tags")
    parser.add_argument("--confidence", default="Medium", help="Confidence level (e.g., High, Medium, Low)")
    parser.add_argument("--horizon", default="3M", help="Time horizon (e.g., 1M, 3M, 6M+)")
    parser.add_argument("--implication", default="", help="Optional implication for the portfolio")

    args = parser.parse_args()
    tags = [t.strip() for t in args.tags.split(",")]
    add_insight(args.text, tags, args.confidence, args.horizon, args.implication)
