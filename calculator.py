def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

history = []

def show_history(history):
  for record in history:
    print(record)
    
while True:

  print("1. Calculate")
  print("2. Show history")
  print("3. Clear history")
  print("4. Quit")
  choice = input("Choose an option: ")

  if choice == '1':
    try:
      var1 = float(input("Enter first value: "))
      var2 = float(input("Enter second value: "))
    except ValueError:
      print("Enter a number")
      continue
    print("Choose an operation: ")
    var3 = input()
    if var3 == 'add':
      result = add(var1, var2)
      print(result)
      history.append(f"{var1} + {var2} = {result}")
    elif var3 == 'subtract':
      result = subtract(var1, var2)
      print(result)
      history.append(f"{var1} - {var2} = {result}")
    elif var3 == 'multiplication':
      result = multiplication(var1, var2)
      print(result)
      history.append(f"{var1} * {var2} = {result}")
    elif var3 == 'division':
      if var2 == 0:
        print("Invalid Operation")
      else:
        result = division(var1, var2)
        print(result)
        history.append(f"{var1} / {var2} = {result}")
    else:
      print("Invalid Operation")
  elif choice == '2':
    show_history(history)
  elif choice == '3':
    history = []
  elif choice == '4':
    break
  else:
    print("Invalid input. Try again")
