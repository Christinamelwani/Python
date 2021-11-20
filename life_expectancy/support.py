import csv


def get_resources():

   try:
    with open("life.csv") as file:
      reader = csv.reader(file)
      list_of_expectancies = {rows[0]: float(rows[1]) for rows in reader}
      return list_of_expectancies

   except:
     print("Download life.csv first!")
     return "not found"


def get_year(prompt):

  while True:
    temp = input(prompt)
    try: 
      temp = int (temp)
      break;
    except ValueError:
      print("Not a valid year. Try again!\n")

  return temp


def get_expectancy(prompt, expectancy):

  while True:
    country = input(prompt)
    country = country.capitalize()
    if country in expectancy:
      temp = int(float(expectancy[country]))
      break
    else:
      print("Not a valid country. Try again!\n")

  return temp


def predict_death(birth, expectancy):
  death = expectancy + birth
  return death 


def calculate_age(birth, current):
  age = current - birth
  if age < 0:
    print("A time traveller? This calculation won't work for you. See ya sooner!")
    return "error"
  else:
    return age


def print_results(age, death_year, age_at_death):
  print(f'''
You are:
  approximately {age} years old.
  You are (or were?) expected to die in the year {death_year}
  at {age_at_death} years old.
  Damn.''')


def exit_sequence():
  check = input("Try again? (Yes, No)\n")
  if check.upper() == 'NO':
    print(f'''
Thank you for using life_expectancy.py.
This program is solely for entertainment purposes and very unlikely to predict your actual death. Be wary of your surroundings and try to stay healthy!\n''')
    return "confirmed"
  else:
    return 0

