# Banking System Project

import json


class Account:

    def __init__(self):
        self.balance = 0
        print("Welcome to James' Deposit & Withdrawal Machine!")
        self.firstname = input("Enter first name: ")
        self.lastname = input("Enter last name: ")
        self.name = self.firstname + self.lastname
        self.address = input("Enter address: ")
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
            service = Hizonhood(investor_balance)
        elif service_input == 2:
            name = input("Enter name: ")
            account_no = int(input("Enter account no: "))
            expiration_date = input("Enter expiration date: ")
            cvv = input("Enter cvv: ")
            balance = float(input("Enter balance: "))
            self.balance -= balance
            self.json_dict["Balance"] = self.balance
            service = CreditCard(name, account_no, expiration_date, cvv, balance)
        elif service_input == 3:
            loan_amount = float(input("Enter loan amount: "))
            self.balance -= loan_amount
            self.json_dict["Balance"] = self.balance
            service = Loan(loan_amount)
        return service


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


class Person:

    def __init__(self, firstname, lastname, address, cash_available):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.cash_available = cash_available
        self.json_dict = {"Name": self.firstname + self.lastname,
                          "Address": self.address,
                          "Cash": self.cash_available}

    def visit_bank(self):
        """
        Method: Will request for account type and PIN code setup for registering or login.
        """

        account_type_input = int(input("Select account type:\nType 1 for checking account and 2 for savings account."))
        if account_type_input == 1:
            if "PIN" not in self.json_dict.keys():
                print("You currently do not have a Checking Account.\n"
                      "A new checking account will be created automatically for you.\n")
                checking_account_pin_setup = input("Set up PIN Code: ")
                self.json_dict["PIN"] = checking_account_pin_setup
                account = CheckingAccount()
            else:
                checking_account_pin = input("Enter PIN Code: ")
                if self.json_dict["PIN"] == checking_account_pin:
                    account = CheckingAccount()
                else:
                    print("Invalid PIN Code.")
        elif account_type_input == 2:
            if "PIN" not in self.json_dict.keys():
                print("You currently do not have a Savings Account.\n"
                      "A new savings account will be created automatically for you.\n")
                savings_account_pin_setup = input("Set up PIN Code: ")
                self.json_dict["PIN"] = savings_account_pin_setup
                account = SavingsAccount()
            else:
                savings_account_pin = input("Enter PIN Code: ")
                if self.json_dict["PIN"] == savings_account_pin:
                    account = SavingsAccount()
                else:
                    print("Invalid PIN Code.")
        return account

    def set_cash_available(self, new_cash_amount):
        self.cash_available = new_cash_amount
        self.json_dict["Cash"] = self.cash_available
        return self.cash_available


class Customer(Person):
    """
    We want to basically have this customer table work s.t. each time a customer logs into the bank account,
    it will request a PIN code or some unique identifier.
    """

    def __init__(self, firstname, lastname, address, cash_available, accounts_available=None):
        Person.__init__(self, firstname, lastname, address, cash_available)
        self.accounts_available = accounts_available

    def get_customer_accounts(self):
        if self.accounts_available is None:
            print("None")
        else:
            for act in self.accounts_available:
                print("Customer accounts:", act)

    def set_customer_accounts(self):
        """
        Simple set_customer_accounts method that asks for user input
        and returns a list of accounts after asking.
        :return: List of user accounts
        """
        accounts_list = []
        act_input = input("Enter user account: ")
        accounts_list.append(act_input)
        more_input = input("Would you like to add more input?\nType 'Y' for Yes and 'N' for No.")
        while more_input == 'Y':
            act_input = input("Enter user account: ")
            accounts_list.append(act_input)
        self.accounts_available = accounts_list
        # List to dict
        super(Customer, self).json_dict["Accounts"] = accounts_list
        return "Customer accounts set!"

    def customer_to_json(self):
        """
        Note that the we use super class to inherit the json_dict attribute from Accounts
        to dump data into customer_file as our object.
        """
        with open("customer_data.json", "w") as customer_file:
            json.dump(super(Customer, self).json_dict, customer_file)
        return "New JSON file created!"

    def customer_from_json(self):
        with open("customer_data.json", "r") as customer_file:
            data = json.load(customer_file)
        print("JSON file has been read!")
        return data


