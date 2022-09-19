#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


LA=pd.read_csv("C:\\Users\\Syam Prabath\\Downloads\\LoanApprovalcsv.csv ")
LA.head()


# In[6]:


LA.duplicated().sum()


# In[7]:


LA.info()


# In[8]:


LA.isna().sum()


# In[9]:


LA.drop(["Loan_ID"],axis=1,inplace=True)


# In[10]:


LA["Loan_Status"]=LA.Loan_Status.map({"Y": 1, "N": 0})


# In[11]:


LA.head()


# In[12]:


import seaborn as sns
sns.barplot(data=LA,x='Education',y='Loan_Status')


# In[13]:


import seaborn as sns
sns.barplot(data=LA,x='Self_Employed',y='Loan_Status')


# In[14]:


import seaborn as sns
sns.barplot(data=LA,x='Loan_Status',y='Property_Area')


# In[15]:


import seaborn as sns
sns.barplot(data=LA,x='Gender',y='Loan_Status')


# In[16]:


import seaborn as sns
sns.barplot(data=LA,x='Married',y='Loan_Status')


# In[17]:


loan_approval=pd.get_dummies(LA)


# In[18]:


loan_approval.head()


# In[19]:


y=loan_approval.Loan_Status.values
y


# In[20]:


loan_approval.drop("Loan_Status",axis=1,inplace=True)


# In[21]:


x=loan_approval.values
x


# In[22]:


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)


# In[23]:


from sklearn.ensemble import RandomForestClassifier


# In[24]:


rand_for=RandomForestClassifier(n_estimators=500,max_depth=7,min_samples_split=3,random_state=42)


# In[25]:


rand_for.fit(x_train,y_train)


# In[26]:


rand_for.score(x_train,y_train)


# In[27]:


rand_for.score(x_test,y_test)


# In[28]:


rand_for.score(x,y)


# In[29]:


y_pred=rand_for.predict(x_test)


# In[30]:


y_pred


# In[31]:


y_test


# In[35]:


from sklearn.metrics import confusion_matrix

cm_df = pd.DataFrame(confusion_matrix(y_test, y_pred).T, index=rand_for.classes_,columns=rand_for.classes_)
cm_df.index.name = 'Predicted'
cm_df.columns.name = 'True'
print(cm_df)


# In[36]:


submission=pd.DataFrame(data = {'Loan_Status':y_pred})
submission["Loan_Status"]=submission["Loan_Status"].map({1: "Y", 0: "N"})

submission.to_csv('Sample_Submission.csv',index = False)


# In[ ]:





# In[ ]:




