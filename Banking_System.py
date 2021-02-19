# Banking System Project

import json


class Account:

    def __init__(self):
        self.balance = 0
        print("Welcome to James' Deposit & Withdrawal Machine!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
        return self.balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        return self.balance

    def display(self):
        print("Available Balance: ", self.balance)

    def use_service(self):
        """
        Logic: Requests for user input and returns a specified service as an instance of one of the different
        service classes.

        Note:
        - It may not be as high quality, but we just want a simple working solution.

        return: service as an object to be used
        """
        # Ask for which service to use?
        service_input = int(input("Select service:\n1 for Hizonhood\n2 for Credit Card\n3 for Loan"))
        if service_input == 1:
            # Request investor_balance/deposit money from account to service:
            investor_balance = float(input("Enter amount to deposit into Hizonhood: "))
            self.balance -= investor_balance
            service = Hizonhood(investor_balance)
        elif service_input == 2:
            # Request info:
            name = input("Enter name: ")
            account_no = int(input("Enter account no: "))
            expiration_date = input("Enter expiration date: ")
            cvv = input("Enter cvv: ")
            balance = float(input("Enter balance: "))
            self.balance -= balance
            service = CreditCard(name, account_no, expiration_date, cvv, balance)
        elif service_input == 3:
            # Request loan amount:
            loan_amount = float(input("Enter loan amount: "))
            self.balance -= loan_amount
            service = Loan(loan_amount)
        return service


class CheckingAccount(Account):
    """
    Simple CheckingAccount class with method that withdraws based on fee amount.
    """
    ca_fee = 1

    def withdrawal_fee(self, fee=ca_fee):
        return super(CheckingAccount, self).withdraw() - fee


class SavingsAccount(Account):
    """
    Simple SavingsAccount class with method that checks the savings amount
    based on interest rate provided.
    """
    interest_rate = 0.1

    def check_savings(self, rate=interest_rate):
        return super(SavingsAccount, self).balance * rate


class Person:

    def __init__(self, firstname, lastname, address, cash_available):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.cash_available = cash_available

    def visit_bank(self):
        """
        Want to ask whether person wants to use a checking or a savings account.
        Logic: Based on user input, visit bank to use either a checking or savings account.
        """
        account_type_input = int(input("Select account type:\nType 1 for checking account and 2 for savings account."))
        if account_type_input == 1:
            account = CheckingAccount()
        elif account_type_input == 2:
            account = SavingsAccount()
        return account


class Customer(Person):
    """
    Customer class will inherit from Person and Base class.
    The Base class will be used to drive the SQLAlchemy data storage solution and create a
    Customer table.

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
        # Initialize empty account list:
        accounts_list = []
        # Ask for user input:
        act_input = input("Enter user account: ")
        accounts_list.append(act_input)
        # Request for more:
        more_input = input("Would you like to add more input?\nType 'Y' for Yes and 'N' for no.")
        while more_input == 'Y':
            act_input = input("Enter user account: ")
            accounts_list.append(act_input)
        self.accounts_available = accounts_list
        return "Customer accounts set!"


# Next: Create visit_bank and user_service methods, along with creating the CreditCard and Loan classes.
# - Maybe... we should simply create the other classes first.
class Employee(Person):

    def __init__(self, firstname, lastname, address, cash_available, salary=0):
        Person.__init__(firstname, lastname, address, cash_available)
        self.salary = salary

    def increase_salary(self):
        increase_amount = float(input("Enter salary amount for increasing: "))
        self.salary += increase_amount
        return "New salary: {}".format(self.salary)


# Three services: CreditCard, Loan, and Hizonhood (Remake of Robinhood).

class Service:

    def __init__(self):
        self.services_list = "Hizonhood\nLoan\nCreditCard"

    def display_all_services(self):
        # Print upcoming services to be available
        print("Upcoming services available soon: Webull\nTD Ameritrade\nVenmo\nPayPal")
        return "Coming Soon: ".format(self.services_list)


# I am trying to think about how to write code for each service:
class Hizonhood(Service):
    # Initialize empty investment portfolio as a dictionary
    def __init__(self, investor_balance):
        self.investor_balance = investor_balance
        self.investment_portfolio = {}

    def invest(self, stock_ticker, amount):
        # Subtract from investor balance
        self.investor_balance -= amount
        # Create dictionary
        if stock_ticker in self.investment_portfolio.keys():
            self.investment_portfolio[stock_ticker] += amount
        else:
            self.investment_portfolio[stock_ticker] = amount
        for key, value in self.investment_portfolio.items():
            print("${}0 has been invested into {}".format(float(value), key))

    def to_json(self):
        """
        Using dictionary, we want to dump the data into a JSON object.
        """
        with open("investment_data_file.json", "w") as write_file:
            json.dump(self.investment_portfolio, write_file)
        return "New JSON file created!"


class CreditCard(Service):

    def __init__(self, name, account_no, expiration_date, cvv, balance):
        self.name = name
        self.account_no = account_no
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.balance = balance

    def make_purchase(self, purchase_amount):
        if purchase_amount > self.balance:
            print("Insufficient amount on card.")
        else:
            self.balance -= purchase_amount
            return "Purchase has been made."


class Loan(Service):
    def __init__(self, loan_amount):
        self.loan_amount = loan_amount

    def take_loan(self, customer_balance):
        customer_balance -= self.loan_amount
        return f"Loan of {self.loan_amount} has been taken!\nCustomer now has {round(customer_balance, 2)} left."

# Next:
# - How do we want to set up our classes s.t. we will store data into a database?


# class Customer(Base):
#     __tablename__ = "Customer"
#
#     id = Column('id', Integer, primary_key=True)
#     FirstName = Column('FirstName', String, unique=True)
#     LastName = Column('LastName', String, unique=True)
#     Address = Column('Address', String, unique=True)
#     CheckingAccountAvailable = Column('CheckingAccountAvailable', String, unique=True)
#     SavingsAccountAvailable = Column('SavingsAccountAvailable', String, unique=True)
#
#
# class Employee(Base):
#     __tablename__ = "Employee"
#
#     id = Column('id', Integer, primary_key=True)
#     FirstName = Column('FirstName', String, unique=True)
#     LastName = Column('LastName', String, unique=True)
#     Address = Column('Address', String, unique=True)
#     Salary = Column('Salary', String, unique=True)
#
#
# class CheckingAccount(Base):
#     __tablename__ = "CheckingAccount"
#
#     id = Column('id', Integer, primary_key=True)
#     PersonId = Column('PersonId', Integer, foreign_key=True)
#     FirstName = Column('FirstName', String, unique=True)
#     LastName = Column('LastName', String, unique=True)
#     Balance = Column('Balance', Float, unique=True)
#
#
# class SavingsAccount(Base):
#     __tablename__ = "SavingsAccount"
#
#     id = Column('id', Integer, primary_key=True)
#     PersonId = Column('PersonId', Integer, foreign_key=True)
#     FirstName = Column('FirstName', String, unique=True)
#     LastName = Column('LastName', String, unique=True)
#     Balance = Column('Balance', Float, unique=True)
#
#
# engine = create_engine('sqlite:///:memory:', echo=True) # use sqlite to run in-memory
# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)
#
# session = Session()
#
# session.close()

# Driver Code

# John_Smith = Customer("John", "Smith", "100 ABC Street", 100, "CheckingAccount")
# John_Smith.firstname
# 'John'
# John_Smith.lastname
# 'Smith'
# bank_visit = John_Smith.visit_bank()
# Select account type:
# Type 1 for checking account and 2 for savings account.>? 1
# Welcome to James' Deposit & Withdrawal Machine!
# <__main__.CheckingAccount object at 0x10b9b78e0>
# John_Smith.visit_bank()
# Select account type:
# Type 1 for checking account and 2 for savings account.>? 2
# Welcome to James' Deposit & Withdrawal Machine!
# <__main__.SavingsAccount object at 0x10b9b73a0>

# bank_visit.deposit()
# 100
# use_hizonhood = bank_visit.use_service()
# 1
# 80
# use_hizonhood.invest("DOGE", 20)
# use_hizonhood.invest("GOD", 40)
# use_hizonhood.to_json()
