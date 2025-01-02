from Checkings import Checkings

class Transactions(Checkings):
    def __init__(self, name, acc_num, exp_date, cv, acc_type):
        super().__init__(name, acc_num, exp_date, cv, acc_type)

    def add_transaction(self, transaction):
    # Save transaction information to the file
    # You can use the same approach described in the previous response
        pass

def lookup_transactions(self, date):
    # Look up transactions based on the provided date
    # Retrieve and return transactions for that date from self.transactions
        pass