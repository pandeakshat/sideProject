import matplotlib.pyplot as plt 
import numpy as np

# creating an empty list 
default1 = [] 
j=0
k=0
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 

# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 

	default1.append(ele) # adding the element 

x = []
y =[]
x.append(0)
y.append(0)
for i in range(0,n):
    j+=default1[i]
    x.append(j)
  
for i in range(0,n):
    if i%2==0 :
        k+=default1[i]
        y.append(k) 
    else : 
        k-=default1[i]
        y.append(k)
        
maxval= np.max(y)
ymax=maxval-1
end=x[-1]
ymaxpos=y.index(max(y))
xmax=x[ymaxpos]

plt.plot(x,y, linestyle='dashed', linewidth = 3) 
plt.plot(xmax, ymax+3, marker='o', markerfacecolor='blue', markersize=12)
plt.plot(xmax-3, ymax+2, marker='+', markerfacecolor='blue', markersize=12)
plt.plot(xmax, ymax+2, marker='|', markerfacecolor='blue', markersize=12)
plt.plot(xmax+3, ymax+2, marker='+', markerfacecolor='blue', markersize=12)
plt.plot(xmax-4, ymax+1, marker='<', markersize=12)
plt.plot(xmax+4, ymax+1, marker='>', markersize=12) 

plt.ylim(1,ymax+5) 

plt.xlim(1,end) 

plt.title('try') 
 
plt.show() 
