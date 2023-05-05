#!/usr/bin/env python
# coding: utf-8

# Create a function that takes a string and returns a string in which each character is repeated once.
# 

# In[1]:


def double_char(string):
    new_string = ''
    for char in string:
        new_string += char * 2
    return new_string


# In[2]:


double_char("string")


# In[3]:


double_char("Hello World")


# In[4]:


double_char("1234!_")


# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.
# 

# In[5]:


def reverse(value):
    if type(value) == bool:
        return not value
    else:
        return "boolean expected"


# In[7]:


True


# In[8]:


False


# In[15]:


reverse(0)


# In[16]:


reverse(None)


# Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
# 

# In[53]:


def num_layers(n):
    thickness = 0.5/1000
    total_thickness = thickness * (2 ** n)
    return "{:.3f}m".format(total_thickness)


# In[54]:


num_layers(1)


# In[55]:


num_layers(4)


# In[56]:


num_layers(21)


# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
# 

# In[65]:


def index_of_caps(word):
    return [ i for i in range(len(word))if word[i].isupper()]


# In[66]:


index_of_caps("eDaBiT")


# In[67]:


index_of_caps("eQuINoX")


# In[68]:


index_of_caps("determine")


# In[69]:


index_of_caps("STRIKE")


# In[70]:


index_of_caps("sUn")


# In[73]:


def find_even_nums(n):
    return [i for i in range (1, n+1) if i % 2 == 0]


# In[74]:


find_even_nums(8)


# In[75]:


find_even_nums(4)


# In[76]:


find_even_nums(2)


# In[ ]:




