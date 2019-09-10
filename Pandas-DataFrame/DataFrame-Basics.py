#!/usr/bin/env python
# coding: utf-8

# In[2]:


#creating empty dataframe
import pandas as pd
df = pd.DataFrame()
print(df)


# In[3]:


#creating dataframe to list
import numpy as np
import pandas as pd
data = [1,2,3,4,5,6]
df = pd.DataFrame(data)
print(df)


# In[4]:


#data frame with column header
import numpy as np
import pandas as pd
data = [['selva',100],['ganapathi',100]]
df = pd.DataFrame(data, columns = ['name','mark'],dtype =float)
print(df)


# In[7]:


#data frame with index
import numpy as np
import pandas as pd
data = {'name':['selva','ganapathi'],'rank':[100,100]}
df = pd.DataFrame(data, index = ['rank1','rank2'])
print(df)


# In[8]:


#creating dataframe list of dict
import numpy as np
import pandas as pd
data = [{'a':1,'b':2},{'a':10,'b':20,'c':20}]
df = pd.DataFrame(data)
print(df)

