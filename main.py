import sqlite3
import json

def create_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER)''')
        print("Table created successfully")

    except Exception as e:
        print(f"Error creating table: {e}")

# Function to insert data into the SQLite database
def insert_data(conn, data):
    try:
        c = conn.cursor()
        for item in data:
            c.execute("INSERT INTO users (name, age) VALUES (?,?)", (item['name'], item['age']))
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Main function to read JSON file and store data in SQLite
def main():
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('users.db')

    # Create table if it doesn't exist
    create_table(conn)

    # Read JSON file
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Insert data into the database
    insert_data(conn, data)

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()