#!/usr/bin/env python
# coding: utf-8

# # NumPy: Numerical Python
#     - Multidimensional array objects and methods associated
#     - Random number generation and operation
#     - Linear Algebra Functions

# In[1]:


import numpy as np


# In[4]:


# Arrays: 
#sales of 20 stores for a month
#list: dictionary: 20 keys


# In[5]:


sales = [[1, 1, 3, 2, 4], [2, 1, 4, 3,  1], [3,2,  1, 4,5 ], [6, 2, 3, 5, 1], [1, 4, 3,4, 2]]
#sales for each store:


# In[6]:


for i in sales:
    print(sum(i))


# In[ ]:





# In[144]:


#creating an array


# In[145]:


sales_arr = np.array([1000, 2000, 870, 780, 1500, 1450, 1700])


# In[146]:


print('Array Data :\n', sales_arr)
print('Array dimensions: \t:{}'.format(sales_arr.ndim)) #How many elements in each dimension
print('Array Shape \t:{}'.format(sales_arr.shape))
print('Array Size \t:{}'.format(sales_arr.size))
print('Array Data Type \t:{}'.format(sales_arr.dtype))
print('Array Item Size \t:{}'.format(sales_arr.itemsize)) #Size in bytes


# In[147]:


store1 = [1000, 1200, 870, 780, 1500, 1450, 1700]
store2 = [780, 75, 1145, 1345, 1400, 670, 2000]
store3 = [1167, 1560, 1899, 1900, 1654, 1000, 1900]
store4 = [1145, 1180, 1800, 2100, 1245, 1900, 2125]
store5 = [1160, 1780, 2100, 810, 1090, 1100, 1560]

sales_list = [store1, store2, store3, store4, store5]
sales_list


# In[148]:


sales_arr = np.array(sales_list)
print('Array Data :\n', sales_arr)
print('Array dimensions: \t:{}'.format(sales_arr.ndim)) #How many elements in each dimension
print('Array Shape \t:{}'.format(sales_arr.shape))
print('Array Size \t:{}'.format(sales_arr.size))
print('Array Data Type \t:{}'.format(sales_arr.dtype))
print('Array Item Size \t:{}'.format(sales_arr.itemsize)) #Size in bytes


# In[149]:


np.array([1234, 23.44, 34])


# In[150]:


np.array([1234, 23.45, True, '34'], dtype = int)


# In[151]:


#Hierarchy String > float > int


# In[152]:


#Arrays filed with zeros with numpy:
np.zeros(5)


# In[153]:


np.zeros((5, 4), dtype = str)


# In[154]:


np.ones(5)


# In[155]:


np.zeros_like(sales_arr)


# In[156]:


np.random.randint(2, 100, (5, 4)) #Array filled with random numbers between 2 and 100 of shape 5x4 


# In[157]:


np.linspace(1, 100, 10, retstep = True) #Array with equally steppd numbers inclusive of 1 and 100 with 10 numbers


# In[158]:


np.arange(1, 100, 10) #start, stop, and step value stop is excluded


# In[159]:


sales_stores_arr = np.array([1000, 2000, 870, 780, 1500, 1450, 1700])


# In[160]:


sales_stores_arr


# In[161]:


sum(sales_stores_arr)


# In[162]:


per_arr = sales_stores_arr / sum(sales_stores_arr) * 100 #sales as percentage


# In[163]:


per_arr


# In[164]:


per_arr.round(2)


# In[165]:


print('Sum\t:', sales_stores_arr.sum())


# In[166]:


print('Sum\t:', sales_stores_arr.cumsum()) #Cumulative sum


# In[167]:


print('Max Value\t:', sales_stores_arr.max()) #<Max value


# In[168]:


print('Min Value\t:', sales_stores_arr.min()) #<Max value


# In[169]:


print('Mean Value\t:', sales_stores_arr.mean(), 2) #<Max value


# In[170]:


print('Var Value\t:', sales_stores_arr.var(), 2) #<Max value


# ## 2 Dimensional Array

# In[171]:


sales_arr


# In[172]:


print('Sum\t:', sales_arr.sum())
print('Sum\t:', sales_arr.cumsum()) #Cumulative sum
print('Max Value\t:', sales_arr.max()) #<Max value
print('Min Value\t:', sales_arr.min()) #<Max value
print('Mean Value\t:', sales_arr.mean(), 2) #<Max value
print('Var Value\t:', sales_arr.var(), 2) #<Max valu


# ## Along an Axis:

# In[173]:


#For a 2d array 
#Axis = 0 Column Wise Operation
#Axis = 1 Row-wise operation

print('for each store IE Row-wize operation'.upper())
print('Sum\t:', sales_arr.sum(axis=1))
print('Cumulative Sum\t:', sales_arr.cumsum(axis=1)) #Cumulative sum
print('Max Value\t:', sales_arr.max(axis=1)) #<Max value
print('Min Value\t:', sales_arr.min(axis=1)) #<Max value
print('Mean Value\t:', sales_arr.mean(axis=1), 2) #<Max value
print('Var Value\t:', sales_arr.var(axis=1), 2) #<Max valu


# In[174]:


#For a 2d array 
#Axis = 0 Column Wise Operation
#Axis = 1 Row-wise operation

print('for each store IE Column-wize operation'.upper())
print('Sum\t:', sales_arr.sum(axis=1))
print('Cumulative Sum\t:', sales_arr.cumsum(axis=0)) #Cumulative sum
print('Max Value\t:', sales_arr.max(axis=0)) #<Max value
print('Min Value\t:', sales_arr.min(axis=0)) #<Max value
print('Mean Value\t:', sales_arr.mean(axis=0), 2) #Mean value
print('Var Value\t:', sales_arr.var(axis=0), 2) #Var value


# In[175]:


np.sqrt
np.sin
np.log
np.greater


# In[176]:


print(dir(np))


# In[177]:


x1 = np.array([2, 4, 1, 5, 6])
x2 = np.array([3, 5, 1, 3, 6])


# In[178]:


np.logical_and(x1 < 2.5, x2 < 2.5)


# In[179]:


np.logical_or(x1 < 2.5, x2 < 2.5)


# In[180]:


np.logical_not(x1 < 2.5)


# In[181]:


np.logical_xor(x1 < 2.5, x2 < 2.5)


# In[182]:


ratings = np.array([00, 1, 3, 4, 2, 3, 3, 3, 4, 5, 2, 10, 3, 3]* 100)
ratings.shape


# In[183]:


np.any(ratings > 5) #Used to check if a single value in the array is true


# In[184]:


np.all(ratings <= 5) #used to check if all values evalue to true


# In[185]:


ht = np.array([1.77, 1.67, 1.56, 1.76, 1.70])
wt = np.array([80, 91, 87, 76, 90])


# In[186]:


bmi = wt/(ht**2)


# In[187]:


bmi


# ## Matrix Product: No Elementize Computation

# In[188]:


a1 = np.random.randint(1, 10, (2, 4))
a2 = np.random.randint(1, 10, (4, 5))


# In[189]:


a1


# In[190]:


a2


# ### Indexing An Array

# In[191]:


lis = ['A', 1, 'B', 2, 'C', 3, 'D', 4, 'E', 5]
lis[0]


# In[192]:


sales_arr


# In[193]:


sales_stores_arr


# In[194]:


sales_stores_arr[0]


# ### Slicing In Arrays

# In[195]:


sales_stores_arr[1:10:2]


# In[196]:


rand_arr_id = np.random.randint(1, 10, 20)


# In[197]:


rand_arr_id


# In[198]:


rand_arr_id[1:10:2]


# In[199]:


#For two dimensional arrays: arr_2d[row, column]
rand_arr_2d = np.random.randint(1, 10, (5, 4))


# In[200]:


rand_arr_2d


# In[201]:


rand_arr_2d[2]


# In[202]:


#A complete column:
rand_arr_2d[:, 3]


# In[203]:


#To extract as 2d need to correlate in form of a list:
rand_arr_2d[[2]]


# In[204]:


rand_arr_2d[:, [3]]


# In[205]:


rand_arr_2d[4, 3]


# ### Array Manipulations

# In[206]:


sales_arr


# In[207]:


#Correct 75 in array
sales_arr[1, 1] = 750 #Assigning to 750


# In[208]:


sales_arr


# ### Changing Array Shapes

# In[209]:


rand_arr_2d


# ### To Convert to a 1D Array

# In[210]:


rand_arr_2d.ravel(order='C') #In 'C' order:


# In[211]:


rand_arr_2d.flatten(order='F') #Flatten Array


# In[212]:


#For reshaping the size remains the same


# ### Transpose Function

# In[213]:


sales_arr.T


# ### Concatenate - To Join Arrays

# In[214]:


x1 = np.array([[10, 20, 30], [20, 40, 60]])
x2 = np.array([[100, 200, 300]])


# In[215]:


np.concatenate([x1, x2], axis=None)


# In[233]:


np.concatenate([x1, x2], axis=0) #Column-wise operation


# In[234]:


x3 = np.array([[100, 200], [300, 400]])
x3.shape


# ### Stack Functions - Stack, HStack, VStack

# In[225]:


#Stack
#hstack
#vstack

x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
np.stack((x1, x2))


# In[226]:


np.hstack((x1, x2))


# In[227]:


np.vstack((x1, x2))


# ### Split Functions - HSplit, VSplit

# In[228]:


x = np.arange(12)
x


# In[229]:


np.split(x, 3)


# In[230]:


x = np.arange(16).reshape((4, 4))


# In[231]:


np.hsplit(x, 2) #Split at column 2


# In[232]:


np.vsplit(x, 2) #Split at row 2

