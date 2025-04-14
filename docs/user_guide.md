# PositionBuilder — User Guide

PositionBuilder is your personal trading assistant. It helps align portfolio decisions with structured macro insights or "edges" that you record over time.

---

## Features

- Save structured insights to a local database
- Review your journal of macro or strategic beliefs
- Align trade plans with your stored insights
- Build toward scoring, simulation, and strategy automation

---

## How to Use

1. Add an Insight

Example command:

python tools/add_insight.py --text "Market is down but rates remain high" --tags inflation,high_rates,risk_off --confidence High --horizon 6M --implication "Prefer commodities and value stocks"

Arguments:
--text : Your thesis or observation  
--tags : Comma-separated labels (no spaces)  
--confidence : High / Medium / Low  
--horizon : Timeframe (e.g., 3M, 6M+)  
--implication : How it might affect portfolio positioning

---

2. View Saved Insights

Run this:

python tools/list_insights.py

Displays all insights stored in the database, from most recent to oldest.

---

## Project Structure

positionbuilder/
├── core/
│   ├── insights/       # Insight objects and logic
│   ├── trades/         # Trade planning & matcher
│   └── db/             # Database manager class
├── tools/              # Command-line tools
├── migrations/         # SQL schema
├── tests/              # Unit tests (pytest)
├── docs/               # Documentation
├── positionbuilder.db  # SQLite database
├── main.py             # (Optional) Entry point
└── requirements.txt

---

## Initialize the Database

To set up the SQLite database:

python tools/init_db.py

This creates positionbuilder.db using the schema in migrations/001_create_insights_table.sql

---

## Coming Soon

- Add trade plans and match them to insights
- Score how well trades align with beliefs
- Recommend positioning ideas
- Simulate strategies and track performance
