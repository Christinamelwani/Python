import re


def main():
  confirmation = "no"
  while not confirmation.upper() == "YES":
    username = input("Please enter your username: ")
    password = input(f"Hello, {username}\nPlease enter your password: ")
    password = validate(password)
    obscured_password = "*" * len(password)
    confirmation = input(f"{username}, your password is {obscured_password}\nDoes this look correct? (yes/no) ")
    if confirmation.upper() == "YES":
      print("Password succesfully set.")
    else:
      print("Please try again:\n")


def validate(password):
  error_prompt = ("The password is not strong enough.\nIt should contain:\n a lowercase letter \n an uppercase letter \n a special character(?/!.@) \nand be at least 8 letters long. \n\nPlease try again (enter new password): ")
  while (is_valid(password) == "no"):
    password = input(error_prompt)
  return(password)
  

def is_valid(password):
  # condition is a regex expression that is fulfilled if:
  # the password string contains at least one lowercase letter,
  # one uppercase letter
  # and one special character 
  condition = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[?/!.@])"
  complexity = re.search(condition , password)
  if complexity == None:
    return "no"
  if len(password) < 8:
    return "no"
  # if all conditions fulfilled:
  return "yes"


if __name__ == "__main__":
  main()
