num = int(input("enter the number"))

factorial = 1

if(num<0):
  print('enter the valid number')

elif(num==0):
  print("factorial of 0 is 1")
else:
  for i in range(1,num+1):
    factorial = factorial * i
  

print(f"factorial of {num} is {factorial}")
