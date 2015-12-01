#take in argument that is number of seconds
#example: min = seconds(60) should be 1
print('Time Calculator')
#reads from "File.txt displays values for the user"
file = "File.txt"
inFile = open(file,'r')
count = 0
for i in inFile:
	if(inFile):
		count+=1
		print(count ,":",i)
#Demands the input of minutes from the user 
num1 = input('Amount of Minutes: ')

# The amount of minutes times 60 gives you the amount of seconds
answer = float(num1) * 60
# Displays product
print('{0} Minute(s) will equal {1} seconds '.format(num1,answer))
#Demands the input of seconds from the user
num2 = input('Amount of Seconds: ')

# The amount of seconds times the value of a second gives you the amount of minutes
answer1 = float(num2) * 0.0166667
print('{0} Seconds(s) will equal {1} Minute(s)'.format(num2,answer1))

