from Customer import Customer

class Savings(Customer):
    """
        Savings class that allows the user to see their balance, deposit money on the account,
        withdraw money off the account, and calculate the interest rate. It is a subclass of Customer.
    """

    def __init__(self, name, acc_num, exp_date, cv, acc_type, balance=0.0, interest_rate=0.0):
        """
        Constructor class that have as arguments:
            name : String --> Customer name
            acc_num : String --> Bank Account number
            exp_date : String --> Account expire date
            cv : String --> Security code
            acc_type : String --> Account type
            balance: Float -> Represents user's balance
            interest_rate: Float -> Represents the interest rate an account has
        """

        # Call the superclass __init__ method and pass the required arguments.
        Customer.__init__(self, name, acc_num, exp_date, cv, acc_type)

        self.__balance = balance
        self.__interest_rate = interest_rate

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

    # Calculates the interest rate on an account in a specific amount of time and update the balance
    def calc_interest(self, time):
        interest = self.__balance * self.__interest_rate * time
        self.__balance += interest
        return interest

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

    def __str__(self) -> str:
        ''' String representation of the object '''
        display_str = Customer.acc_num + f"Balance: ${self.__balance}\nInterest rate: {self.__interest_rate * 100:.1f}%"

        return display_str