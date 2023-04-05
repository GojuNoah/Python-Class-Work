transactions = []


def get_transaction():
    print('-------Menu-------')
    print('1.Add Transaction')
    print('2.Delete Transaction')
    print('3.Edit Transaction')
    print('4.Display Transaction')
    print('5.Exit the Program')
    selections = int(input('Enter a number 1-5, for your choice: '))
    return selections


def add_transaction():
    x = input('Enter new transaction: ')
    transactions.append(x)


def delete_transaction():
    y = input('Enter Transaction to be deleted: ')
    if y in str(get_transaction()):
        item_number = transactions.index(y)
        del transactions[item_number]
    else:
        print(y, 'Transaction not found.')


def edit_transaction():
    edit = input('Enter the transaction to edit: ')
    if edit in transactions:
        new_transaction = input('Enter your edit to the transaction: ')
        edit_transaction_index = new_transaction.index(edit)
        transactions[edit_transaction_index] = new_transaction
    else:
        print(edit, 'Is not found in the transaction list. ')


def display_transactions():
    print('The following are transactions')
    for i in range(len(transactions)):
        print(transactions[i])


while True:
    print("\n")
    selection = get_transaction()
    if selection == 1:
        add_transaction()
    elif selection == 2:
        delete_transaction()
    elif selection == 3:
        edit_transaction()
    elif selection == 4:
        display_transactions()
    elif selection == 5:
        print('Exiting program...')
        break
    else:
        print('Invalid entry. Try 1-4 or 5 to exit')
print('Exiting loop')
