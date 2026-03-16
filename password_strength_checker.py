import re,string

LEVELS=['Very Weak','Weak','Medium','Strong','Very Strong']


rules = {
    "Add an uppercase letter": "[A-Z]",
    "Add a lowercase letter": "[a-z]",
    "Add a digit": "[0-9]",
    "Add a special character": "[^A-Za-z0-9]"
}

def check_password_strength(password):
  strength = 0 
  suggestions=[]

  if len(password) >= 8:
    strength += 1
  else:
    suggestions.append("Password length must be greater than 8 ")

  for rule,pattern in rules.items():
    if (re.search(pattern,password)):
      strength+=1
    else:
        suggestions.append(rule)
  return strength,suggestions
  
def main():
  password = input('Enter a password: ')
  strength ,suggestions= check_password_strength(password)
  print(f"Password Strength : {LEVELS[strength-1]}")
  if suggestions:
    print("Suggestions to improve :")
    for s in suggestions:
      print("-",s)


if __name__ == '__main__':
  main()