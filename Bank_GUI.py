"""
    GUI Application of a pseudo bank. It allows the user to create a bank account and access it to deposit, withdraw or transfer money.
    Every transaction in the app are stored in a file, transaction.txt, and all bank accounts saved on the accounts.txt file.
"""
from tkinter import *
from tkinter import messagebox


class Bank_GUI:
    def __init__(self):

        """

            This is the first window of the application. Allows the user to choose to login in the app or create a new bank account
            in case no account for that user is registered.

        """

        # Create the menu window
        self.withdraw_amount_lbl = None
        self.withdraw_window = None
        self.amount_entry = None
        self.amount_lbl = None
        self.deposit_window = None
        self.balance_entry = None
        self.balance_lbl = None
        self.transfer_bttn = None
        self.withdraw_bttn = None
        self.main_window = None
        self.create_savings_window = None
        self.create_acc_bttn = None
        self.birthdate_entry = None
        self.name_entry = None
        self.name_lbl = None
        self.birthdate_lbl = None
        self.withdraw_amount_entry = None
        self.w_cancel_bttn = None
        self.create_checkings_window = None
        self.close_window_bttn = None
        self.savings_bttn = None
        self.checkings_bttn = None
        self.create_acc_window = None
        self.close_bttn = None
        self.password_label = None
        self.acc_entry = None
        self.login_window = None
        self.cancel_bttn = None
        self.confirm_bttn = None
        self.password_entry = None
        self.password_lbl = None
        self.username_entry = None
        self.create_login_window = None
        self.menu_window = Tk()
        self.menu_window.title("Main Menu")

        # Size of the window
        self.menu_window.geometry("500x500+200+200")

        # Button to allow the user to login or open a new account in the application
        Button(self.menu_window, text="Login", command=self.open_login_window).pack()
        Button(self.menu_window, text=" Open new account", command=self.create_login).pack()

        # Button to exit the application
        Button(self.menu_window, text="Close", command=self.close_app).pack()

        # Start with the window event loop
        self.menu_window.mainloop()

    def create_login(self):

        self.create_login_window = Toplevel(self.menu_window)
        self.create_login_window.title("Create Account")
        self.create_login_window.geometry("500x500+200+200")

        Label(self.create_login_window, text="Enter username for login").pack()
        self.username_entry = Entry(self.create_login_window, width=20)
        self.username_entry.pack()

        Label(self.create_login_window,
              text="Enter passcode for login. It must be 4 digits.").pack()
        self.password_entry = Entry(self.create_login_window, width=20)
        self.password_entry.pack()

        def close():
            """
                Method to close the create_savigs_window
            """
            self.create_login_window.destroy()

        self.confirm_bttn = Button(self.create_login_window, text="Confirm", command=self.validate_password)
        self.confirm_bttn.pack()
        self.cancel_bttn = Button(self.create_login_window, text="Cancel", command=close)
        self.cancel_bttn.pack()

    def validate_password(self):
        username = self.username_entry.get()
        passcode = self.password_entry.get()

        if passcode.isnumeric() and len(passcode) == 4:
            messagebox.showinfo(title="Confirmation", message="Account created with success.")
            self.create_login_window.destroy()
            self.open_create_acc_window()
        else:
            messagebox.showerror(title="ERROR", message="You must enter a 4 digit passcode")

    def open_login_window(self):

        """
            open_login_window method opens and configure a new window to allow the user to log in the application.

        """

        self.login_window = Toplevel(self.menu_window)
        self.login_window.title("Login")
        self.login_window.geometry("500x500+200+200")

        # Widgets for the account number
        Label(self.login_window, text="Account number").pack()
        Entry(self.login_window, width=20).pack()

        # Widgets for the password
        Label(self.login_window, text="Password").pack()
        Entry(self.login_window, width=20).pack()

        def close():
            """
                Close this window
            """
            self.login_window.destroy()
            self.login_window.update()

        def check_login():
            """
                This check if the information entered is correct and call the main_menu window
            """
            self.main_menu()
            close()

        # Close and confirm button widgets
        Button(self.login_window, text="Close", command=close).pack()
        Button(self.login_window, text="Confirm", command=check_login).pack()

    def open_create_acc_window(self):

        """
            This method open and configures a new window to display the two options for account creation:
                Checkings account
                Savings account
        """

        # Configure the window
        self.create_acc_window = Toplevel(self.menu_window)
        self.create_acc_window.title("Create new account")
        self.create_acc_window.geometry("500x500+200+200")

        # Button widgets
        Button(self.create_acc_window, text="Checkings Account",
               command=self.open_checkings_acc).pack()
        Button(self.create_acc_window, text="Savings Account", command=self.open_savings_acc).pack()

        def close():
            """
                Method to close the create_acc_window
            """
            self.create_acc_window.destroy()
            self.create_acc_window.update()

        # Close button
        Button(self.create_acc_window, text="Close", command=close).pack()

    def open_checkings_acc(self):

        """
            Open and configure create_checkings_window that allows the user to create a checkings account.
        """
        # Configure the window
        self.create_checkings_window = Toplevel(self.menu_window)
        self.create_checkings_window.title("Create Checkings Account")
        self.create_checkings_window.geometry("500x500+200+200")

        # Widgets to create a card
        Label(self.create_checkings_window, text="Enter your legal name").pack()
        Entry(self.create_checkings_window, width=20).pack()
        Label(self.create_checkings_window, text="Enter your date of birth").pack()
        Entry(self.create_checkings_window, width=20).pack()

        def close():
            """
                Method that closes the create_checkings_window
            """
            self.create_checkings_window.destroy()
            self.create_checkings_window.update()

        # Widgets to create the account and close the window
        Button(self.create_checkings_window, text="Close", command=close).pack()
        Button(self.create_checkings_window, text="Create Account",
               command=self.create_checkings_acc).pack()

    def open_savings_acc(self):
        """
            This method open and configure the create_savings_window and allow the user to create a savings account
        """
        # Configure the window
        self.create_savings_window = Toplevel(self.menu_window)
        self.create_savings_window.title("Create Savings Account")
        self.create_savings_window.geometry("500x500+200+200")

        # Widgets to create the account
        Label(self.create_savings_window, text="Enter your legal name").pack()
        Entry(self.create_savings_window, width=20).pack()
        Label(self.create_savings_window, text="Enter your date of birth").pack()
        Entry(self.create_savings_window, width=20).pack()

        def close():
            """
                Method to close the create_savigs_window
            """
            self.create_savings_window.destroy()
            self.create_savings_window.update()

        # Widgets to create the savings account and close the window
        Button(self.create_savings_window, text="Close", command=close).pack()
        Button(self.create_savings_window, text="Create Account",
               command=self.create_savings_acc).pack()

    def main_menu(self):

        """
            This method controls the transactions and main functions of the application.
                Here the user can deposit money in his account
                Withdraw money of the account
                Transfer money between accounts
                See the current balance of the user account
        """

        # Configure window
        self.main_window = Toplevel(self.menu_window)
        self.main_window.title("Account Menu")
        self.main_window.geometry("500x500+200+200")

        # Widgets button
        Button(self.main_window, text="Deposit Money", command=self.deposit).pack()
        Button(self.main_window, text="Withdraw Money", command=self.withdraw).pack()
        Button(self.main_window, text="Transfer money", command=self.transfer).pack()

        # Widget to show the balance
        Label(self.main_window, text="Balance").pack()
        self.balance_entry = Entry(self.main_window, width=20, cursor="left_ptr")
        self.balance_entry.configure(state=DISABLED)
        self.balance_entry.pack()

    def deposit(self):

        """
            Method to deposit money into the account
        """

        # Configure window
        self.deposit_window = Toplevel(self.menu_window)
        self.deposit_window.title("Deposit Menu")
        self.deposit_window.geometry("200x250+200+300")

        Label(self.deposit_window, text="Enter the deposit amount").pack()
        self.amount_entry = Entry(self.deposit_window, width=20)

        def confirm():
            confirmation_msg = f"Would you like to deposit {self.amount_entry.get()} into the account?"

            answer = messagebox.askyesno("Deposit confirmation", confirmation_msg)
            if answer == "yes":
                self.balance_entry.configure(state=NORMAL)
                self.balance_entry.insert(0, self.amount_entry.get())
                self.balance_entry.configure(state=DISABLED)

        def close():
            self.deposit_window.destroy()
            self.deposit_window.update()

        Button(self.deposit_window, text="Confirm", command=confirm).pack()
        Button(self.deposit_window, text="cancel", command=close).pack()
        self.amount_entry.pack()

    def withdraw(self):

        """
            Method to withdraw money from the account
        """

        # Configure window
        self.withdraw_window = Toplevel(self.menu_window)
        self.withdraw_window.title("withdraw Menu")
        self.withdraw_window.geometry("200x250+200+300")

        Label(self.withdraw_window, text="Enter the withdraw amount").pack()
        self.withdraw_amount_entry = Entry(self.withdraw_window, width=20)

        def confirm():
            confirmation_msg = f"Would you like to withdraw {self.withdraw_amount_entry.get()} into the account?"

            answer = messagebox.askyesno("Deposit confirmation", confirmation_msg)
            if answer == "yes":
                self.balance_entry.configure(state=NORMAL)
                self.balance_entry.insert(0, self.amount_entry.get())
                self.balance_entry.configure(state=DISABLED)

        def close():
            self.withdraw_window.destroy()
            self.withdraw_window.update()

        self.withdraw_amount_entry.pack()
        Button(self.withdraw_window, text="Confirm", command=confirm).pack()
        Button(self.withdraw_window, text="cancel", command=close).pack()

    def transfer(self):
        pass

    def create_checkings_acc(self):
        pass

    def create_savings_acc(self):
        pass

    def close_app(self):
        self.menu_window.destroy()


if __name__ == "__main__":
    Bank_GUI()
