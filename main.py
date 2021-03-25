# Prompt the user to input a year
year = int(input("Please input a year: "))

# Using if statements, output whether the inputted year is or is not a leap year
if(year < 0):
  if(year // 100 != 0):
    if(year % 400 == 0):
      print("Your year is a leap year")
    else:
      print("Your year is not a leap year")
  elif(year % 4 == 0):
    print("Your year is a leap year")
  else:
    print("Your year is not a leap year")