#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pandas reading text files
 
import numpy as np
import pandas as pd
poke12 = pd.read_csv('pokemon_data.txt', sep=" ", header=None)
print(poke12)
print(poke12.head(5))
print(poke12.tail(5))

