def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

def show_history(history):
  for record in history:
    print(record)

def save_history(history):
  with open("history.txt", "w") as file:
    for record in history:
      file.write(record + "\n")

def load_history():
  current = []
  try:
    with open("history.txt", "r") as file:
      for record in file:
        current.append(record.rstrip("\n"))
  except FileNotFoundError:
    return []
  return current

history = load_history()

while True:
  print("1. Calculate")
  print("2. Show history")
  print("3. Clear history")
  print("4. Quit")
  print("5. Delete most recent calculation")
  choice = input("Choose an option: ")

  if choice == '1':
    try:
      var1 = float(input("Enter first value: "))
      var2 = float(input("Enter second value: "))
    except ValueError:
      print("Enter a number")
      continue

    print("Choose an operation: add, subtract, multiplication, division")
    var3 = input()

    if var3 == 'add':
      result = add(var1, var2)
      print(result)
      history.append(f"{var1} + {var2} = {result}")
      save_history(history)
    elif var3 == 'subtract':
      result = subtract(var1, var2)
      print(result)
      history.append(f"{var1} - {var2} = {result}")
      save_history(history)
    elif var3 == 'multiplication':
      result = multiplication(var1, var2)
      print(result)
      history.append(f"{var1} * {var2} = {result}")
      save_history(history)
    elif var3 == 'division':
      if var2 == 0:
        print("Invalid Operation")
      else:
        result = division(var1, var2)
        print(result)
        history.append(f"{var1} / {var2} = {result}")
        save_history(history)
    else:
      print("Invalid Operation")

  elif choice == '2':
    show_history(history)
  elif choice == '3':
    history = []
    save_history(history)
  elif choice == '4':
    save_history(history)
    break
  elif choice == '5':
    if len(history) == 0:
      print("No history to delete")
    else:
      history.pop()
      save_history(history)
  else:
    print("Invalid input. Try again")