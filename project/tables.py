import pandas as pd
from database import fetch_data

# Create your tables as Pandas DataFrames
table1 = fetch_data('select * from accounts')
table2 = fetch_data('select * from customers_cards')
table3 = fetch_data('select * from customers')
table4 = fetch_data('select * from financial_transactions')