# SpringboardDE_BankingSystem_Project
Banking System Code using OOP

The following code includes three parent classes: Account, Person and Services

Customer and Employee classes will inherit from the Person class, the
CheckingAccount and SavingsAccount classes will inherit from the Account class,
and Hizonhood, CreditCard and Loan classes will inherit from the services class.

I created methods to store and extract data in JSON format within each class.

A working example of interacting with each class can be detailed as follows:

1) Create an instance of the Person class.
2) Call the ".visit_bank()" method as an object and account to be used.
3) The program will ask to set up a PIN Code if an account has not yet been registered. Otherwise, it will simply ask for PIN Code (stored inside dictionary).
4) Call the ".deposit()" method to have a certain balance (say $100).
5) Call the ".use_service()" method to choose a specified service as an object. It will request for amount to be used.
6) Call the ".invest()" method and specify stock_ticker and investment amount.
7) Call the ".hizon_to_json()" method to store data in JSON format.

The following is an example of how to run this code, where I incorporate all of the main classes (Account, Service and Person):

IN:
John_Smith = Customer("John", "Smith", "100 ABC Street", 100, "CheckingAccount")
bank_visit = John_Smith.visit_bank()
OUT:
Select account type:
Type 1 for checking account and 2 for savings account.>? 1
You currently do not have a Checking Account.
A new checking account will be created automatically for you.
Set up PIN Code: >? 1234
Welcome to James' Deposit & Withdrawal Machine!
Enter first name: >? John
Enter last name: >? Smith
Enter address: >? 123 hizon ave
IN:
bank_visit.deposit()
OUT:
Enter amount to deposit: >? 100
100.0
IN:
use_hizonhood = bank_visit.use_service()
Select service:
1 for Hizonhood
2 for Credit Card
3 for Loan>? 1
Enter amount to deposit into Hizonhood: >? 80
Enter Investor name: >? John
IN:
use_hizonhood.investment_portfolio
OUT:
{}
IN:
use_hizonhood.json_dict
OUT:
{'Investor Name': 'John', 'Investor Balance': 80.0, 'Investor Portfolio': {}}
IN:
use_hizonhood.invest("DOGE", 20)
{'Investor Name': 'John', 'Investor Balance': 60.0, 'Investor Portfolio': {'DOGE': 20}}
{'DOGE': 20}
OUT:
$20.00 has been invested into DOGE
IN:
use_hizonhood.hizon_to_json()
OUT:
'New JSON file created!'

The last part of the code will create a JSON file called "investment_data_file.json" with the following contents:

{"Investor Name": "John", "Investor Balance": 60.0, "Investor Portfolio": {"DOGE": 20}}


