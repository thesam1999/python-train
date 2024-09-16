class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        # 代表一創建物件，就會執行上面的print

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):  # self.balance的值會在這裡被更新
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${
                    self.balance:.2f}"
            )
        # 引發異常會中斷當前的程式執行流程，如果沒有try跟except捕捉這個異常，會中止程式

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)  # 使用同個類的方法要加self
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:  # 用except因為發生異常時會捕捉異常並處理，給用戶友好的提示，而不讓程式崩潰。
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):  # 直接替代deposit這個方法
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
