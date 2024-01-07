#!/usr/bin/env python
# coding: utf-8

# In[1]:


def palindrome(tpl):
    tpl_copy = tpl[::-1]
    
    if tpl == tpl_copy:
        return "Yes!"
    else:
        return "No!"


# In[8]:


tpl = tuple(input("Enter Comma Saperated words : ").split(","))

print(palindrome(tpl))


# In[ ]:




