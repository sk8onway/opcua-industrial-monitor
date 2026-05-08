import sqlite3

def initialize_database():
    """Initialize the SQLite database and create the telemetry table if it doesn't exist."""
    conn = sqlite3.connect('telemetry.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            variable_id TEXT NOT NULL,
            value REAL NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_value(timestamp, variable_id, value):
    """Insert a telemetry record into the database."""
    conn = sqlite3.connect('telemetry.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO telemetry (timestamp, variable_id, value)
        VALUES (?, ?, ?)
    ''', (timestamp, variable_id, value))
    
    conn.commit()
    conn.close()

# initialize_database()