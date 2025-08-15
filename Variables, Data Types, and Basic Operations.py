#!/usr/bin/env python
# coding: utf-8

# Exercise 1: Customer Data Processing

# In[14]:


customer_id = 12234
customer_name = "Ahmed Omar"
email = "Amhed.mar@gd.com"
age = 32
account_balance = 15775.5
is_premium = True
purchase_history = [99.99, 149.50, 75.25, 200.00]


# In[25]:


import numpy as np
import pandas as pd 
Total_amount_spent = sum(purchase_history)
Average_purchase = np.mean(purchase_history)
Number_of_purchases  = len(purchase_history)

#create a formatted string: "Customer {name} (ID: {id}) has spent ${total:.2f}"
print(f"Customer {customer_name} (ID: {customer_id}) has spent ${Total_amount_spent:.2f}")


# In[26]:


# Raw data from different sources
raw_data = {
    "user_id": "  12345  ",
    "username": "JOHN_DOE",
    "email": "John.Doe@EXAMPLE.COM",
    "age": "28",
    "salary": "75000.50",
    "active": "true",
    "tags": "python,data,engineer"
}


# In[46]:


# TODO: Clean and convert the data:
# 1. Strip whitespace from user_id and convert to integer
# 2. Convert username to lowercase
# 3. Convert email to lowercase
# 4. Convert age to integer
# 5. Convert salary to float
# 6. Convert active to boolean (handle "true"/"false" strings)
# 7. Split tags into a list
# 8. Store cleaned data in a new dictionary
#1 
raw_data["user_id"].strip()
#2
raw_data["username"].lower()
#3
raw_data["email"].lower()
#4
int(raw_data["age"])
#5
float(raw_data["salary"])
#6
#raw_data["active"] = raw_data["active"].lower() == "true"
#7
raw_data["tags"].split(",")
#8
clean_data = {
     "user_id": raw_data["user_id"].strip(),
    "username": raw_data["username"].lower(),
    "email": raw_data["email"].lower(),
    "age": int(raw_data["age"]),
    "salary": float(raw_data["salary"]),
    "active": raw_data["active"],
    "tags": raw_data["tags"].split(",")
}


# In[44]:


raw_data


# In[47]:


clean_data


# In[10]:


# Monthly sales data
monthly_sales = [12500, 15750, 18200, 16800, 19500, 22100, 20800, 18900, 21200, 19800, 23400, 25600]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# TODO: Calculate and display:
# 3. Best performing month (highest sales)
max(monthly_sales)
monthly_sales.index(max(monthly_sales))
print(f" Best performing month {months[monthly_sales.index(max(monthly_sales))]} ")
# 4. Best performing month (lowest sales)
print(f" Best performing month {months[monthly_sales.index(min(monthly_sales))]} ")
# 5. Quarter-wise sales (Q1: Jan-Mar, Q2: Apr-Jun, etc.)


# 6. Months with above-average sales


# In[13]:


def Q1_total_sales(monthly_sales):
    sales = 0
    for i in range(3):
        sales = sales + monthly_sales[i]
    return sales
print(Q1_total_sales(monthly_sales))


# In[14]:


def Q2_total_sales(monthly_sales):
    sales = 0
    for i in range(3, 6):
        sales = sales + monthly_sales[i]
    return sales
print(Q2_total_sales(monthly_sales))


# In[15]:


def Q3_total_sales(monthly_sales):
    sales = 0
    for i in range(6, 9):
        sales = sales + monthly_sales[i]
    return sales
print(Q3_total_sales(monthly_sales))


# In[16]:


def Q4_total_sales(monthly_sales):
    sales = 0
    for i in range(9, 12):
        sales = sales + monthly_sales[i]
    return sales
print(Q4_total_sales(monthly_sales))


# In[23]:


# Simulate CSV data (all strings initially)
csv_row = ["12345", "Alice Smith", "28", "75000.50", "true", "2024-01-15", "Engineering,Python,Data"]

# Column definitions
columns = ["id", "name", "age", "salary", "active", "hire_date", "skills"]
column_types = [int, str, int, float, bool, str, list]

# TODO: Convert each field to its appropriate type
# Handle the boolean conversion ("true"/"false" strings)
# Split the skills field into a list
# Create a dictionary mapping column names to converted values

def convert_row (row, column, types):
    result = {}
    for col_name, value, col_type in zip( column,row, types):
        try:
            if col_type == bool:
                converted = value.lower() == "true"
            elif col_type == list:
                converted =value.split(',')
            else:
                converted = col_type(value)
            result[col_name] = converted
        except (valueError, AttributeError) as e:
            print(f"Error converting {col_name} with value {value}")
            result[col_name] = None
    return result

emplyee_data = convert_row (csv_row, columns, column_types)
print(emplyee_data)

