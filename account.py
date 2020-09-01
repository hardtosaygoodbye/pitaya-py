
import decimal
service_charge_rate = decimal.Decimal(0.005)

class Account:

    capital = decimal.Decimal(100000.0) 

    stock = decimal.Decimal(0.0)

    open_times = 0

    total_money_arr = []

    def __init__(self):
        pass

    def open(self, price):
        self.open_times = self.open_times + 1
        self.stock = self.stock + self.capital / (price * (1 + service_charge_rate))
        self.capital = decimal.Decimal(0.0)

    def close(self, price):
        self.capital = self.capital + self.stock * price
        self.stock = decimal.Decimal(0.0)

    def report(self, price):
        self.total_money_arr.append(float(self.capital + self.stock * price))

    def print_msg(self):
        print('capital:%2f'%(self.capital))
        print('stock:%2f'%(self.stock))