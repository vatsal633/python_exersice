def get_age(age,current_year):
  diffrence = 100-age
  result = current_year+diffrence
  print(f"in year{result} your age would be 100")
name = input("enter your name:")
age = int(input("enter your age:"))
current_year = int(input("enter the current year:"))

get_age(age,current_year)
