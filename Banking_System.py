# Banking System Project

# Task:
# - Create simple account class for a customer to use.

# Think:
# - I want to have my banking system such that each person can visit the bank and use a given service.
# - Typically, each person can go to their account to take money.

# Key Notes:
# - I created classes for all entities based on my original UML diagram, and tried to keep everything as simple as possible.
# - This is as simple as I could make it so far w/o overengineering it. I have not tested it, but the code does appear to be correctly written.
# - The Person class has a built-in method so that it can interact with different accounts and services.
# - I was originally able to create a git repository within Pycharm, but when I tried to commit changes inside Pycharm, it did not let me. Thus, I manually made changes on the Github website.

class Account:

    def __init__(self):
        self.balance = 0
        print("Welcome to James' Deposit & Withdrawal Machine!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return self.balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        return self.balance

    def display(self):
        print("\nAvailable Balance: ", self.balance)


# The following are child classes of BankAccount:

class CheckingAccount(Account):
    """
    Simple CheckingAccount class with method that withdraws based on fee amount.
    """
    ca_fee = 1

    def withdrawal_fee(self, fee=ca_fee):
        return super(CheckingAccount, self).withdraw() + fee


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

    # Create method to visit bank account
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

    # Create method to use a specified service
    def use_service(self):
        """
        Logic: Requests for user input and returns a specified service as an instance of one of the different
        service classes.
        """
        # Ask for which service to use?
        service_input = int(input("Select service:\n1 for Hizonhood\n2 for Credit Card\n3 for Loan"))
        if service_input == 1:
            service = Hizonhood()
        elif service_input == 2:
            service = CreditCard()
        elif service_input == 3:
            service = Loan()
        return service


class Customer(Person):

    # THINK: How to inherit all attributes from base/parent class,
    # while also adding additional attributes?
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

    # Initialize Service to be an empty list:
    def __init__(self, services_list=[]):
        self.services_list = services_list

    def display_all_services(self):
        return self.services_list


# I am trying to think about how to write code for each service:

class Hizonhood(Service):

    # Initialize empty investment portfolio as a list
    def __init__(self, services_list, investor_balance, investment_portfolio={}):
        Service.__init__(services_list)
        self.investor_balance = investor_balance
        self.investment_portfolio = investment_portfolio

    def invest(self, stock_ticker, amount):
        # Create dictionary
        if stock_ticker in self.investment_portfolio.keys():
            self.investment_portfolio[stock_ticker] += amount
        else:
            self.investment_portfolio[stock_ticker] = amount
        for key, value in self.investment_portfolio.items():
            return "${} has been invested into {}".format(round(value, 2), key)


class CreditCard(Service):

    def __init__(self, services_list, name, account_no, expiration_date, cvv, balance):
        Service.__init__(services_list)
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

    def __init__(self, services_list, loan_amount):
        Service.__init__(services_list)
        self.loan_amount = loan_amount

    def take_loan(self, customer_balance):
        customer_balance -= self.loan_amount
        return f"Loan of {self.loan_amount} has been taken!\nCustomer now has {round(customer_balance, 2)} left."


# Next:
# - How do we want to set up our classes s.t. we will store data into a database?

# Use SQLAlchemy:

# from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship
#
# Base = declarative_base()
#
#
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
# John_Smith.visit_bank()
# Select account type:
# Type 1 for checking account and 2 for savings account.>? 1
# Welcome to James' Deposit & Withdrawal Machine!
# <__main__.CheckingAccount object at 0x10b9b78e0>
# John_Smith.visit_bank()
# Select account type:
# Type 1 for checking account and 2 for savings account.>? 2
# Welcome to James' Deposit & Withdrawal Machine!
# <__main__.SavingsAccount object at 0x10b9b73a0>
