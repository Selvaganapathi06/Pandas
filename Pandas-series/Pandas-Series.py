#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Pandas Series
import numpy as np
import pandas as pd
s=pd.Series()
print(s)


# In[11]:


#creating Series from nd array
import numpy as np
import pandas as pd
data = np.array(['a','b','c','d','e'])
t = pd.Series(data)
print(t)


# In[12]:


#creating Series from nd array with specified index
import numpy as np
import pandas as pd
data = np.array(['a','b','c','d','e'])
t = pd.Series(data,index =[10,20,30,40,50])
print(t)


# In[13]:


#creating Series from dictionary 
import numpy as np
import pandas as pd
data = {'a':'0.','b':'1.','c':'2.','d':'3.'}
t = pd.Series(data)
print(t)


# In[15]:


#creating Series from dictionary with manual index
import numpy as np
import pandas as pd
data = {'a':'0.','b':'1.','c':'2.','d':'3.'}
t = pd.Series(data,index = ['a','b','e','a'])
print(t)


# In[16]:


#creating Series from scalr value
#while using scalar value manually assign tasks
import numpy as np
import pandas as pd
t = pd.Series(5,index =[10,20,30,40,50])
print(t)


# In[22]:


#creating series and accessing value
import numpy as np
import pandas as pd
t = pd.Series(5,index =[10,20,30,40,50])
print(t[10])
print(t[20])
print(t[40])

