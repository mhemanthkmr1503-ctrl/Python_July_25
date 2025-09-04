class Bank:
    __balance = 1000

    def __getBalance(self):
        print(self.__balance)

    def hello(self):
        self.__getBalance()

account_holder = Bank()
account_holder.hello()