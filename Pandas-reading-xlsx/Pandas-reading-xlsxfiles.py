#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pandas reading files
#Read Xlsx Files 
import numpy as np
import pandas as pd
poke12 = pd.read_excel('pokemon_data.xlsx')
print(poke12)


# In[5]:


#pandas reading files first and last 5 columns
#Read Xlsx Files 
import numpy as np
import pandas as pd
poke12 = pd.read_excel('pokemon_data.xlsx')
print(poke12.head(5))
print(poke12.tail(5))

