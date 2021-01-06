#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup



# In[3]:


url = 'https://www.weatherzone.com.au/world/africa/egypt/cairo'
response = requests.request('GET', url)
print(response.text)


# In[4]:


soup = BeautifulSoup(response.text, 'html.parser')
print(soup)


# In[5]:


data = soup.find_all('div', attrs={'class':'content'})
for d in data:
    print(d)
    print('\n')


# In[6]:


data_a = data[0].find('div').text
print(data_a)


# In[7]:


nu = data_a.split()
print(nu)


# In[8]:


cairo = nu[23]
print(cairo)


# In[9]:


from datetime import datetime


# In[10]:


now = datetime.now()
time_now = now.strftime("%d-%m-%Y")
print(time_now)


# In[ ]:


import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

while True:
    url = 'https://www.weatherzone.com.au/world/africa/egypt/cairo'
    response = requests.request('GET', url)

    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup.find_all('div', attrs={'class':'content'})

    data_a = data[0].find('div').text

    nu = data_a.split()

    cairo = nu[23]

    print(cairo)
    
    f = open('degree.txt', 'a')
    now = datetime.now()
    time_now = now.strftime("%d/%m/%Y")
    output = 'Total degree= '+cairo+'\n\n'
    f.write(output)
    f.close()
    time.sleep(600)

    


# In[ ]:




