n1 = int(input("enter n1:"))
n2 = int(input("enter n2:"))

print("what you want to do")
print("*,/,+,-")


choise = input()

if(choise == '+'):
  print(n1+n2)

elif(choise == '-'):
  print(n1-n2)
  
elif(choise == '*'):
  print(n1*n2)

else:
  print(n1/n2)
