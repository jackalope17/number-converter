nd = 0
nb = 0

def decimalToBinary(nd):
  while True:
    try:
      nd = int(input('\nPlease enter the whole number you wish to convert to binary: ',))
      return bin(nd).replace('0b','')
      break
    except:
      print('Please only enter whole numbers to be converted.')
      continue

  
def binaryToDecimal(nb):
  while True:
    try:
      nb = (input('\nPlease enter the binary number you wish to convert to decimal: ',))
      return int(nb,2)
      break
    except:
      print('Please only enter a number writen in binary, using only 1 and 0, to be converted.')
      continue


def get_menu_choice():
  def print_menu():
    print('')
    print(28 * "-", "CONVERSION MENU", 28 * "-")
    print("1. Convert Decimal to Binary")
    print("2. Convert Binary to Decimal")      
    print("3. Exit from the Program")
    print(73 * "-")


  while True:
    print_menu()
    choice = input("Enter your choice [1-3]: ")

    if choice == '1':
      print(decimalToBinary(nd))
    elif choice == '2':
      print(binaryToDecimal(nb))
    elif choice == '3':
      print("\nExiting..")
      return '\n'
      break
    else:
      print("\nWrong menu selection. Please enter a number from 1-3")
  

print(get_menu_choice())