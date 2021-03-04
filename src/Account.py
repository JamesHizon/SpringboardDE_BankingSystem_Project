import json

from Service import Hizonhood, Loan, CreditCard


class Account:

    def __init__(self):
        """
        We will re-enter same values from Person into Account class.
        I cannot find an efficient way to transfer values from Person class at the moment.
        Also, this approach of entering data both in Account and Person class
        will also one person to fetch money from another person's account.
        - This satisfies the condition:
            1) What if one person trusts the other person such as a husband allowing his wife
            to make withdrawals from his account).
            2) What if one person has hired an investor to make solid investment decisions and has trusted the
            investor with his/her information.
        """
        self.balance = 0
        print("Welcome to James' Deposit & Withdrawal Machine!")
        # Edit: Place this into the Banking_system_test.py file.
        self.firstname = input("Enter first name: ")
        self.lastname = input("Enter last name: ")
        self.address = input("Enter address: ")
        self.name = self.firstname + self.lastname
        self.json_dict = {"Name": self.name, "Address": self.address, "Balance": self.balance}

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
        self.json_dict["Balance"] = self.balance
        return self.balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        self.json_dict["Balance"] = self.balance
        return self.balance

    def display(self):
        print("Available Balance: ", self.balance)

    def use_service(self):
        """
        Method: Requests for user input and returns a specified service as an instance of one of the different
        service classes.

        return: service as an object to be used
        """
        service_input = int(input("Select service:\n1 for Hizonhood\n2 for Credit Card\n3 for Loan"))
        if service_input == 1:
            investor_balance = float(input("Enter amount to deposit into Hizonhood: "))
            self.balance -= investor_balance
            self.json_dict["Balance"] = self.balance
            return Hizonhood(investor_balance)
        elif service_input == 2:
            name = input("Enter name: ")
            account_no = int(input("Enter account no: "))
            expiration_date = input("Enter expiration date: ")
            cvv = input("Enter cvv: ")
            balance = float(input("Enter balance: "))
            self.balance -= balance
            self.json_dict["Balance"] = self.balance
            return CreditCard(name, account_no, expiration_date, cvv, balance)
        elif service_input == 3:
            loan_amount = float(input("Enter loan amount: "))
            self.balance -= loan_amount
            self.json_dict["Balance"] = self.balance
            return Loan(loan_amount)


class CheckingAccount(Account):
    """
    Simple CheckingAccount class with method that withdraws based on fee amount and stores data into JSON file.
    """
    ca_fee = 1

    def withdrawal_fee(self, fee=ca_fee):
        """
        Method: Based on fee amount, will withdraw with fee subtracted from balance.
        """
        w_fee = super(CheckingAccount, self).withdraw() - fee
        super(CheckingAccount, self).json_dict["Balance"] = w_fee
        return w_fee

    def ca_to_json(self):
        """
        Method: Create a JSON file to store savings account data.
        """
        with open("checking_account_data.json", "w") as checking_act_file:
            json.dump(super(CheckingAccount, self).json_dict, checking_act_file)
        return "New JSON file created!"

    def ca_from_json(self):
        """
        Method: Read JSON file as dictionary object.
        """
        with open("checking_account_data.json", "r") as checking_act_file:
            ca_json_dict = json.load(checking_act_file)
        print("JSON file has been read!")
        return ca_json_dict


class SavingsAccount(Account):
    """
    Simple SavingsAccount class with method that checks the savings amount
    based on interest rate provided.
    """
    interest_rate = 0.1

    def check_savings(self, rate=interest_rate):
        """
        This method will check savings and be used to update JSON object inherited from the Account class.
        """
        savings = super(SavingsAccount, self).balance * rate
        super(SavingsAccount, self).json_dict["Savings"] = savings
        return savings

    def sa_to_json(self):
        """
        Method: Create a JSON file to store savings account data.
        """
        with open("savings_account_data.json", "w") as savings_act_file:
            json.dump(super(SavingsAccount, self).json_dict, savings_act_file)
        return "JSON File has been created!"

    def sa_from_json(self):
        """
        Method: Read JSON file as dictionary object.
        """
        with open("savings_account_data.json", "r") as savings_act_file:
            sa_json_dict = json.load(savings_act_file)
        print("JSON file has been read!")
        return sa_json_dict
