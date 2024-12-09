file = open('accounts.csv', 'r')

lines = file.readlines()

accounts = {}

for line in lines:
    parts = line.strip().split(',')
    if parts[0] != 'id':
        account = {'id': parts[0], 'pin': parts[1], 
                   'name': parts[2], 'balance': float(parts[3])}
        accounts[parts[0]] = account

accounts['1']['balance'] = 0
print(accounts)

# Save the file
wfile = open('accounts.csv', 'w')
wfile.write("id,pin,name,balance\n")
for key in accounts:
    wfile.write(accounts[key]['id'] + ',' + accounts[key]['pin'] + ',' +
                accounts[key]['name'] + ',' + 
                str(accounts[key]['balance']) + '\n')