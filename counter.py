file=open("text.txt", "r")

data = file.read()

occurences1 = data.count("sorry")

occurences2 = data.count("Sorry")

occurences=occurences1+occurences2

redeem= int(occurences/2)
print(' you know what this means ' )

print(' Number of occurences of sorry :' , occurences)

print(' Redeemption count = ' , redeem)

print(' I am coming, be ready and prepare ' )
