
import mysql.connector
import pandas as pd

def fetch_data(user_query):
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@May211999",
        database="customers_card_transactions"
    )
    
    # Create a cursor to interact with the database
    cursor = connection.cursor()  
    # Execute the SQL query
    cursor.execute(user_query)    
    # Fetch the results
    results = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
    # Close the cursor and the database connection when done
    cursor.close()
    connection.close() 
    
    return results



# print(fetch_data("SELECT * FROM customers_cards"))