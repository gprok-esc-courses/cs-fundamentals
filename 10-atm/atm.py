
def load_accounts():
    file = open('accounts.csv', 'r')
    lines = file.readlines()
    accounts = {}
    for line in lines:
        parts = line.strip().split(',')
        if parts[0] != 'id':
            account = {'id': parts[0], 'pin': parts[1], 
                    'name': parts[2], 'balance': float(parts[3])}
            accounts[parts[0]] = account
    return accounts


def save_accounts(accounts):
    wfile = open('accounts.csv', 'w')
    wfile.write("id,pin,name,balance\n")
    for key in accounts:
        wfile.write(accounts[key]['id'] + ',' + accounts[key]['pin'] + ',' +
                    accounts[key]['name'] + ',' + 
                    str(accounts[key]['balance']) + '\n')

def login_prompt():
    id = input("ID: ")
    pin = input("Pin: ")
    return id, pin


def menu_selection():
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("0. EXIT")
    choice = input("Choose: ")
    return choice


# Load accounts
accounts = load_accounts()
print(accounts)

# Loop 
while True:
    id, pin = login_prompt()
    if id in accounts and accounts[id]['pin'] == pin:
        print("Welcome,", accounts[id]['name'])
        choice = -1
        while choice != '0':
            choice = menu_selection()
            if choice == '1':
                print("Balance:", accounts[id]['balance'])
            elif choice == '2':
                amount = float(input("amount: ")) 
                if amount > 0:
                    accounts[id]['balance'] += amount
            elif choice == '3':
                amount = float(input("amount: ")) 
                if amount > 0 and amount <= accounts[id]['balance']:
                    accounts[id]['balance'] -= amount
            elif choice == '0':
                save_accounts(accounts)
            else:
                print("Wrong choice")
            # on EXIT save into the file 
    else:
        print("Invalid ID or PIN")