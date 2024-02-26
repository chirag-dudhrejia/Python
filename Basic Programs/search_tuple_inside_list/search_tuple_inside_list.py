#!/usr/bin/env python
# coding: utf-8

# In[16]:


def search_tuple(lst):
    for i in lst:
        if type(i) == tuple:
            print(i,"is tuple")
            break
        print(i)


# In[21]:


rows = int(input("Enter number Of Row : "))
cols = int(input("Enter number of cols : "))
matrix = []

for i in range(1, rows+1):
    print("Input for row :",i)
    a = list(input("Enter Comma saperated value : ").split(","))
    matrix.append(a)
print("Before Change")
print(matrix)

matrix[1] = tuple(matrix[1])
print()
print("After Change")
print(matrix)

print()
search_tuple(matrix)


# In[ ]:




