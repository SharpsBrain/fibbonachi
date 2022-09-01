#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the value of 'n': "))
a=0
b=1
sum=0
count=1
print("Fibbo nacchi Series" ,end =" ")
while(count<=n):
    print(sum, end =" ")
    count +=1
    a=b
    b=sum
    sum=a+b


# In[ ]:




