# HOMEWORK #4. Task 1. Task 2. Task 3. ... Task 5.
from datetime import datetime
from hashlib import sha256
import json, os


class Bank:
    BANK_NAME = "TheBank"

    if os.path.exists("db/clients.json"):
        with open("db/clients.json") as fh:
            clients_of_bank = json.loads(fh.read())
    else:
        os.system("mkdir db")
        clients_of_bank = dict()

    if os.path.exists("db/accounts.json"):
        with open("db/accounts.json") as fh:
            bank_accounts = json.loads(fh.read())
    else:
        os.system("mkdir db")
        bank_accounts = dict()

    client_id = None
    client_name = None

    usdbyn = 3.1
    eurbyn = 3.5
    usdeur = usdbyn / eurbyn
    eurusd = eurbyn / usdbyn


    def log_calls(func):
        def wrapper(*args, **kwargs):
            if os.path.exists("logs/logs.json"):
                with open("logs/logs.json") as fh:
                    logs = json.loads(fh.read())
            else:
                os.system("mkdir logs")
                logs = dict()
            session = args[0]
            user_id = session.client_id
            launch_time = datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
            func_name = func.__name__
            if len(args) == 1:
                logs[launch_time] = ["Client", user_id, func_name]
            elif len(args) == 2:
                logs[launch_time] = ["Client", user_id, func_name]
            elif len(args) == 4:
                if func_name == "reg_account":
                    logs[launch_time] = ["Account", user_id, func_name, args[1].acc_id, args[2], args[3], "-"]
                else:
                    logs[launch_time] = ["Account", user_id, func_name, args[1], args[2], args[3], "-"]
            elif len(args) == 6:
                logs[launch_time] = ["Account", user_id, func_name, args[1], args[3], args[4], args[2]]
            with open('logs/logs.json', 'w') as fh:
                json.dump(logs, fh, indent='    ')
            result = func(*args, **kwargs)
            return result
        return wrapper


    def get_hash(self, user_string):
        hash_string = sha256(user_string.encode('utf-8')).hexdigest()
        return hash_string

    def generate_id(self, prefix):
        if len(self.clients_of_bank) > 0:
            cli_id = int(str(list(self.clients_of_bank.keys())[-1])[len(prefix)+1:]) + 1
            return f"{prefix}_{cli_id}"
        else:
            return f"{prefix}_1"

    def generate_id_acc(self, prefix):
        if len(self.bank_accounts) > 0:
            acc_id = int(str(list(self.bank_accounts.keys())[-1])[len(prefix)+1:]) + 1
            return f"{prefix}_{acc_id}"
        else:
            return f"{prefix}_1"

    @log_calls
    def reg_client(self, client):
        self.clients_of_bank[client.client_id] = [client.login, client.hash_password, client.fullname]
        self.client_id = client.client_id
        self.client_name = client.fullname
        with open('db/clients.json', 'w') as fh:
            json.dump(self.clients_of_bank, fh, indent='    ')

    @log_calls
    def logout_client(self):
        self.client_id = None
        self.client_name = None

    @log_calls
    def login_client(self):
        pass

    @log_calls
    def reg_account(self, account, balance, currency):
        self.bank_accounts[account.acc_id] = [account.client_id, account.currency, account.balance]
        with open('db/accounts.json', 'w') as fh:
            json.dump(self.bank_accounts, fh, indent='    ')

    def get_client_account(self, client_id):
        client_accounts = dict()
        if len(self.bank_accounts) > 0:
            for i, j in self.bank_accounts.items():
                if j[0] == self.client_id:
                    client_accounts[i] = j
        return client_accounts

    @log_calls
    def del_account(self, acc_id, balance, currency):
        del self.bank_accounts[acc_id]
        with open('db/accounts.json', 'w') as fh:
            json.dump(self.bank_accounts, fh, indent='    ')

    @log_calls
    def top_up_account(self, acc_id, top_up_amount, currency):
        self.bank_accounts[acc_id][2] += top_up_amount
        with open('db/accounts.json', 'w') as fh:
            json.dump(self.bank_accounts, fh, indent='    ')

    @log_calls
    def withdrawal_account(self, acc_id, withdrawal_amount, currency):
        self.bank_accounts[acc_id][2] -= withdrawal_amount
        with open('db/accounts.json', 'w') as fh:
            json.dump(self.bank_accounts, fh, indent='    ')

    @log_calls
    def transfer_account(self, acc_number_1, acc_number_2, transfer_funds, currency_1, currency_2):
        self.bank_accounts[acc_number_1][2] -= transfer_funds
        conversion_rate = 1
        if currency_1 == currency_2:
            conversion_rate = 1
        elif currency_1 == "USD":
            if currency_2 == "EUR":
                conversion_rate = self.usdeur
            elif currency_2 == "BYN":
                conversion_rate = self.usdbyn
        elif currency_1 == "EUR":
            if currency_2 == "USD":
                conversion_rate = self.eurusd
            elif currency_2 == "BYN":
                conversion_rate = self.eurbyn
        elif currency_1 == "BYN":
            if currency_2 == "EUR":
                conversion_rate = 1 / self.eurbyn
            elif currency_2 == "USD":
                conversion_rate = 1 / self.usdbyn
        self.bank_accounts[acc_number_2][2] += (transfer_funds * conversion_rate)
        with open('db/accounts.json', 'w') as fh:
            json.dump(self.bank_accounts, fh, indent='    ')

    def print_account(self, acc_statement_filename, acc_stat_text):
        if not os.path.exists("stat/"):
            os.system("mkdir stat")
        with open("stat/"+acc_statement_filename, "w") as fh:
            fh.write(acc_stat_text)

    def his_cli_acc(self):
        if os.path.exists("logs/logs.json"):
            with open("logs/logs.json") as fh:
                logs = json.loads(fh.read())
        else:
            os.system("mkdir logs")
            logs = dict()
        return logs



class Client(Bank):
    def __init__(self, login="", password="", fullname=""):
        self.client_id = self.generate_id(self.__class__.__name__)
        self.login = login
        self.hash_password = self.get_hash(password)
        self.fullname = fullname


class BankAccount(Bank):
    def __init__(self, client_id="", currency = "", balance=""):
        self.client_id = client_id
        self.currency = currency
        self.acc_id = self.generate_id_acc(self.__class__.__name__)
        self.balance = balance


def welcome_bank():
    os.system('cls' if os.name == 'nt' else 'clear')
    bank_session = Bank
    print("")
    print(f"Welcome to \"{Bank.BANK_NAME}\"!")
    while True:
        if bank_session.client_id is None:
            print("")
            print(f"To continue, please LogIn or Register with {bank_session.BANK_NAME}.Online.")
            print("")
            print(
                "Enter:\n"
                "    L - to login;\n"
                "    R - to register;\n"
                "    Q - to quit."
            )
            user_select = input("Please make your choice: ")
            if user_select.upper() == "L":
                login_client(bank_session)
                continue
            elif user_select.upper() == "R":
                os.system('cls' if os.name == 'nt' else 'clear')
                reg_new_client(bank_session)
                continue
            elif user_select.upper() == "Q":
                print("")
                print(f"Thank you for visiting {bank_session.BANK_NAME}. See you soon and have a nice day.")
                bank_session.logout_client(bank_session)
                break
            else:
                print("Please check the correctness of your choice.")
                continue
        else:
            print("")
            print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
            print("")
            print(
                "Select one of the following actions:\n"
                "    B - go to bank accounts;\n"
                "    H - view the history of visits to your personal account;\n"
                "    O - log out of your account;\n"
                "    Q - to quit."
            )
            user_select = input("Please make your choice: ")
            if user_select.upper() == "B":
                os.system('cls' if os.name == 'nt' else 'clear')
                bank_online(bank_session)
                continue
            elif user_select.upper() == "H":
                os.system('cls' if os.name == 'nt' else 'clear')
                history_client(bank_session)
                continue
            elif user_select.upper() == "O":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print("You have successfully logged out of your account.")
                bank_session.logout_client(bank_session)
                continue
            elif user_select.upper() == "Q":
                print("")
                print(f"Thank you for visiting {bank_session.BANK_NAME}. See you soon and have a nice day.")
                bank_session.logout_client(bank_session)
                break


def history_client(bank_session):

    logs = bank_session.his_cli_acc(bank_session)

    dict_hist = {
        "reg_client": "Registration client",
        "logout_client": "Log out",
        "login_client": "Login"
    }

    print("")
    print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
    print("")
    print("Below is the history of visits to your personal account.")
    print("")
    print("  Date-time:           Status:")
    for i in logs.keys():
        if logs[i][0] == "Client" and logs[i][1] == bank_session.client_id:
            print(f"  {i}  {dict_hist[logs[i][2]]}")
    while True:
        user_select = input("\nTo exit to the previous menu, enter \"Q\": ")
        if user_select.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            continue


def history_account(bank_session):

    logs = bank_session.his_cli_acc(bank_session)

    dict_hist = {
        "reg_account": "Open bank account",
        "del_account": "Close bank account",
        "top_up_account": "Top up account",
        "withdrawal_account": "Withdrawal amount",
        "transfer_account": "Transfer amount"
    }

    print("")
    print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
    print("")
    print("Below is a history of changes to your bank accounts.")
    print("")
    print("  Date-time:".ljust(24, " "), "Status:".ljust(22, " "), "Account:".ljust(25, " "), "Amounеt:".ljust(16, " "), "Transfer to:", sep="")
    for i in logs.keys():
        if logs[i][0] == "Account" and logs[i][1] == bank_session.client_id:

            date_time = str(i).ljust(22, " ")
            status_do = str(dict_hist[logs[i][2]]).ljust(22, " ")
            account_num_1 = str(logs[i][3]).ljust(25, " ")
            sum_op = str(logs[i][4]).rjust(8, " ")
            cur_op = str(logs[i][5]).ljust(7, " ")
            account_num_2 = str(logs[i][6])

            print(f"  {date_time}{status_do}{account_num_1}{sum_op} {cur_op}{account_num_2}")
    while True:
        user_select = input("\nTo exit to the previous menu, enter \"Q\": ")
        if user_select.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            continue


def reg_new_client(bank_session):
    print("")
    print(f"Thank you for choosing {Bank.BANK_NAME}. To register, fill in the following fields, please.")
    print("")
    fullname = input("Enter your fullname: ")
    while True:
        login = input("Enter your login: ")
        login_list = [i[0] for i in bank_session.clients_of_bank.values()]
        if login in login_list:
            print("A user with this login already exists, please think of another login.")
            continue
        else:
            break
    while True:
        password = input("Please enter your password: ")
        if password == input("Please enter your password again: "):
            client = Client(login=login, password=password, fullname=fullname)
            bank_session.client_id = client.client_id
            bank_session.reg_client(bank_session, client)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("The passwords entered do not match. Please try again.")
            continue


def login_client(bank_session):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print(f"Welcome to \"{Bank.BANK_NAME}\"!")
        print("")
        client_id = None
        hash_password = None
        client_name = None
        cli_auth = False
        login = input("To log in, enter your login: ")
        for i, j in bank_session.clients_of_bank.items():
            if j[0] == login:
                client_id = i
                hash_password = j[1]
                client_name = j[2]
                break
        if client_id is None:
            print(
                "The user with such login is not registered.\n"
                "Select one of the following actions:\n"
                "    L - try to login again,\n"
                "    R - register;\n"
                "    Q - to quit."
            )
            user_select = input("Please make your choice: ")
            if user_select.upper() == "L":
                continue
            elif user_select.upper() == "R":
                os.system('cls' if os.name == 'nt' else 'clear')
                reg_new_client(bank_session)
                break
            elif user_select.upper() == "Q":
                break
            else:
                print("Please check the correctness of your choice.")
                continue
        elif client_id is not None:
            number_of_attempts = 3
            while number_of_attempts > 0:
                print("")
                password = input(f"Please enter your password ({number_of_attempts} attempts left): ")
                if bank_session.get_hash(bank_session, password) == hash_password:
                    bank_session.client_id = client_id
                    bank_session.client_name = client_name
                    bank_session.login_client(bank_session)
                    cli_auth = True
                    break
                else:
                    print("Passwords do not match. Please try again.")
                    number_of_attempts -= 1
        if cli_auth:
            os.system('cls' if os.name == 'nt' else 'clear')
            break


def show_bank_accounts(bank_session):
    client_accounts = bank_session.get_client_account(bank_session, bank_session.client_id)
    currency_list = [i[1] for i in client_accounts.values()]
    print("")
    print(f"You have {len(client_accounts)} open accounts.")
    print("")
    usd = eur = byn = 0.0
    for i, item in enumerate(client_accounts):
        print(f"{i + 1}. {item} account balance {round(client_accounts[item][2], 2)} {client_accounts[item][1]}")
        if client_accounts[item][1] == "USD":
            usd += client_accounts[item][2]
        elif client_accounts[item][1] == "EUR":
            eur += client_accounts[item][2]
        elif client_accounts[item][1] == "BYN":
            byn += client_accounts[item][2]
    print("")
    print(f"Balance on your accounts: {round(usd, 2)} USD, {round(eur, 2)} EUR, {round(byn, 2)} BYN")
    all_in_usd = round(usd + (eur * Bank.eurusd) + (byn / Bank.usdbyn), 2)
    all_in_eur = round((usd * Bank.usdeur) + eur + (byn / Bank.eurbyn), 2)
    all_in_byn = round((usd * Bank.usdbyn) + (eur * Bank.eurbyn) + byn, 2)
    print("The total balance on all your accounts, converted at the current rate, is:", f"    {all_in_usd} USD",
          f"    {all_in_eur} EUR", f"    {all_in_byn} BYN", sep="\n")
    print("")
    return client_accounts, currency_list


def bank_online(bank_session):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("")
        print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
        print("In this menu you can manage your accounts.")
        client_accounts, currency_list = show_bank_accounts(bank_session)
        print("Select one of the following actions:")
        if len(client_accounts) < 3:
            print("    C - create new account;")
        if len(client_accounts) > 0:
            print(
                "    D - close(delete) account;\n"
                "    U - top up your account;\n"
                "    W - withdraw amount from account;"
            )
        if len(client_accounts) > 1:
            print("    T - transfer money between accounts;")
        print(
            "    P - save account statement to file;\n"
            "    H - history of changes to your bank accounts;\n"
            "    Q - to exit to main menu."
        )
        user_select = input("Please make your choice: ")
        if len(client_accounts) < 3:
            if user_select.upper() == "C":
                os.system('cls' if os.name == 'nt' else 'clear')
                create_account(bank_session)
                continue
        if len(client_accounts) > 0:
            if user_select.upper() == "D":
                os.system('cls' if os.name == 'nt' else 'clear')
                del_acc_number = close_account(bank_session)
                print(f"You have successfully deleted the account: {del_acc_number}.")
                continue
            if user_select.upper() == "U":
                os.system('cls' if os.name == 'nt' else 'clear')
                top_up_acc_number, top_up_amount, currency_acc = top_up_account(bank_session)
                print(f"You have successfully topped up {top_up_acc_number} with the amount of {top_up_amount} {currency_acc}.")
                continue
            if user_select.upper() == "W":
                os.system('cls' if os.name == 'nt' else 'clear')
                withdrawal_acc_number, withdrawal_funds, currency_acc = withdrawal_of_funds(bank_session)
                print(f"You have successfully withdrawn amount {withdrawal_funds} {currency_acc} from account {withdrawal_acc_number}.")
                continue
        if len(client_accounts) > 1:
            if user_select.upper() == "T":
                os.system('cls' if os.name == 'nt' else 'clear')
                acc_number_1, acc_number_2, transfer_funds, currency_acc = transfer_amount(bank_session)
                print(f"You have successfully transferred from account {acc_number_1} to account {acc_number_2} the amount of {transfer_funds} {currency_acc}.")
                continue
        if user_select.upper() == "P":
            acc_statement_filename, acc_stat_text = acc_stat(bank_session)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Your account statement has been saved to file {acc_statement_filename}.")
            continue

        if user_select.upper() == "H":
            os.system('cls' if os.name == 'nt' else 'clear')
            history_account(bank_session)
            continue

        if user_select.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please check the correctness of your choice.")
        continue


def acc_stat(bank_session):
    client_accounts = bank_session.get_client_account(bank_session, bank_session.client_id)
    accounts = ""
    usd = eur = byn = 0.0
    for i, item in enumerate(client_accounts):
        accounts += f"    {i + 1}. {item}: account balance {round(client_accounts[item][2], 2)} {client_accounts[item][1]}\n"
        if client_accounts[item][1] == "USD":
            usd += client_accounts[item][2]
        elif client_accounts[item][1] == "EUR":
            eur += client_accounts[item][2]
        elif client_accounts[item][1] == "BYN":
            byn += client_accounts[item][2]
    all_in_usd = round(usd + (eur * Bank.eurusd) + (byn / Bank.usdbyn), 2)
    all_in_eur = round((usd * Bank.usdeur) + eur + (byn / Bank.eurbyn), 2)
    all_in_byn = round((usd * Bank.usdbyn) + (eur * Bank.eurbyn) + byn, 2)
    acc_statement_filename = f"{Bank.BANK_NAME}_{bank_session.client_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    acc_stat_text =(
        f"{Bank.BANK_NAME}\n"
        f"\n"
        f"Statement of your bank accounts.\n"
        f"\n"
        f"As of {datetime.now().strftime('%d.%m.%Y at %H:%M:%S')} {bank_session.client_name} has {len(client_accounts)} open accounts.\n"
        f"\n"
        f"More details:\n"
        f"\n"
        f"{accounts}\n"
        f"\n"
        f"Balance on your accounts:\n"
        f"    - {round(usd, 2)} USD,\n"
        f"    - {round(eur, 2)} EUR,\n"
        f"    - {round(byn, 2)} BYN.\n"
        f"\n"
        f"\n"
        f"Informational.\n"
        f"\n"
        f"The total balance on all your accounts, converted at the current rate, is: \n"
        f"    - {all_in_usd} USD,\n"
        f"    - {all_in_eur} EUR,\n"
        f"    - {all_in_byn} BYN.\n"
        f"\n"
        f"© The {Bank.BANK_NAME} Team. We work so that you can relax ))).\n"
        f"\n"
    )
    bank_session.print_account(bank_session, acc_statement_filename, acc_stat_text)
    return acc_statement_filename, acc_stat_text


def check_float(user_string):
    try:
        float(user_string)
        return True
    except ValueError:
        return False


def create_account(bank_session):
    print("")
    print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
    _, currency_list = show_bank_accounts(bank_session)
    print("")
    print("To open a new bank account, please follow the instructions below. Enter \"Q\" to exit to main menu.")
    print("")
    break_out_flag = False
    all_currency_list = ["USD", "EUR", "BYN"]
    possible_currencies = [i for i in all_currency_list if i not in currency_list]
    while True:
        currency_acc = input(f"Whiten the account currency {possible_currencies}: ").upper()
        if currency_acc in possible_currencies:
            currency = currency_acc
            print("You can also top up your account or leave it zero.")
            break
        elif currency_acc == "Q":
            break_out_flag = True
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Please check the correctness of your choice.")
            continue
    while True:
        if break_out_flag:
            break
        balance = input(f"Enter the amount to top up your account {currency}: ")
        if check_float(balance) and float(balance) >= 0:
            balance = float(balance)
            break
        elif not balance:
            balance = 0
            break
        else:
            print("Please check the correctness of your choice.")
            continue
    if break_out_flag != True:
        client_acc = BankAccount(client_id=bank_session.client_id, currency=currency, balance=balance)
        os.system('cls' if os.name == 'nt' else 'clear')
        bank_session.reg_account(bank_session, client_acc, balance, currency)

def close_account(bank_session):
    while True:
        print("")
        print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
        client_accounts, currency_list = show_bank_accounts(bank_session)
        print("")
        print("To withdraw all funds from the account and close (delete) the account, enter the account number (BankAccount_*) or enter \"Q\" to cancel and go to the previous menu.")
        print("")
        acc_list = [i for i in client_accounts.keys()]
        user_select = input("Please make your choice: ")
        if user_select.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif user_select in acc_list:
            if bank_session.client_id == client_accounts[user_select][0]:
                bank_session.del_account(bank_session, user_select, client_accounts[user_select][2], client_accounts[user_select][1])
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You don't have such an account \"{user_select}\".")
            continue
    os.system('cls' if os.name == 'nt' else 'clear')
    return user_select

def top_up_account(bank_session):
    while True:
        print("")
        print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
        client_accounts, currency_list = show_bank_accounts(bank_session)
        print("")
        print("To top up, enter your account number (BankAccount_*) or enter \"Q\" to cancel and go to the previous menu.")
        print("")
        acc_list = [i for i in client_accounts.keys()]
        user_select = input("Please make your choice: ")
        currency = ""
        top_up_amount = 0
        if user_select.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif user_select in acc_list:
            if bank_session.client_id == client_accounts[user_select][0]:
                currency = client_accounts[user_select][1]
                while True:
                    top_up_amount = input(f"Enter the amount to top up your account {currency}: ")
                    if check_float(top_up_amount) and float(top_up_amount) >= 0:
                        top_up_amount = float(top_up_amount)
                        break
                    else:
                        print("Please check the correctness of your choice.")
                        continue
                bank_session.top_up_account(bank_session, user_select, top_up_amount, currency)
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You don't have such an account \"{user_select}\".")
            continue
    os.system('cls' if os.name == 'nt' else 'clear')
    return user_select, top_up_amount, currency

def withdrawal_of_funds(bank_session):
    while True:
        print("")
        print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
        client_accounts, currency_list = show_bank_accounts(bank_session)
        print("")
        print("Enter the account (BankAccount_*) from which you would like to withdraw funds or enter \"Q\" to cancel and go to the previous menu.")
        print("")
        acc_list = [i for i in client_accounts.keys()]
        user_select = input("Please make your choice: ")
        currency = ""
        withdrawal_amount = 0
        if user_select.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif user_select in acc_list:
            if bank_session.client_id == client_accounts[user_select][0]:
                currency = client_accounts[user_select][1]
                while True:
                    withdrawal_amount = input(f"Enter the amount to withdrawal from your account {currency}: ")
                    if check_float(withdrawal_amount) and float(withdrawal_amount) >= 0:
                        if float(withdrawal_amount) > client_accounts[user_select][2]:
                            print(f"There are not enough funds in your account {user_select} for withdrawal.")
                            continue
                        else:
                            withdrawal_amount = float(withdrawal_amount)
                            break
                    else:
                        print("Please check the correctness of your choice.")
                        continue
                bank_session.withdrawal_account(bank_session, user_select, withdrawal_amount, currency)
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You don't have such an account \"{user_select}\".")
            continue
    os.system('cls' if os.name == 'nt' else 'clear')
    return user_select, withdrawal_amount, currency

def transfer_amount(bank_session):
    break_out_flag = False
    while True:
        print("")
        print(f"Dear {bank_session.client_name}, welcome to {bank_session.BANK_NAME}.Online!")
        client_accounts, currency_list = show_bank_accounts(bank_session)
        print("Enter the account (BankAccount_*) from which you want to transfer funds or enter \"Q\" to cancel and go to the previous menu.")
        print("")
        acc_list = [i for i in client_accounts.keys()]
        acc_number_1 = input("Please make your choice: ")
        acc_number_2 = ""
        currency_1 = ""
        currency_2 = ""
        transfer_funds = 0
        if acc_number_1.upper() == "Q":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif acc_number_1 in acc_list:
            if bank_session.client_id == client_accounts[acc_number_1][0]:
                currency_1 = client_accounts[acc_number_1][1]
                while True:
                    print("")
                    acc_number_2 = input("Enter the account (BankAccount_*) to which you want to transfer funds: ")
                    print("")
                    if acc_number_2 in acc_list:
                        if bank_session.client_id == client_accounts[acc_number_2][0]:
                            currency_2 = client_accounts[acc_number_2][1]
                            break
                    else:
                        print(f"You don't have such an account \"{acc_number_2}\".")
                        continue
                while True:
                    transfer_funds = input(f"Enter the amount to transfer {currency_1}: ")
                    if check_float(transfer_funds) and float(transfer_funds) >= 0:
                        if float(transfer_funds) > client_accounts[acc_number_1][2]:
                            print(f"There are not enough funds in your account {acc_number_2} for transfer.")
                            continue
                        else:
                            transfer_funds = float(transfer_funds)
                            break
                    else:
                        print("Please check the correctness of your choice.")
                        continue
                bank_session.transfer_account(bank_session, acc_number_1, acc_number_2, transfer_funds, currency_1, currency_2)
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"You don't have such an account \"{acc_number_1}\".")
            continue
    os.system('cls' if os.name == 'nt' else 'clear')
    return acc_number_1, acc_number_2, transfer_funds, currency_1



welcome_bank()