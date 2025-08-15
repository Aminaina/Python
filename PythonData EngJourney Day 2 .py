#!/usr/bin/env python
# coding: utf-8

# Python Data Engineering Journey - Day 1
# Variables, Data Types, and Basic Operations
# 

# In[1]:


#Exercise 5: Data Type Conversion Challenge
#Handle mixed data types from a CSV-like source:
# Simulate CSV data (all strings initially)
csv_row = ["12345", "Alice Smith", "28", "75000.50", "true", "2024-01-15", "Engineering,Python,Data"]

# Column definitions
columns = ["id", "name", "age", "salary", "active", "hire_date", "skills"]
column_types = [int, str, int, float, bool, str, list]

# TODO: Convert each field to its appropriate type
# Handle the boolean conversion ("true"/"false" strings)
# Split the skills field into a list
# Create a dictionary mapping column names to converted values


# In[7]:


def converted_def(row, column, column_type):
    result = {}
    for column, value, types in zip(columns, csv_row, column_types):
        try:
            if types == bool :
                    converted = value.lower() == "true"
            elif types == list:
                     converted = value.split(',')
            else:
                     converted = types(value)
            result[column] = converted
        except (ValueError, AttributeError) as e:
                Print(f"Error converted {column} with value {value} : {e}")
                result[column] = None
    return result

employee_data = converted_def(csv_row, columns, column_types)
        
print(employee_data)    
    


# In[87]:


#Exercise 6: Log File Analysis
# TODO: Parse each log entry and extract:
# 1. IP address
# 2. HTTP method (GET, POST, DELETE)
# 3. Endpoint/URL
# 4. Status code (convert to integer)
# 5. Response time (convert to float)
log_entries = [
    "192.168.1.100 - GET /api/users 200 0.45",
    "10.0.0.1 - POST /api/login 401 0.12",
    "192.168.1.100 - GET /api/products 200 1.23",
    "203.0.113.5 - GET /api/users 404 0.08",
    "10.0.0.1 - POST /api/login 200 0.34",
    "192.168.1.100 - DELETE /api/products/123 500 2.1",
    "203.0.113.5 - GET /api/dashboard 200 0.67"
]
def log_analys (log_entrie):
    disc_log = []
    for log in log_entries:
        listlog = log.split()
        try:
            disc_log.append({
                  "ip": listlog[0],
                   "method": listlog[2],
                    "endpoint": listlog[3] ,
                    "status": int(listlog[4]),
                    "response_time":float(listlog[5]) 
                    })
    
        except (IndexError, ValueError) as e:
             Print(f"skipping malformd entry {log} with Error {e}")
              
    return disc_log
log_list = log_analys (log_entries)        
print(log_list)
#Then calculate:
# 1. Total number of requests
total = len(log_list)
print(f"Total number of requests {total} ")
# 2. Number of successful requests (status 200-299)
successful_requests = sum(1 for log in log_list if 200 <= log["status"] < 300)
print( f"Number of successful requests {successful_requests}")
# 3. Number of error requests (status 400+)
error_requests = sum(1 for log in log_list if log["status"] >= 400)
print( f"Number of error requests {error_requests}")
# 4. Average response time
import numpy as np
listt = []
for  log in log_list: 
     listt.append(log["response_time"])
Average = np.mean(listt)
print(f"Average response time {Average:.2f}")
# 5. Most frequent IP address
from collections import Counter 
ips = Counter([log["ip"] for log in log_list  ])
most_frequent_ip = ips.most_common(1)[0][0]
print(f"Most frequent IP address: {most_frequent_ip} ")
# 6. Most frequent endpoint
endpoint = [log["endpoint"] for log in log_list]
Most_frequent_endpoint = Counter(endpoint).most_common(1)[0][0]
print(Most_frequent_endpoint)
# 7. Slowest request (highest response time)
response_time = [log["response_time"] for log in log_list]
print(f"Slowest request: {max(response_time)} ")


# Exercise 7: E-commerce Product Catalog
# Manage product data with various data types and operations:

# In[177]:


# Product data from different sources
products = [
   ("P001", "Laptop", "Electronics", 999.99, 15, True),
   ("P002", "Coffee Mug", "Kitchen", 12.50, 50, True),
   ("P003", "Phone Case", "Accessories", 25.00, 0, False),
   ("P004", "Desk Chair", "Furniture", 299.99, 8, True),
   ("P005", "Notebook", "Office", 5.99, 100, True)
]

# Column names for reference
columns = ["product_id", "name", "category", "price", "stock", "active"]

# TODO: Convert the tuple data to a more workable format and:
# 1. Create a list of dictionaries (one dict per product)

def convert_tuple(columns, products):
   list_dic = []
   for  product in products:
       try:
               list_dic.append(
                  {columns[0]:  product[0],
                   columns[1]:  product[1],
                   columns[2]:  product[2],
                   columns[3]:  product[3],
                   columns[4]:  product[4],
                   columns[5]:  product[5],
                   })
               
       except(IndexError, ValueError) as e:
                 print(f"Error in column {Columns} with error {e}")
   return list_dic
list_dict = convert_tuple(columns,products)
print(convert_tuple(columns,products))

# 2. Find all products in stock (stock > 0)
in_stock = [product["name"] for product in list_dict if product["stock"] > 0 ]
print(f"Find all products in stock: {in_stock}" )
   
# 3. Calculate total inventory value (price * stock for all products)
tota_ventory = sum(product["price"] * product["stock"] for product in list_dict)
print(f"total inventory: {tota_ventory}" )
# 4. Find the most expensive product
#method1
exp_prod = [product["name"] for product in list_dict if product["price"] == max(product["price"]for product in list_dict )]

print(f"the most expensive product: {exp_prod}")
#method2
mos_exp = max(list_dict, key = lambda x:x["price"])
print(f"expense prod: {mos_exp['name']}")
# 5. Group products by category (create a dictionary with categories as keys)
#method1
from collections import defaultdict
grouped = defaultdict(list)
for product in list_dict:
   category = product["category"]
   grouped[category].append(product["name"])
grouprd_dict = dict(grouped)
print(grouprd_dict)
#method2
import pandas as pd 
df = pd.DataFrame(list_dict)
df_dict = df.groupby("category")["name"].apply(list).to_dict()
print(f"Group products by category {df_dict}")
# 6. Find products that need restocking (stock < 10)
need_restocking = df[df["stock"] < 10]["name"].tolist()
print(f"products that need restocking: {need_restocking}")
# 7. Calculate average price per category
average_price = df.groupby("category")["price"].mean()
print(f"average price per category: {average_price}")
# 8. Create a "low stock alert" list with product names where stock < 5
def low_stock_alert(dataframe):
   low_stock = dataframe[dataframe["stock"] < 5 ]["name"].tolist()
   return low_stock
lowstock = low_stock_alert(df)
print(f"a low stock alert to these products {lowstock}")


# In[ ]:




