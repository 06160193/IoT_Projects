import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filename='/home/aiot/IoTPlatformLab/iot/01_rest/log.txt'
elements=[]
index=[]
with open(filename) as file:
    i=0
    for line in file:
        line = line.strip().split(' ')
        elements.extend(line)
        index.append(i)
        i=i+1
#print(type(line)) 
#print(type(elements))
ele_array = np.array(elements,dtype=np.float64)
index_array = np.array(index,dtype=np.float64)
#print ('%s\nshape is %s' % (type(ele_array), ele_array.shape)) 
#print (ele_array) 
#print (elements) 

plt.hist(ele_array)
plt.show() 
plt.bar(index_array,ele_array) 
plt.show() 
plt.scatter(index_array,ele_array) 
plt.show() 
#file.close()
