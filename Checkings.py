from Customer import Customer

class Checkings(Customer):
    """
    Checkings class that allows the user to see their balance, deposit money on the account,
    withdraw money off the account. It is a subclass of Customer.
    """

    def __init__(self, name, acc_num, exp_date, cv, acc_type, balance=0.0):
        '''
            Constructor class that have as arguments:
                name : String --> Customer name
                acc_num : String --> Bank Account number
                exp_date : String --> Account expire date
                cv : String --> Security code
                acc_type : String --> Account type
                balance: Float -> Represents user's balance
        '''

        # Call the superclass __init__ method and pass the required arguments.
        Customer.__init__(self, name, acc_num, exp_date, cv, acc_type)

        self.__balance = balance
        # Dictionary to store checking account (acc_num : [list of information])
        self.__checkings_acc = {}
        # Dictionary to store transactions (date: [list of transactions])
        self.__transaction = {}

    # Allow the user to add money to an account
    def deposit(self, amount):
        self.__balance += amount

    # Allow user to withdraw money to an account
    def withdraw(self, amount):
        if self.__balance <= 0:
            print("Sorry, you do not have enough funds in the account to withdraw.")
        else:
            self.__balance -= amount

    # Allows the user to transfer money between accounts if the account has enough funds
    def transfer(self, recipient, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            recipient.deposit(amount)
            print("Transfer completed.")
        else:
            print("Sorry, you do not have enough funds in the account to complete this transfer.")

            # Display the balance

    def get_balance(self):
        return self.__balance

    # Display the bank account information
    def __str__(self) -> str:
        display_str = Customer.acc_num + f"Balance: ${self.__balance}"
        return display_str