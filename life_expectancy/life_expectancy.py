from support import get_resources, get_year, get_expectancy, calculate_age, predict_death, print_results, exit_sequence

def main():

  list_of_expectancies = get_resources()
  if list_of_expectancies == "not found":
    return

  while True:
    birth_year = get_year("What year were you born?\n")
    current_year= get_year("Interesting. What year is it now, btw?\n")
    expectancy = get_expectancy("Lastly, what country are you from?\n", list_of_expectancies)

    age = calculate_age(birth_year, current_year)
    if age == "error":
      return
    death_year = predict_death(birth_year, expectancy)
    age_at_death = calculate_age(birth_year, death_year)

    print_results (age, death_year, age_at_death)

    if exit_sequence() == "confirmed":
      return


if __name__ == "__main__":
  main()
  
