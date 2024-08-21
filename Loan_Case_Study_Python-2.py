#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Import statements
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[3]:


# Read the loan data set csv file into a data frame
loan_df = pd.read_csv('/Users/I326944/Library/CloudStorage/OneDrive-SAPSE/desktop/loan.csv',dtype='unicode')


# In[5]:


# Check Data Set Info for null values / sum of null values
loan_df.head()
loan_df.info()
loan_df.isnull().sum() 


# In[7]:


# Remove the null values from columns that have all null / NA Values (Data Cleaning)
loan_df_new = loan_df.dropna(axis=1,how='all')
loan_df_new.isnull().sum()


# In[9]:


# Remove next_pymnt_d column as it has 38577 NA values and few dates that are Jun 16
loan_df_new = loan_df_new.drop('next_pymnt_d',axis=1)


# In[11]:


# Remove desc column as it has 12942 NA values and it would not be required for this case study
loan_new_df = loan_df_new.drop('desc',axis=1)


# In[15]:


# Remove emp_ltitle as it has 2459 NA Values and would not be required for this case study
loan_new_df = loan_df_new.drop('emp_title',axis=1)


# In[17]:


#Remove URL column ( not required for this case study)
loan_df_new = loan_df_new.drop('url',axis=1)


# In[19]:


#Check for duplicates
loan_new_df[loan_new_df.duplicated()]


# In[65]:


#Analysis of revol_util - remove the %
loan_status_default_df['revol_util'] = loan_status_default_df['revol_util'].str.replace('%', '')
loan_status_default_df['revol_util']
sns.distplot(loan_status_default_df['revol_util'],kde=True,color='blue',bins=5)


# In[67]:


# Plot House Ownership variable as a hist plot
sns.histplot(loan_status_default_df['home_ownership'],kde=False,color='blue')


# In[69]:


# Analysis of DTI
sns.distplot(loan_status_default_df['dti'],kde=True,color='blue',bins=5)
sns.boxplot(x=loan_status_default_df['dti'])


# In[75]:


# Analysis of Loan Grade as a histogram
sns.histplot(loan_status_default_df['grade'])


# In[93]:


# clean the tax_liens field and replace NA with 0
loan_status_default_df.loc['tax_liens'] = loan_status_default_df['tax_liens'].fillna(0)


# In[95]:


loan_status_default_df['tax_liens']


# In[97]:


# Tax Liens has all zeros and will not be analzed


# In[101]:


# Analysis of Annual Income - Convert to float
loan_status_default_df.loc['annual_inc'] = loan_status_default_df['annual_inc'].astype(float)


# In[105]:


# Distribution ploat for Annual Income
sns.distplot(loan_status_default_df['annual_inc'],kde=True,color='blue',bins=5)


# In[107]:


# Hist Plot for Annual Income
sns.histplot(loan_status_default_df['annual_inc'])


# In[109]:


loan_status_default_df['annual_inc'].describe()


# In[135]:


# Analysis of mths_since_last_delinq ( Fill NA with 0)
loan_status_default_df.loc['mths_since_last_delinq'] = loan_status_default_df['mths_since_last_delinq'].fillna(0)


# In[119]:


# Distribution Plot
sns.distplot(loan_status_default_df['mths_since_last_delinq'],kde=True,color='blue',bins=5)


# In[157]:


# Analysis of mths_since_last_record ( Replace the NA with 0)
loan_status_default_df.loc['mths_since_last_record'] = loan_status_default_df['mths_since_last_record'].fillna(0)


# In[159]:


loan_status_default_df.loc['mths_since_last_record'] = loan_status_default_df['mths_since_last_record'].astype(float)


# In[161]:


sns.distplot(loan_status_default_df['mths_since_last_record'],kde=True,color='blue',bins=5)


# In[165]:


# Hist Plot to analayze loan term
sns.histplot(loan_status_default_df['term'],kde=False,color='blue')


# In[181]:


# Scatter Plot Analysis
loan_status_default_df['annual_inc']


# In[185]:


loan_status_default_df['annual_inc'].dropna()


# In[187]:


loan_status_default_df['int_rate'].dropna()


# In[189]:


sns.scatterplot(data=loan_status_default_df, x="annual_inc", y="int_rate")


# In[191]:


loan_status_default_df = loan_df_new[loan_df_new.loan_status == 'Charged Off']


# In[195]:


# Plot Scatter Plot between annual income and interest rate
sns.scatterplot(data=loan_status_default_df, x="annual_inc", y="int_rate")


# In[197]:


# Plot Scatter Plot between annual income and interest rate and loan term
sns.scatterplot(data=loan_status_default_df, x="annual_inc", y="int_rate",hue="term")


# In[199]:


# Plot Scatter Plot between annual income and interest rate and home ownership
sns.scatterplot(data=loan_status_default_df, x="annual_inc", y="int_rate",hue="home_ownership")


# In[ ]:




