year = int(input("Which year do you want to check? "))

if (year%4 == 0 or year%400 == 0):
  print("This year is a leap year")
elif(year%4 !=0 or year%100 == 0):
  print("This year is not a leap year")
else:
  print(f"{year} is a dummy year")

