#JUSTIN ISARAPHANICH 9/3/2025 LAST MODIFIED
#VERIFY THE DATABASE FILE, PRINT THE TABLES

import sqlite3

conn = sqlite3.connect('instance/satellite.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Check Data table structure
cursor.execute("PRAGMA table_info(data);")
print("\nData table columns:", cursor.fetchall())

# Check Positions table structure  
cursor.execute("PRAGMA table_info(positions);")
print("\nPositions table columns:", cursor.fetchall())

conn.close()