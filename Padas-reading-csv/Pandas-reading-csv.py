#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pandas reading files
#Read CSV Files 
import numpy as np
import pandas as pd
poke = pd.read_csv('pokemon_data.csv')
print(poke)


# In[4]:


#Read CSV Files 
import numpy as np
import pandas as pd
poke1 = pd.read_csv('pokemon_data.csv')
#show only first 5 rows
print(poke1.head(5))
#show only last 5 rows
print(poke1.tail(5))

