import json

from Account import CheckingAccount, SavingsAccount


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
                return CheckingAccount()
            else:
                checking_account_pin = input("Enter PIN Code: ")
                if self.json_dict["PIN"] == checking_account_pin:
                    return CheckingAccount()
                else:
                    print("Invalid PIN Code.")
        elif account_type_input == 2:
            if "PIN" not in self.json_dict.keys():
                print("You currently do not have a Savings Account.\n"
                      "A new savings account will be created automatically for you.\n")
                savings_account_pin_setup = input("Set up PIN Code: ")
                self.json_dict["PIN"] = savings_account_pin_setup
                return SavingsAccount(Person.firstname, Person.lastname, Person.address)
            else:
                savings_account_pin = input("Enter PIN Code: ")
                if self.json_dict["PIN"] == savings_account_pin:
                    return SavingsAccount(Person.firstname, Person.lastname, Person.address)
                else:
                    print("Invalid PIN Code.")

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
        self.json_dict = {"Name": self.firstname + self.lastname,
                          "Address": self.address,
                          "Cash": self.cash_available,
                          "Accounts": self.accounts_available}

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
            more_input = input("Would you like to add more input?\nType 'Y' for Yes and 'N' for No.")
        self.accounts_available = accounts_list
        # List to dict
        self.json_dict["Accounts"] = accounts_list
        return "Customer accounts set!"

    def customer_to_json(self):
        """
        Note that the we use super class to inherit the json_dict attribute from Accounts
        to dump data into customer_file as our object.
        """
        with open("customer_data.json", "w") as customer_file:
            json.dump(self.json_dict, customer_file)
        return "New JSON file created!"

    def customer_from_json(self):
        with open("customer_data.json", "r") as customer_file:
            data = json.load(customer_file)
        print("JSON file has been read!")
        return data


class Employee(Person):

    def __init__(self, firstname, lastname, address, cash_available, salary=0):
        Person.__init__(self, firstname, lastname, address, cash_available)
        self.salary = salary
        self.json_dict = {"Name": self.firstname + self.lastname,
                          "Address": self.address,
                          "Cash Available": self.cash_available,
                          "Salary": salary}

    def increase_salary(self):
        increase_amount = float(input("Enter salary amount for increasing: "))
        self.salary += increase_amount
        self.json_dict["Salary"] = self.salary
        return "New salary: {}".format(self.salary)

    def employee_to_json(self):
        with open("employee_data.json", "w") as employee_file:
            json.dump(self.json_dict, employee_file)
        return "New JSON file created!"

    def employee_from_json(self):
        with open("employee_data.json", "r") as employee_file:
            data = json.load(employee_file)
        print("JSON file has been read!")
        return data
