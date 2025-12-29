import json
from dataclasses import dataclass, asdict


@dataclass
class account_user:
    name: str
    password: str
    role: str
    balance: float
    currencies: dict

@dataclass
class account_admin:
    name: str
    password: str
    role: str


@dataclass
class currency:
    index: int
    name: str
    symbol: str
    price: float
    
@dataclass
class transactions:
    username : str
    type :str
    symbol : str
    quantityy : float
    price : float
    total : float


def user_sign_up():
    info_signup = []

    try:
        with open("user_signup.json", "r") as info:
            sign_info = json.load(info)
    except (FileNotFoundError, FileExistsError):
        sign_info = []
    try:
        with open("user_signup.json", "r") as admin_in:
            admin_sign_up = json.load(admin_in)
    except (FileNotFoundError, FileExistsError):
        admin_sign_up = []
    while True:
        name = input("Enter Name :")
        password = input("Enter password :")

        user_info = False
        for user in sign_info:
            if user["name"] == name:
                user_info = True
                break
        for user in admin_sign_up:
            if user["name"] == name:
                user_info = True
                break

        if user_info:
            print("Name already exist . try again.")
            continue
        c = account_user(
            name, password, role="user", balance=1000, currencies=None,
        )
        info_signup.append(asdict(c))
        sign_info.extend(info_signup)
        break

    with open("user_signup.json", "w") as info_write:
        json.dump(sign_info, info_write, indent=4)
    print("Congratulation you got 1000 USD as your signup reward.")


def admin_signup():
    info_signup = []
    try:
        with open("admin_signup.json", "r") as info:
            sign_info = json.load(info)
    except (FileExistsError, FileNotFoundError):
        sign_info = []
    try:
        with open("user_signup.json", "r") as user_in:
            user_signup = json.load(user_in)
    except (FileExistsError, FileNotFoundError):
        user_signup = []

    while True:
        name = input("Enter Name :")
        password = input("Enter Password :")
        role = input("Enter the role :")
        user_info = False
        for user in sign_info:
            if user["name"] == name:
                user_info = True
                break
        for user in user_signup:
            if user["name"] == name:
                user_info = True
                break
        if user_info:
            print("Name already exist.Try again.")
            continue
        if role == "user":
            c = account_user(
                name, password, role, balance=1000, currencies=None, quantity=0
            )
            info_signup.append(asdict(c))
            sign_info.extend(info_signup)
            break
        elif role == "admin":
            c = account_user(name, password, role)
            info_signup.append(asdict(c))
            sign_info.extend(info_signup)
            break
    if role == "user":
        with open("user_signup.json", "w") as information:
            json.dump(sign_info, information, indent=4)
        print("Congratulation you got 1000 USD as your signup reward.")
    if role == "admin":
        with open("admin_signup.json", "w") as information:
            json.dump(sign_info, information, indent=4)


user_current_index = 0
crypto_index = 0


def login():
    global user_current_index
    name = input("Enter Name :")
    password = input("Enter password :")
    try:
        with open("admin_signup.json", "r") as info:
            sign_info = json.load(info)
    except (FileExistsError, FileNotFoundError):
        print("No users found. Please sign up first.")
        return None
    try:
        with open("user_signup.json", "r") as user_in:
            user_signup = json.load(user_in)
    except (FileExistsError, FileNotFoundError):
        print("No users found. Please sign up first.")
        return None

    i = 0
    for user in sign_info:
        if user["name"] == name and user["password"] == password:
            print(f"WELCOME {name}")
            user_current_index = i
            return user["role"]
        i += 1

    j = 0
    for user in user_signup:
        if user["name"] == name and user["password"] == password:
            print(f"WELCOME {name}")
            user_current_index = j
            return user["role"]
        j += 1


def crpto_currency():
    global crypto_index
    info_currencies = []
    try:
        with open("currencies.json", "r") as info:
            currencies_info = json.load(info)
    except (FileExistsError, FileNotFoundError):
        currencies_info = []
    if currencies_info:
        crypto_index = currencies_info[-1]["index"] + 1
    else:
        crypto_index = 1
    while True:
        name = input("ENTER NAmE OF THE CRYPTO CURRENCY :")
        symbol = input("ENTER THE SYMBOL :")
        price = round(float(input("ENTER THE PRICE :")))
        found = False
        for i in currencies_info:
            if i["name"] == name:
                found = True
                break
        if found:
            print("Name already exist.Try again.")
            continue
        c = currency(crypto_index, name, symbol, price)
        info_currencies.append(asdict(c))
        currencies_info.extend(info_currencies)
        break

    with open("currencies.json", "w") as write_info:
        json.dump(currencies_info, write_info, indent=4)


def show():
    try:
        with open("currencies.json", "r") as info:
            info_currency = json.load(info)
    except (FileExistsError, FileNotFoundError):
        info_currency = []

    for i in range(len(info_currency)):
        print(f"INDEX : {info_currency[i]["index"]} ")
        print(f"NAME : {info_currency[i]["name"]} ")
        print(f"SYMBOL : {info_currency[i]["symbol"]} ")
        print(f"PRICE : {info_currency[i]["price"]} ")
        print("--------------------------------------")


def remove():
    global crypto_index
    updated_list = []
    try:
        with open("currencies.json", "r") as info:
            info_currency = json.load(info)
    except (FileExistsError, FileNotFoundError):
        info_currency = []

    show()
    if not info_currency:
        print("NO CURRENCY TO REMOVE")
    index = int(input("ENTER THE iNDEX OF THE CURRENCY YOU WANT TO REMOVE :"))
    while index > len(info_currency):
        index = int(input("ENTER THE INDEX OF THE currency YOU WANT TO REMOVE :"))

    updated_list = []
    count = 1
    for crypto in info_currency:
        if crypto["index"] != index:
            crypto["index"] = count
            updated_list.append(crypto)
            count += 1
        with open("currencies.json", "w") as write_info:
            json.dump(updated_list, write_info, indent=4)


def update_price():
    try:
        with open("currencies.json", "r") as info:
            info_currency = json.load(info)
    except (FileExistsError, FileNotFoundError):
        info_currency = []

    index = int(input("ENTER THE INDEX OF THE CURRENCY YOU WANT UPDATE:"))
    while index > len(info_currency):
        print("INDEX NOT FOUND:")
        index = int(input("ENTER THE INDEX OF THE CURRENCY YOU WANT TO REMOVE :"))

    new_price = round(float(input("ENTER THE UPDATED PRICE :")))

    for i in range(len(info_currency)):
        if info_currency[i]["index"] == index:
            info_currency[i]["price"] = new_price

    with open("currencies.json", "w") as write_info:
        json.dump(info_currency, write_info, indent=4)


def see_users():
    with open("user_signup.json", "r") as info:
        user_info = json.load(info)

    for i in range(len(user_info)):
        print(f"NAME :{user_info[i]["name"]}")
        print(f"PASSWORD :{user_info[i]["password"]}")
        print(f"BALANCE :{user_info[i]["balance"]}")
        print(f"ROLE :{user_info[i]["role"]}")
        print(f"CURRENCIES :{user_info[i]["currencies"]}")
        print("---------------------------------------")


def find_user():
    try:
        with open("user_signup.json", "r") as info:
            user_info = json.load(info)
    except (FileExistsError, FileNotFoundError):
        user_info = []

    name = input("ENTER NAME OF THE USER :")
    found = False

    for i in range(len(user_info)):
        if name == user_info[i]["name"]:
            found = True
            print(f"NAME :{user_info[i]["name"]}")
            print(f"PASSWORD :{user_info[i]["password"]}")
            print(f"BALANCE :{user_info[i]["balance"]}")
            print(f"ROLE :{user_info[i]["role"]}")
            print(f"CURRENCIES :{user_info[i]["currEncies"]}")
    if not found:
        print("NO CURRENCY FOUND")


def find_currency():
    try:
        with open("currencies.json", "r") as info:
            user_info = json.load(info)
    except (FileExistsError, FileNotFoundError):
        user_info = []

    name = input("ENTER NAME OF THE CURRENCY :")
    found = False
    for i in range(len(user_info)):
        if name == user_info[i]["name"]:
            found = True
            print(f"INDEX :{user_info[i]["index"]}")
            print(f"NAME :{user_info[i]["name"]}")
            print(f"SYMBOL :{user_info[i]["symbol"]}")
            print(f"PRICE :{user_info[i]["price"]}")

    if not found:
        print("NO CURRENCY FOUND")


def buy_currency():
    global user_current_index
    existing_info = []
    try:
        with open("currencies.json", "r") as info:
            currency_info = json.load(info)
    except (FileExistsError, FileNotFoundError):
        currency_info = []
        
    try:
        with open("transactions.json","r") as transaction_info:
            info_transaction = json.load(transaction_info)
    except(FileExistsError,FileNotFoundError):
        info_transaction = []
    
    show()

    index = int(input("ENTER THE INDEX OF THE CURRENCY WANT TO BUY :"))
    real_index = index - 1

    selected_currency = currency_info[real_index]

    if real_index < 0 or real_index >= len(currency_info):
        print("INVALID INDEX")
        return

    try:
        with open("user_signup.json", "r") as info_login:
            login_info = json.load(info_login)
    except:
        print("No users found.")
        return

    current_user = login_info[user_current_index]
    
    quantity = float(input("ENTER THE QUANTITY YOU WANT TO BUY :"))
    total = selected_currency["price"]*quantity

    if current_user["balance"] < total:
        print("LOW BALANCE")
        return

    else:
        current_user["balance"] = current_user["balance"] - total
    if current_user["currencies"] is None:
        current_user["currencies"] = {}

    symbol = selected_currency["symbol"]

    if symbol in current_user["currencies"]:
        current_user["currencies"][symbol]["quantity"] += quantity
    else:
        current_user["currencies"][symbol] = {"name": selected_currency["name"],"price": selected_currency["price"],"quantity": quantity}
        print(f"SUCCESSFULLY BOUGHT {selected_currency['name']}")
        print(f"REMAINING BALANCE = {current_user['balance']}")
        
        c = transactions(username=current_user["name"],type="BUY",symbol=symbol,quantityy=quantity,price=selected_currency["price"],total=total)
        existing_info.append(asdict(c))
        info_transaction.extend(existing_info)
        
        with open("transactions.json","w") as write_info:
            json.dump(info_transaction,write_info,indent=4)
        
        with open("user_signup.json", "w") as write_file:
            json.dump(login_info, write_file, indent=4)

def sell_currency():
    global user_current_index
    cur_info = []
    
    with open("user_signup.json" , "r") as info:
        user_info = json.load(info)
        
    with open("currencies.json","r") as infor:
        currency_info = json.load(infor)
        
    current_user = user_info[user_current_index]
    
    if current_user["currencies"] is None:
        print("NO CURRENCY TO SELL")
        return
    else:
        print(current_user["currencies"])
    symbol = input("ENTER THE SYMBOL OF THE CURRENCY YOU WANT TO SELL :").upper()
    
    if symbol not in current_user["currencies"]:
        print("WRONG SYMBOL.")
        return
    
    current_cost = 0
    for i in currency_info:
        if symbol == i["symbol"]:
            current_cost = i["price"]
            break
        
    available_quantity = current_user["currencies"][symbol]["quantity"]
    print("AVAILABLE QUANTITY =",available_quantity)
    sell = float(input("ENTER THE QUANTTY YOU WANT TO SELL :"))
    
    while (sell > available_quantity):
        print("DONT HAVE MUCH QUANTITY")
        sell = float(input("ENTER THE QUANTTY YOU WANT TO SELL :"))
    
    total_cost = available_quantity * current_cost
    current_user["currencies"][symbol]["quantity"] -= available_quantity
    if current_user["currencies"][symbol]["quantity"] == 0:
        del current_user["currencies"][symbol]
    current_user["balance"] += total_cost
    transaction_data = []
    c = transactions(username=current_user["name"],type="SELL",symbol=symbol,quantityy=available_quantity,price=current_cost,total=total_cost)
    transaction_data.append(asdict(c))
    try:
        with open("transactions.json", "r") as read_info:
            existing_transactions = json.load(read_info)
    except:
        existing_transactions = []
    
    existing_transactions.extend(transaction_data)
    
    with open("transactions.json", "w") as write_info:
        json.dump(existing_transactions, write_info, indent=4)

    with open("user_signup.json", "w") as write_info:
        json.dump(user_info, write_info, indent=4)
    
    print(" SUCCESSFULLY SOLD ")
    
def see_wallet():
    global user_current_index
    
    try:
        with open("user_signup.json", "r") as info:
            user_info = json.load(info)
    except:
        print("No users found.")
        return

    current_user = user_info[user_current_index]
    
    print(f"NAME :{current_user["name"]}")
    print(f"PASSWORD :{current_user["password"]}")
    print(f"BALANCE :{current_user["balance"]}")
    print(f"CURRENCIES :{current_user["currencies"]}")
    
def transaction_history():
    global user_current_index
    
    try:
        with open("transactions.json", "r") as info:
            transactions_info = json.load(info)
    except:
        print("No users found.")
        return
    try:
        with open("user_signup.json", "r") as information:
            user_info = json.load(information)
    except:
        print("No users found.")
        return
    
    name = user_info[user_current_index]["name"]

    for i in range(len(transactions_info)):
        username = transactions_info[i]["username"]
        if(name == username):
            print(f"NAME :{transactions_info[i]["username"]}")
            print(f"TYPE :{transactions_info[i]["type"]}")
            print(f"SYMBOL :{transactions_info[i]["symbol"]}")
            print(f"QUANTITY :{transactions_info[i]["quantityy"]}")
            print(f"PRICE :{transactions_info[i]["price"]}")
            print(f"TOTAL :{transactions_info[i]["total"]}")
            print("---------------------------------------")  
    
def all_transactions():
        
    try:
        with open("transactions.json", "r") as info:
            transactions_info = json.load(info)
    except:
        print("No users found.")
        return 
    
    for i in range(len(transactions_info)):
        print(f"NAME :{transactions_info[i]["username"]}")
        print(f"TYPE :{transactions_info[i]["type"]}")
        print(f"SYMBOL :{transactions_info[i]["symbol"]}")
        print(f"QUANTITY :{transactions_info[i]["quantityy"]}")
        print(f"PRICE :{transactions_info[i]["price"]}")
        print(f"TOTAL :{transactions_info[i]["total"]}") 
        print("---------------------------------------")          