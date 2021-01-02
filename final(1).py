def printer(ans,x):

	for row in ans: 
		for i in row:
			print(i,end="")
		print("")

def border(ans,x,y,n):
	for i in range(n):
		ans[x][y]="|"
		x-=1

def top(ans,x,y,n):
	for i in range(n):
		ans[x][y]="_"
		y+=1


def fill(ans,x,y):
	ans[x-2][y]=" "
	ans[x-2][y-1]="<"
	ans[x-2][y+1]=">"
	ans[x-3][y]="|"
	ans[x-3][y-1]="/"
	ans[x-3][y+1]="\\"
	ans[x-4][y]="o"
	border(ans,x-1,y-2,4)
	border(ans,x-1,y+2,4)
	top(ans,x-1,y-1,3)
	top(ans,x-5,y-1,3)

#get input arr
print("enter the list of numbers: ")
arr = list(map(int,input().split(" ")))
sum=0
max=int(arr[0])
width=0
base=0



for i in range(0,len(arr)):
	if i%2==0:
		sum+=int(arr[i])
	else:
		sum-=int(arr[i])
		{if sum<=0:
                        sum=base} need correction here
	if sum>max:
		max=sum
	width+=int(arr[i])


max+=5

ans=[]

#array of arrays with empty spaces
for i in range(max):
	col=[]
	for j in range(width+1):
		col.append(' ')
	ans.append(col)

x=max-1
y=0
pos=0;
while(pos<len(arr)):
	val=arr[pos]
	
	if pos%2==0 and i!=1:	
		while val>0:
			if val==arr[pos] and pos!=0:
				x-=1
			ans[x][y]='/'
			if x==5:
				fill(ans,x,y+1)
				y+=1
			x-=1
			y+=1
			val-=1
	else:
		while val>0:
			if val==arr[pos]:
				x+=1
			
		    
		    
			ans[x][y]="\\"
			if(x != len(ans) -1):
				x+=1
			y+=1
			val-=1
	pos+=1
printer(ans,val)





 