class Employee(Person):

    def __init__(self, firstname, lastname, address, cash_available, salary=0):
        Person.__init__(firstname, lastname, address, cash_available)
        self.salary = salary
        super(Employee, self).json_dict["Salary"] = self.salary

    def increase_salary(self):
        increase_amount = float(input("Enter salary amount for increasing: "))
        self.salary += increase_amount
        super(Employee, self).json_dict["Salary"] = self.salary
        return "New salary: {}".format(self.salary)

    def employee_to_json(self):
        with open("employee_data.json", "w") as employee_file:
            json.dump(super(Employee, self).json_dict, employee_file)
        return "New JSON file created!"

    def employee_from_json(self):
        with open("employee_data.json", "r") as employee_file:
            data = json.load(employee_file)
        print("JSON file has been read!")
        return data


class Service:

    def __init__(self):
        self.services_list = "Hizonhood\nLoan\nCreditCard"

    def display_all_services(self):
        # Print upcoming services to be available
        print("Upcoming services available soon: Webull\nTD Ameritrade\nVenmo\nPayPal")
        return "Available services: ".format(self.services_list)


class Hizonhood(Service):
    """
    Simple Investment Portfolio service class which will track how much money is invested
    (will not record gains or losses, however, for the sake of simplicity.)
    """
    def __init__(self, investor_balance):
        self.name = input("Enter Investor name: ")
        self.investor_balance = investor_balance
        self.investment_portfolio = {}
        self.json_dict = {"Investor Name": self.name,
                          "Investor Balance": self.investor_balance,
                          "Investor Portfolio": self.investment_portfolio}

    def invest(self, stock_ticker, amount):
        self.investor_balance -= amount
        self.json_dict["Investor Balance"] = self.investor_balance
        if stock_ticker in self.investment_portfolio.keys():
            self.investment_portfolio[stock_ticker] += amount
            self.json_dict["Investor Portfolio"] = self.investment_portfolio
        else:
            self.investment_portfolio[stock_ticker] = amount
            self.json_dict["Investor Portfolio"] = self.investment_portfolio
        for key, value in self.investment_portfolio.items():
            print("${}0 has been invested into {}".format(float(value), key))

    def hizon_to_json(self):
        """
        Using dictionary, we want to dump the data into a JSON object.
        """
        with open("investment_data_file.json", "w") as write_file:
            json.dump(self.json_dict, write_file)
        return "New JSON file created!"

    def hizon_from_json(self):
        """
        Retrieve JSON file and set to self.investment_portfolio.
        """
        with open("investment_data_file.json", "r") as read_file:
            self.json_dict = json.load(read_file)
        return "JSON file has been read!"


class CreditCard(Service):

    def __init__(self, name, account_no, expiration_date, cvv, balance):
        self.name = name
        self.account_no = account_no
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.balance = balance
        self.json_dict = {"Name": self.name,
                          "Account": self.account_no,
                          "Expiration Date": self.expiration_date,
                          "CVV": self.cvv,
                          "Balance": self.balance}

    def make_purchase(self, purchase_amount):
        if purchase_amount > self.balance:
            print("Insufficient amount on card.")
        else:
            self.balance -= purchase_amount
            self.json_dict["Balance"] = self.balance
            return "Purchase has been made."

    def credit_to_json(self):
        with open("credit_card_data.json", "w") as credit_card_file:
            json.dump(self.json_dict, credit_card_file)
        return "New JSON file created!"

    def credit_from_json(self):
        with open("credit_card_data.json", "r") as credit_card_file:
            data = json.load(credit_card_file)
        print("JSON file has been loaded!")
        return data


class Loan(Service):

    def __init__(self, loan_amount, consumer_name):
        self.name = consumer_name
        self.loan_amount = loan_amount
        self.json_dict = {"Name": self.name, "Loan Amount": self.loan_amount}

    def take_loan(self, customer_balance):
        customer_balance -= self.loan_amount
        return f"Loan of {self.loan_amount} has been taken!\nCustomer now has {round(customer_balance, 2)} left."

# Driver Code

# John_Smith = Customer("John", "Smith", "100 ABC Street", 100, "CheckingAccount")
# bank_visit = John_Smith.visit_bank()
# bank_visit.deposit()
# use_hizonhood = bank_visit.use_service()
# use_hizonhood.invest("DOGE", 20)
# use_hizonhood.invest("BTC", 40)
# use_hizonhood.hizon_to_json()