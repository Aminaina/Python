#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd 


# In[140]:


df = pd.read_csv(
                r'C:\Users\Käyttäjä\OneDrive - LUT University\Documents 1\data_analytics\Projects_2025\AirBnB Listing Analysis\Airbnb+Data\Airbnb Data\Listings.csv',

            encoding= 'ISO-8859-1',
            low_memory=False

)


# In[141]:


df.head()


# In[142]:


# Convert host_since to datetime
df['host_since'] = pd.to_datetime(df['host_since'])


# In[143]:


Paris_df = df.query("city == 'Paris'").loc[:, ['host_since', 'neighbourhood', 'city', 'accommodates',  'price']]


# In[144]:


Paris_df.info()


# In[145]:


Paris_df.isna().sum()


# In[146]:


Paris_df.describe()


# In[147]:


Paris_df.query("price == 0").count()


# In[148]:


Paris_df.query("accommodates == 0").count()


# In[149]:


paris_listings_neighbourhood  = Paris_df.groupby('neighbourhood')['price'].mean().reset_index(name = 'avg_price').sort_values('avg_price')
paris_listings_neighbourhood


# In[150]:


Most_expense_neighborhood = Paris_df.groupby('neighbourhood')['price'].mean().idxmax()
filter_m_e_neighborhood = Paris_df.query("neighbourhood == @Most_expense_neighborhood")
filter_m_e_neighborhood


# In[151]:


paris_listings_accomodations = filter_m_e_neighborhood.groupby('accommodates')['price'].mean().reset_index(name = 'avg_price').sort_values('avg_price')
paris_listings_accomodations    


# In[152]:


Paris_listings_over_time = Paris_df.set_index('host_since').resample('y').agg(
{'price':'mean',
 'neighbourhood': 'count'})


# In[153]:


Paris_listings_over_time


# In[138]:


import matplotlib.pyplot as plt


# In[158]:


paris_listings_neighbourhood


# In[193]:


import seaborn as sns
paris_listings_neighbourhood.set_index('neighbourhood').plot.barh( title = 'Average Listing Price by Paris neighbourhood',
                                  xlabel='Price (€)',
                                  ylabel= 'Neighbourhood',legend=None)

sns.despine()


# In[165]:


paris_listings_accomodations


# In[237]:


paris_listings_accomodations.plot(x = 'accommodates', kind = 'barh', legend= None, figsize=(6, 3))
plt.title(' The average price by Accommodates Number')
plt.xlabel("Average Price (€)")
plt.ylabel("Accommodated")
plt.ylim(bottom=0)

sns.despine()


# In[173]:


Paris_listings_over_time


# In[219]:


Paris_listings_over_time.plot(y='neighbourhood', kind = 'line', legend= None)
plt.title('new hosts over time')
plt.xlabel('year')
plt.ylabel('new hosts')
plt.ylim(0)
sns.despine()


# In[218]:


Paris_listings_over_time.plot(y='price', kind = 'line', legend = None, c='pink')
plt.title('Average price over time')
plt.xlabel('year')
plt.ylabel('Average price')
plt.ylim(0)
sns.despine()


# After the 2015 regulations were introduced, the average listing price increased, while the number of new hosts decreased.
# This suggests that the regulations may have made it harder or less attractive for individuals to join as new hosts, potentially driving up prices due to reduced competition and supply.
# 

# In[217]:


fig, ax = plt.subplots()
ax.plot(
  Paris_listings_over_time.index, 
 Paris_listings_over_time['neighbourhood'],
  label = 'new hosts'
 )
ax.set_ylabel('New Hosts')
ax2 = ax.twinx()
ax2.plot(
  Paris_listings_over_time.index, 
 Paris_listings_over_time['price'],
  label = 'Average Price', c = 'pink'
 )
ax2.set_ylabel('Average Price')
ax2.set_ylim(0)


# In[ ]:




