# After running Account.py, Person.py and Service.py files,
# we will run this code to test if it works.

# The following is our main files (base classes) to be imported:

import Account
import Person
import Service

# In order to work with driver (test) code, we also need to import the child classes associated with the base class.

from Account import CheckingAccount, SavingsAccount
from Person import Customer, Employee
from Service import Hizonhood, Loan, CreditCard

# Driver Code

if __name__ == '__main__':
    # Request user input:
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + last_name
    address = input("Enter address: ")
    # Request Person type:
    person_type = int(input("Are you a Customer or an Employee?\n"
                            "Enter 1 for 'Customer'\n"
                            "Enter 2 for 'Employee'\n"))
    # Create Person object
    if person_type == 1:
        # Customer actions
        person = Customer(first_name, last_name, address, 0)
        cash_input = input("Currently, you have no cash available.\n"
                           "Enter 'Y' if this is the case.\n"
                           "Otherwise, enter new cash amount: ")
        if cash_input != 'Y':
            person.set_cash_available(cash_input)
        # Getter, setter and JSON methods
        customer_req = int(input("Would you like to get or set customer accounts?\n"
                                 "Enter 1 to get customer accounts\n"
                                 "Enter 2 to set customer accounts\n"
                                 "Enter 3 to extract customer data from JSON file (if exists)\n"
                                 "Enter 4 to perform none of the listed actions: \n"))
        if customer_req == 1:
            person.get_customer_accounts()
        elif customer_req == 2:
            # Save data to JSON after setting customer account info
            person.set_customer_accounts()
            person.customer_to_json()
        elif customer_req == 3:
            try:
                person.customer_from_json()  # may need try/except clause
            except ValueError:
                print("No JSON file found.")
        elif customer_req == 4:
            print("Did not perform an action.")
    elif person_type == 2:
        # Employee actions
        cash_input = input("Currently, you have no cash available.\n"
                           "Enter 'Y' if this is the case.\n"
                           "Otherwise, enter new cash amount: ")
        salary_input = int(input("Enter current salary: "))
        # Create Employee object to perform actions
        person = Employee(first_name, last_name, address, cash_input, salary_input)
        if cash_input != 'Y':
            cash_input = int(cash_input)
            person.set_cash_available(cash_input)
        # Salary and JSON file requests
        employee_req = int(input("Enter 1 to increase salary\n"
                                 "Enter 2 to request employee data from JSON (if exists)\n"
                                 "Enter 3 to perform no action: "))
        if employee_req == 1:
            person.increase_salary()
            person.employee_to_json()  # Save file in JSON format
        elif employee_req == 2:
            try:
                person.employee_from_json()  # May need try/except clause
            except ValueError:
                print("No JSON file found.")
        elif employee_req == 3:
            print("Did not perform action.")

    # Ask to visit bank (prior to using service). (Think of recursive calls/work with while loops.)
    visit_bank_req = input("Would you like to visit the bank?\n"
                           "Enter 'Y' for Yes and 'N' for No: ")
    if visit_bank_req == 'Y':
        active_person = person.visit_bank()
        print("Person has chosen to visit the bank!")
        # Request user action (build on active_person object):
        action_req = int(input("Enter number for specified action:\n"
                               "Enter 1 to withdraw\n"
                               "Enter 2 to deposit\n"
                               "Enter 3 to display current balance: "))
        if action_req == 1:
            active_person.withdraw()
        elif action_req == 2:
            active_person.deposit()
        elif action_req == 3:
            active_person.display()
        # Ask user to perform more actions:
        more_action_req = input("Would you like to perform another action?\n"
                                "Enter 'Y' for another action and "
                                "'N' to stop using the banking system: ")
        while more_action_req == 'Y':
            # Request user action (build on active_person object):
            action_req2 = int(input("Enter number for specified action:\n"
                                    "Enter 1 to withdraw\n"
                                    "Enter 2 to deposit\n"
                                    "Enter 3 to display balance\n"
                                    "Enter 4 to use a service: "))
            if action_req2 == 1:
                active_person.withdraw()
            elif action_req2 == 2:
                active_person.deposit()
            elif action_req2 == 3:
                active_person.display()
            elif action_req2 == 4:
                service = active_person.use_service()
                # Service Actions
                more_service_req = input("Would you like to perform any additional service requests?\n"
                                         "Enter 'Y' for Yes and 'N' to stop using services: ")
                while more_service_req == 'Y':
                    # Hizonhood: Invest, Extract data from JSON
                    hizonhood_actions = input("Would you like to invest using Hizonhood?\n"
                                              "Type 'Y' for Yes and 'N' for No: ")
                    if hizonhood_actions == 'Y':
                        print("Select 1 for Hizonhood as follows.")
                        hizonhood = active_person.use_service()
                        stock_ticker = input("Enter stock ticker: ")
                        stock_inv_amt = input("Enter stock investment amount: ")
                        hizonhood.invest(stock_ticker, stock_inv_amt)
                        hizonhood.hizon_to_json()
                    else:
                        print("No investment made.")
                    # CreditCard: Make Purchase, Extract data from JSON
                    credit_card_actions = input("Would you like to make a purchase using your credit card?\n"
                                                "Enter 'Y' for Yes, otherwise, type anything: ")
                    if credit_card_actions == 'Y':
                        print("Select 2 for Credit Card as follows.")
                        credit_card = active_person.use_service()
                        cc_purchase = credit_card.make_purchase()
                        cc_purchase.credit_to_json()
                    else:
                        print("No purchase made.")
                    # Loan: Take loan
                    loan_action = input("Would you like to take out a loan?\n"
                                        "Enter 'Y' for Yes, otherwise, type anything: ")
                    if loan_action == 'Y':
                        print("Select 3 for Loan as follows.")
                        loan = active_person.use_service()
                        loan_taken = loan.take_loan()

                    more_service_req = input("Would you like to perform any additional service requests?\n"
                                             "Enter 'Y' for Yes and 'N' to stop using services: ")

            more_action_req = input("Would you like to perform another action?\n"
                                    "Enter 'Y' for another action and "
                                    "'N' to stop using the banking system.")
    elif visit_bank_req == 'N':
        print("Did not visit bank.\n"
              "You will not be able to use any services without first visiting the bank "
              "and performing an action.")
