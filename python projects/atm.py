from cardHolder import cardHolder

def print_menu():
  ### print options to the user

  print("please choose from one of the following options...")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. show Balance")
  print("4. Exit")

def deposit(cardHolder):
  try:
    deposit=float(input("How much $$ would you like to deposit:"))
    cardHolder.set_balance(cardHolder.get_balance()+deposit)
    print("Thank you for your $$ YOur new balance is:", str(cardHolder.get_balance()))
  except:
    print("Invalid input")


def withdraw(cardHolder):
  try:
    withdraw = float(input("How much $$ would you like to withdraw:"))
    ### check if user has enough money
    if(cardHolder.get_balance()<withdraw):
      print("Insufficient balance:")
    else:
      cardHolder.set_balance(cardHolder.get_balance() - withdraw)
      print("You are good to go! Thank you :")
  except:
    print("Invalid input")

def check_balance(cardHolder):
  print("Your current balance is:", cardHolder.get_balance())

if __name__=="__main__":
  current_user = cardHolder("","","","","")

  ### create a list of cardholders
  list_of_cardHolders=[]
  list_of_cardHolders.append(cardHolder("4532772818527395",1234,"John","joseph",150.31))
  list_of_cardHolders.append(cardHolder("9032764231478920",3824,"kalyan","kumar",321.13))
  list_of_cardHolders.append(cardHolder("5327728185273956",1698,"anadha","krishnan",105.35))
  list_of_cardHolders.append(cardHolder("7032772818524212",2345,"sri","nivash",851.84))
  list_of_cardHolders.append(cardHolder("8132772818527001",1024,"nandha","kuamr",54.27))

  ### prompt user for debit card number

  debitCardNum=""
  while True:
    try:
      debitCardNum = input("please enter your debit card:")
      ### check against list
      debitMatch= [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
      if(len(debitMatch)) > 0:
        current_user = debitMatch[0]
        break
      else:
        print("Card number not recognized. please try again.") 
    except:
      print("card number not recognized. please try again.")

### prompt for PIN
while True:
  try:
    userPin= int(input("please enter your pin: ").strip())
    if(current_user.get_pin()==userPin):
      break
    else:
      print("Invalid PIN. please try again")

  except:
    print("Invalid PIN. please try again.")

  ### print options
  print("Welcome ", current_user.get_firstName(),":)")
  option =0
  while (True):
    print_menu()
    try:
      option = int(input())
    except:
      print("Invalid input. please try again")

    if(option==1):
     deposit(current_user)
    elif(option==2):
     withdraw(current_user)
    elif(option==3):
     check_balance(current_user)
    elif(option==4):
     break
    else:
     option = 0
      
  print("Thank you. Have  a nice day :)")




