#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Desktop Notifier for COVID-19


# In[2]:


from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
from datetime import date


# In[3]:


today = date.today()


# In[4]:


year = today.year
month = today.month
date = today.day


# In[5]:


year


# In[6]:


month


# In[7]:


date


# In[8]:


header = {'User-Agent':'Mozilla'}
req = Request('https://www.worldometers.info/coronavirus/country/india/',headers=header)
html = urlopen(req)


# In[9]:


html.status


# In[10]:


obj = bs(html)


# In[11]:


new_cases = obj.find('li',{'class':'news_li'}).strong.text.split()[0]


# In[12]:


new_cases


# In[13]:


deaths = list(obj.find('li',{'class':'news_li'}).strong.next_siblings)[1].text.split()[0]


# In[14]:


deaths


# In[15]:


notifier = ToastNotifier()


# In[16]:


message = 'New Cases - '+new_cases+'\nDeaths - '+deaths+'\non '+str(date)+'-'+str(month)+'-'+str(year)


# In[17]:


message


# In[18]:


notifier.show_toast(title='COVID-19 UPDATES',msg = message,duration=5,icon_path=r'virus.ico')


# In[ ]:




