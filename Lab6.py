def showIntro():
    print("welcome to the Aritgmetic Engine")
    print("================================")
    print("Valid commands are 'add','mult','sub','div', and 'quit'.\n"

def showEnd():
          print("\nThank you for using the Arithmetic Engine...")
          print("\nPlease come back again soon!")

def doLoop():
          while True:
          cmd = input("What computation do you want to do?")
          num1 = int(input("Enter the first number: "))
          num2 = int(input("Enter the second number: "))

          if cmd == "add":
              result = num1 + num2
          elif cmd == "sub":
              result = num1 - num 2
          elif cmd == "mult":
              result
