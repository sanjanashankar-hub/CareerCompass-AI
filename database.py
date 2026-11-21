import sqlite3

def create_database():
    connection = sqlite3.connect("career_guidance.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            interest TEXT,
            skill TEXT,
            work_preference TEXT,
            score INTEGER
        )
    """)

    connection.commit()
    connection.close()

create_database()

def save_result(name, interest, skill, work_preference, score):
    connection = sqlite3.connect("career_guidance.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users
        (name, interest, skill, work_preference, score)
        VALUES (?, ?, ?, ?, ?)
    """, (name, interest, skill, work_preference, score))

    connection.commit()
    connection.close()