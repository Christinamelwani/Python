import csv
life_expectancy = { }

def main():
  with open("life_expectancy.csv") as file:
    reader = csv.reader(file)
    life_expectancy = {rows[0]: float(rows[1]) for rows in reader}
  
  birth_year = int(input("What year were you born?\n"))
  current_year= int(input("Interesting. What year is it now, btw?\n"))
  country = input("Lastly, what country are you from?\n")
  if country.capitalize() in life_expectancy:
    death_year = predict_death(birth_year, life_expectancy[country.capitalize()])
    print(f'''
    You are:
    approximately {current_year - birth_year} years old.
    You are expected to die in the year {int(death_year)}
    at {int(death_year - birth_year)} years old.
    Damn.''')
  else:
    print("Country not found!")


def predict_death(birth, expectancy):
  death = expectancy + birth
  return death 


if __name__ == "__main__":
  main()
  
  
