def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

history = []

while True:
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
    history.append(result)
  elif var3 == 'subtract':
    result = subtract(var1, var2)
    print(result)
    history.append(result)
  elif var3 == 'multiplication':
    result = multiplication(var1, var2)
    print(result)
    history.append(result)
  elif var3 == 'division':
    if var2 == 0:
      print("Invalid Operation")
    else:
      result = division(var1, var2)
      print(result)
      history.append(result)
  else:
    print("Invalid Operation")

  print(history)  
  print("Calculate again? (y/n)")
  x = input()
  if x == "n":
    break
