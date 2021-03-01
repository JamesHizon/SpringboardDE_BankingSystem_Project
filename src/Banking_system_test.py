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

John_Smith = Customer("John", "Smith", "100 ABC Street", 100, "CheckingAccount")
bank_visit = John_Smith.visit_bank()
bank_visit.deposit()
use_hizonhood = bank_visit.use_service()
use_hizonhood.invest("DOGE", 20)
use_hizonhood.invest("BTC", 40)
use_hizonhood.hizon_to_json()