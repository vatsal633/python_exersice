num_list = []

# adding items to the list
for i in range(5):
  num = int(input("enter the "))
  num_list.append(num)


temp = 0
min = num_list[0]
for i in range(4):
  if(temp<num_list[i]):
    temp = num_list[i]
  elif(num_list[i]<=min):
    min = num_list[i]
print(f'max number is {temp} and minimum number is {min}')
