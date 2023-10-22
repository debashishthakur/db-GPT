#!/usr/bin/env python
# coding: utf-8

# In[3]:


import transformers
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# Load the model
model_name = "tscholak/1wnr382e"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# In[19]:


# user_query = "Tell me the first name of a customer whose adress is 094 Julianne Mill\nWebstertown, KY 91980-4004."
db_id = "customers_card_transactions"
tables_and_columns = "Accounts: account_id, customer_id, account_name, other_account_details | Customers: customer_id, customer_first_name, customer_last_name, customer_address, customer_phone, customer_email, other_customer_details | Customers_Cards: card_id, customer_id, card_type_code, card_number, date_valid_from, date_valid_to, other_card_details | Financial_Transactions: transaction_id, previous_transaction_id, account_id, card_id, transaction_type, transaction_date,transaction_amount, transaction_comment, other_transaction_details"


# In[22]:


def generate_sql_query(user_query: str):
    input_text = f"{user_query} | {db_id} | {tables_and_columns}"
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate SQL query
    with torch.no_grad():
        sql_query = model.generate(**inputs)
        
    decoded_query = tokenizer.batch_decode(sql_query)
    decoded = decoded_query[0]  # Get the first element from the list
    parts = decoded.split('|')
    sql_query = parts[1].strip().replace('</s>', '')  # Get the text after "|", and remove leading/trailing whitespace
    return sql_query


# In[23]:


generate_sql_query("Tell me the last name of a customer whose adress is 094 Julianne Mill\nWebstertown, KY 91980-4004.")


# In[24]:





# In[ ]:




