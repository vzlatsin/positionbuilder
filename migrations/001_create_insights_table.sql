CREATE TABLE IF NOT EXISTS insights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    tags TEXT,
    confidence TEXT,
    time_horizon TEXT,
    implication TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
