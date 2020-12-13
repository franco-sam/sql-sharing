#!/usr/bin/env python
# coding: utf-8

# # **Project Description**
# 
# A country may take debt to manage its economy. For example, infrastructure spending is one costly ingredient required for a country's citizens to have comfortable lives. The World Bank is the organization that provides debt to countries.
# 
# In this project, I am going to analyze international debt data collected by The World Bank. The dataset contains information about the amount of debt (in USD) owed by developing countries across several categories.
# 
# The data used in this project is provided by The World Bank. It contains both national and regional debt statistics for several countries across the globe as recorded from 1970 to 2015.

# In[1]:


get_ipython().run_cell_magic('sql', '', 'postgresql:///international_debt\n    \nSELECT * \nFROM international_debt\nLIMIT 10;')


# **2. Finding the number of distinct countries**
# 
# From the first ten rows, we can see the amount of debt owed by Afghanistan in the different debt indicators. But we do not know the number of different countries we have on the table. There are repetitions in the country names because a country is most likely to have debt in more than one debt indicator.
# 
# In this section, extract the number of unique countries present in the table.

# In[2]:


get_ipython().run_cell_magic('sql', '', 'SELECT COUNT(DISTINCT country_name) AS total_distinct_countries\nFROM international_debt;')


# **3. Finding out the distinct debt indicators**
# 
# Knowing about the various debt indicators will help us to understand the areas in which a country can possibly be indebted to.

# In[3]:


get_ipython().run_cell_magic('sql', 'SELECT DISTINCT indicator_code AS distinct_debt_indicators', 'FROM international_debt\nORDER BY distinct_debt_indicators;')


# **4. Totaling the amount of debt owed by the countries**
# 
# Let's find out the total amount of debt (in USD) that is owed by the different countries. This will give us a sense of how the overall economy of the entire world is holding up.

# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT \n    ROUND(SUM(debt), 0) AS total_debt\nFROM international_debt; ')


# **5. Country with the highest debt**
# 
# Let's now find out the country that owns the highest amount of debt along with the amount. 
# 
# This debt is the sum of different debts owed by a country across several categories.

# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT country_name, sum(debt) as total_debt\nFROM international_debt\nGROUP BY country_name\nORDER BY total_debt DESC\nLIMIT 1;')


# **6. Average amount of debt across indicators**
# 
# A more in-depth breakdown of China's debts can be found here.

# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT indicator_code as debt_indicator, indicator_name, AVG(debt) as average_debt\nFROM international_debt\nGROUP BY debt_indicator, indicator_name\nORDER BY average_debt DESC\nLIMIT 10;')


# **7. The highest amount of principal repayments**
# 
# We can see that the indicator DT.AMT.DLXF.CD tops the chart of average debt. This category includes repayment of long term debts.
# 
# The first two indicators are the most severe categories in which the countries owe their debts.
# 
# We can investigate this a bit more so as to find out which country owes the highest amount of debt in the category of long term debts (DT.AMT.DLXF.CD). Since not all the countries suffer from the same kind of economic disturbances, this finding will allow us to understand that particular country's economic condition a bit more specifically.

# In[9]:


get_ipython().run_cell_magic('sql', '', "SELECT \n    country_name, \n    indicator_name\nFROM international_debt\nWHERE debt = (SELECT \n                  MAX(debt)\n             FROM international_debt\n             WHERE indicator_code='DT.AMT.DLXF.CD');")


# **8. The most common debt indicator**
# 
# China has the highest amount of debt in the long-term debt (DT.AMT.DLXF.CD) category. 
# 
# We saw that long-term debt is the topmost category when it comes to the average amount of debt. But is it the most common indicator in which the countries owe their debt?

# In[14]:


get_ipython().run_cell_magic('sql', 'SELECT indicator_code, COUNT(indicator_code) as indicator_count', 'FROM international_debt\nGROUP BY indicator_code\nORDER BY indicator_count DESC, indicator_code DESC\nLIMIT 20;')


# **9. Other viable debt issues and conclusion**
# 
# There are a total of six debt indicators in which all the countries listed in our dataset have taken debt.
# 
# Let's change tracks from debt_indicators now and focus on the amount of debt again. Let's find out the maximum amount of debt across the indicators along with the respective country names. With this, we will be in a position to identify the other plausible economic issues a country might be going through.
# 

# In[15]:


get_ipython().run_cell_magic('sql', 'SELECT country_name, indicator_code, MAX(debt) AS maximum_debt', 'FROM international_debt\nGROUP BY country_name, indicator_code\nORDER BY maximum_debt DESC\nLIMIT 10;')

