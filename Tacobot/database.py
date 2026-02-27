import sqlite3
import json

conn = sqlite3.connect("restaurant_reservations.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tables (
    table_number INTEGER PRIMARY KEY,
    is_booked INTEGER DEFAULT 0,  
    customer_name TEXT,
    phone_number TEXT ,
    date_time TEXT
    
)
''')

cursor.executemany('''
INSERT OR IGNORE INTO tables (table_number, is_booked) VALUES (?, ?)
''', [(i, 0) for i in range(1, 11)])  

conn.commit()
conn.close()
#print("Tables initialized.")

def check_and_book_table(name, phone, date_time):
    conn = sqlite3.connect("restaurant_reservations.db")
    cursor = conn.cursor()

    # Check for an available table
    cursor.execute("SELECT table_number FROM tables WHERE is_booked = 0 LIMIT 1")
    table = cursor.fetchone()

    if table:
        table_number = table[0]

        # Book the table: update the `tables` and `reservations` tables
        cursor.execute('''UPDATE tables 
                       SET is_booked = 1,
                       customer_name =?,
                       phone_number = ?,
                       date_time = ?
                       WHERE table_number = ?''',(name,phone,date_time,table_number,))
        conn.commit()
        conn.close()
        return f"Table {table_number} has been booked for {name} on {date_time}."
    else:
        conn.close()
        return "Sorry, all tables are currently booked."
    
def cancel_reservation(phone):
    conn = sqlite3.connect("restaurant_reservations.db")
    cursor = conn.cursor()

    # Find the reservation by phone number
    cursor.execute("SELECT table_number FROM tables WHERE phone_number = {}".format(phone))
    reservation = cursor.fetchone()

    if reservation:
        table_number = reservation[0]

        # Remove the reservation and mark the table as available
        cursor.execute("DELETE FROM tables WHERE phone_number = {}".format(phone,))
        cursor.execute("UPDATE tables SET is_booked = 0 WHERE table_number = ?", (table_number,))
        conn.commit()
        conn.close()
        return f"Reservation for phone number {phone} has been canceled. Table {table_number} is now available."
    else:
        conn.close()
        return "No reservation found for the given phone number."


