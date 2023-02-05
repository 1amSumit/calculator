from replit import clear
from art import logo
def add(n1 , n2):
  return n1 + n2

def subtract(n1 , n2):
  return n1 - n2

def multiply(n1 , n2):
  return n1 * n2

def divide(n1 , n2):
  return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,   
    "/":divide
  }

def calculator():
  print(logo)

  n1 = float(input("What is the first number? "))

  for symbol in operations:
    print(symbol)


  operation_symbol = input("Pick an operator line above: ")

  n2 = float(input("What is the next number? "))

  calculation = operations[operation_symbol]
  answer = calculation(n1 , n2)
  print(f"{n1} {operation_symbol} {n2} = {answer}")

  end = False
  while not end:
    choice = input("Type 'y' to continue calculation or 'n' to start new calculation . : ")

    if choice == 'y':
      operation_symbol = input("Pick an operator ")
      n3 = float(input("What is next number? "))
      calculation = operations[operation_symbol]
      sec_answer = calculation(answer , n3)
      answer = sec_answer
      print(f"{answer} {operation_symbol} {n3} = {sec_answer}")
    elif choice == 'n':
      end = True
      clear()
      calculator() #recurtion

calculator()