import sys
import os

# Add root path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.db.database_manager import DatabaseManager

def list_insights():
    db = DatabaseManager()
    query = "SELECT id, text, tags, confidence, time_horizon, implication, created_at FROM insights ORDER BY created_at DESC"
    rows = db.fetch_all(query)

    if not rows:
        print("🪹 No insights found.")
        return

    for row in rows:
        id, text, tags, confidence, horizon, implication, created_at = row
        print(f"\n🧠 Insight #{id} — {created_at}")
        print(f"Text:        {text}")
        print(f"Tags:        {tags}")
        print(f"Confidence:  {confidence}")
        print(f"Horizon:     {horizon}")
        print(f"Implication: {implication or 'N/A'}")
        print("-" * 60)

if __name__ == "__main__":
    list_insights()
