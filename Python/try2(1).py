import matplotlib.pyplot as plt 

# x axis values 
x = [0.,10, 7, 12, 2 , 4] 
# corresponding y axis values 
y = [0.,5, 3, 6, 1 , 2] 

# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
		marker='o', markerfacecolor='blue', markersize=12) 

# setting x and y axis range 
plt.ylim(0, 20) 
plt.xlim(0,20) 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('Some cool customizations!') 

# function to show the plot 
plt.show() 
