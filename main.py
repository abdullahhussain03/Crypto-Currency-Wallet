import funct

print("DIGITAL CRYPTOCURRENCY WALLET")
start = int(input("PRESS 1 TO SIGNUP:\nPRESS 0 TO LOGIN :"))
success = None
if start == 1:
    funct.user_sign_up()
    success = funct.login()
elif start == 0:
    success = funct.login()
    while not success:
        print("NO USER FOUND . TRY AGAIN")
        start = int(input("PRESS 1 TO SIGNUP:\nPRESS 0 TO LOGIN :"))
        if start == 1:
            funct.user_sign_up()
            success = funct.login()
        elif start == 0:
            success = funct.login()

stop = 1
option = 0
while stop != 0:
    if success == "user":
        option = int(input("PRESS 1 TO BUY A CURRENCY:\nPRESS 2 TO SELL A CURRENCY:\nPRESS 3 TO SEARCH CRYPTOCURRENCIES:\nPRESS 4 TO SEE THE WALLET:\nPRESS 5 TO SEE TRANSACTION HISTORY:"))
        if(option==1):
            funct.buy_currency()
        elif(option == 2):
            funct.sell_currency()
        elif(option == 3):
            funct.find_currency()
        elif(option == 4):
            funct.see_wallet()
        elif(option == 5):
            funct.transaction_history()
        
    elif success == "admin":
       option = int(input("PRESS 1 TO SIGNUP NEW ACCOUNT\nPRESS 2 TO ADD CURRENCY:\nPRESS 3 TO SEE ALL CURRENCIES:\nPRESS 4 TO REMOVE CURRENCY:\nPRESS 5 TO UPDATED THE PRICE\nPRESS 6 TO SEE ALL USERS:\nPRESS 7 TO FIND A USER BY NAME:\nPRESS 8 TO FIND A CURRENCY BY NAME:\nPRESS 9 TO SEE ALL USERS TRANSACTIONS:"))
       if(option == 1):
           funct.admin_signup()
       elif(option == 2):
           funct.crpto_currency()
       elif(option == 3):
           funct.show()
       elif(option == 4):
           funct.remove()
       elif(option == 5):
           funct.update_price()
       elif(option == 6):
           funct.see_users()
       elif(option == 7):
           funct.find_user()
       elif(option == 8):
           funct.find_currency()
       elif(option == 9):
           funct.all_transactions()
    stop = int(input("PRESS 0 TO END\nPRESS 1 TO GET BACK :"))