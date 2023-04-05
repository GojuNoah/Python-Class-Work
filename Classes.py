import pickle

orders = []


class OrderData:
    number = 0
    amount = 0.0
    order_type = ''

    def __init__(self, number, amount, order_type):
        self.number = number
        self.amount = amount
        self.order_type = order_type

    def set_number(self, number):
        self.number = number

    def set_amount(self, amount):
        self.amount = amount

    def set_name(self, order_type):
        self.order_type = order_type

    def get_number(self):
        return self.number

    def get_amount(self):
        return self.amount

    def get_name(self):
        return self.order_type

    def display_data(self):
        print('')
        print('Order Information')
        print('-----------------')
        print('Oder Number: ', self.number)
        print('Order Type: ', self.order_type)
        print('Order Amount: ', self.amount)


def get_order():
    print('-------Menu-------')
    print('1.Add Order')
    print('2.Delete Order')
    print('3.Edit Order')
    print('4.Display Order')
    print('5.Save Order')
    print('6.Exit the Program')
    print('')
    selections = int(input('Enter a number 1-5: '))
    return selections


def add_order():
    number = int(input('Enter Order number: '))
    order_type = input('Enter order type: ')
    amount = float(input('Enter amount: '))
    orders.append(OrderData(number, order_type, amount))
    return OrderData


def delete_order(x):
    y = int(input('Enter Order to be deleted: '))
    if y in orders:
        del orders[y]
    else:
        print(y, 'Order not found.')
    return x


def edit_order(x):
    edit = int(input('Enter the Order to edit: '))
    if edit in orders:
        new_number = int(input('Enter new Order number: '))
        new_type = input('Enter new Order type: ')
        new_amount = float(input('Enter new Order amount: '))
        orders[edit] = OrderData(new_number, new_type, new_amount)
    else:
        print(edit, 'Is not found in the Order list. ')
    return x


def display_orders(orders):
    if len(orders) == 0:
        print('There are no orders found')
    else:
        for x in orders.keys():
            orders[x].display_data()


def save_order(x):
    def write_list(a_list):
        with open('listfile', 'wb') as fp:
            pickle.dump(orders, fp)
            print('Saving...')
            print('Done')

    def read_list():
        with open('listfile', 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

    write_list(orders)
    r_orders = read_list()
    print('List is', r_orders)


while True:
    print("\n")
    selection = get_order()
    if selection == 1:
        add_order()
    elif selection == 2:
        delete_order()
    elif selection == 3:
        edit_order()
    elif selection == 4:
        display_orders(orders)
    elif selection == 5:
        save_order()
    elif selection == 6:
        print('Exiting program...')
        break
    else:
        print('Invalid entry. Try 1-4 or 5 to exit')
    print('Exiting loop')
