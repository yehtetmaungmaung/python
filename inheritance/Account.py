import random

class Account(object):
    num_accounts = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt
    
    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance

class EvilAccount(Account):
    def __init__(self, name, balance, evilfactor):
        super().__init__(name, balance)
        self.evilfactor = evilfactor

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * 1.10
        else:
            return self.balance
        
class MoreEvilAccount(EvilAccount):
    def deposit(self, amt):
        self.withdraw(5.00)
        super(MoreEvilAccount, self).deposit(amt)

class DepositCharge(object):
    fee = 5.00
    def deposit_fee(self):
        DepositCharge.withdraw(self.fee)

class WithdrawCharge(object):
    fee = 2.50
    def withdraw_fee(self):
        DepositCharge.withdraw(self.fee)

class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
    def deposit(self, amt):
        self.deposit_fee()
        super(MostEvilAccount, self).deposit(amt)

    def withdraw(self, amt):
        self.withdraw_fee()
        super(MostEvilAccount, self).withdraw(amt)

d = MostEvilAccount("Ye Htet", 500.00, 1.10)
d.deposit_fee()
