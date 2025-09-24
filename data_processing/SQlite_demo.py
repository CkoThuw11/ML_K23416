import sqlite3
import pandas as pd

n = int(input("Please enter top number of customer you want to sho10w: "))
try:
    sqliteConnection = sqlite3.connect('databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print("DB Init")

    query = 'SELECT CustomerId, SUM(total) FROM Invoice GROUP BY CustomerId ORDER BY SUM(total) DESC'
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall())
    df.columns = ['CustomerId', 'Total_value']
    print(df.head(n))

    cursor.close()
except sqlite3.Error as e:
    print("Error occured - ", e)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite Connection closed")