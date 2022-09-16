#!/usr/bin/env python
# coding: utf-8

# In[27]:


from bs4 import BeautifulSoup as bs #module used in python for scrapping


# In[28]:


import requests #it will used to send a request to the webpage


# In[32]:


link="https://www.flipkart.com/mobile-mart-back-cover-oneplus-6t-7/p/itmfba4ptmpvqghz?pid=ACCFBA3HWSJYZ3RT&lid=LSTACCFBA3HWSJYZ3RTO2QSAD&marketplace=FLIPKART&store=tyy%2F4mr%2Fq2u&srno=b_1_3&otracker=browse&iid=708ddf9c-2f8f-4d62-a75c-584d81eb1fe9.ACCFBA3HWSJYZ3RT.SEARCH&ssid=ox0h40e3680000001663293777522"


# In[33]:


page=requests.get(link) #sending request to the webpage and keeping the data in a variable page


# In[34]:


page


# In[35]:


page.content


# In[36]:


soup=bs(page.content,"html.parser") #getting content in correct form


# In[37]:


print(soup)


# In[40]:


names=soup.find_all("p",class_="_2-N8zT") #find_all is used to give parameters tag and class name that present everywhere,class_ default parameter


# In[41]:


names


# In[62]:


#for getting only names but not tagnames and class names
cust_names=[]
for i in range(len(names)):
    cust_names.append(names[i].get_text()) #get_text is a function used to get only text
    


# In[63]:


cust_names


# In[64]:


cust_reviews=soup.find_all("div",class_="t-ZTKy")


# In[65]:


cust_reviews


# In[66]:


#for getting only text (customer reviews)
reviews=[]
for i in range(len(cust_reviews)):
    reviews.append(cust_reviews[i].get_text())


# In[67]:


reviews


# In[68]:


#if \n exists, to remove that \n - strip functions can be used 
#customer_reviews=[i.strip(""\n\n")for i in reviews]


# In[69]:


cust_names


# In[70]:


import pandas as pd


# In[71]:


df=pd.DataFrame()


# In[72]:


df["name of customer"]=cust_names
df["customer review"]=reviews


# In[73]:


df


# In[78]:


data=df.to_csv("C:\\Users\\Syam Prabath\\OneDrive\\Documents\\webscrapping.csv")


# In[ ]:




