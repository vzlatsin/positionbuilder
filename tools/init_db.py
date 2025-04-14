import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.db.database_manager import DatabaseManager

def initialize_database():
    db = DatabaseManager()
    db.execute_script("migrations/001_create_insights_table.sql")
    print("✅ Database initialized.")

if __name__ == "__main__":
    initialize_database()
