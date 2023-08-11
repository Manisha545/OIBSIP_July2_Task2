#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing


# In[2]:


import os
for dirname, _, filenames in os.walk(r'C:\Users\manis\Downloads\archive (1)'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[3]:


import datetime as dt

import plotly.io as pio
pio.templates


# In[4]:


import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from IPython.display import HTML


# In[5]:


df = pd.read_csv(r'C:\Users\manis\Downloads\archive (1)\Unemployment_Rate_upto_11_2020.csv')


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df.columns =['States','Date','Frequency','Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate','Region','longitude','latitude']


# In[10]:


df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)


# In[11]:


df['Frequency']= df['Frequency'].astype('category')


# In[12]:


df['Month'] =  df['Date'].dt.month


# In[13]:


df['Month_int'] = df['Month'].apply(lambda x : int(x))


# In[14]:


import calendar
df['Month_name'] =  df['Month_int'].apply(lambda x: calendar.month_abbr[x])


# In[15]:


df['Region'] = df['Region'].astype('category')


# In[16]:


df.drop(columns='Month',inplace=True)
df.head(3)


# In[17]:


df_stats = df[['Estimated Unemployment Rate',
      'Estimated Employed', 'Estimated Labour Participation Rate']]


round(df_stats.describe().T,2)


# In[18]:


region_stats = df.groupby(['Region'])[['Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate']].mean().reset_index()

region_stats = round(region_stats,2)


region_stats


# In[19]:


fig = px.box(df,x='States',y='Estimated Unemployment Rate',color='States',title='Unemployment rate',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()

# The below box shows unemployement rate in each state in India


# In[20]:


fig = px.scatter_matrix(df,template='plotly',
    dimensions=['Estimated Unemployment Rate','Estimated Employed',
                'Estimated Labour Participation Rate'],
    color='Region')
fig.show()


# In[21]:


plot_ump = df[['Estimated Unemployment Rate','States']]

df_unemp = plot_ump.groupby('States').mean().reset_index()

df_unemp = df_unemp.sort_values('Estimated Unemployment Rate')

fig = px.bar(df_unemp, x='States',y='Estimated Unemployment Rate',color='States',
            title='Average Unemployment Rate in each state',template='plotly')

fig.show()


# In[22]:


fig = px.bar(df, x='Region',y='Estimated Unemployment Rate',animation_frame = 'Month_name',color='States',
            title='Unemployment rate across region from Jan.2020 to Oct.2020', height=700,template='plotly')

fig.update_layout(xaxis={'categoryorder':'total descending'})

fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 2000

fig.show()


# In[23]:


unemplo_df = df[['States','Region','Estimated Unemployment Rate','Estimated Employed','Estimated Labour Participation Rate']]

unemplo = unemplo_df.groupby(['Region','States'])['Estimated Unemployment Rate'].mean().reset_index()


# In[24]:


fig = px.sunburst(unemplo, path=['Region','States'], values='Estimated Unemployment Rate',
                  color_continuous_scale='Plasma',title= 'unemployment rate in each region and state',
                  height=650,template='ggplot2')


fig.show()


# In[ ]:





# In[ ]:




