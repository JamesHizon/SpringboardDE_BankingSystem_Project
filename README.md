# Springboard Data Engineering Banking System Mini-Project

![img.png](https://www.bcsconsulting.com/wp-content/uploads/2018/12/bank-system-tile.png)


The following Python script includes three parent classes to simulate a simple banking system:
1. Person (Child classes: Customer, Employee)
2. Account (Child classes: CheckingAccount, SavingsAccount)
3. Services (Child classes: Hizonhood, CreditCard, Loan)

### Step-By-Step Explanation of example which uses each base class (Python file)

1) Create an instance of the Person class.
2) Call the ".visit_bank()" method as an object and account to be used.
3) The program will ask to set up a PIN Code if an account has not yet been registered. Otherwise, it will simply ask for PIN Code (stored inside dictionary).
4) Call the ".deposit()" method to have a certain balance (say $100).
5) Call the ".use_service()" method to choose a specified service as an object. It will request for amount to be used.
6) Call the ".invest()" method and specify stock_ticker and investment amount.
7) Call the ".hizon_to_json()" method to store data in JSON format.

### Command Line Interface User Interaction (requires Python Version 3)

First, call each file after switching to correct directory.

```
cd src
python3 Account.py
python3 Person.py
python3 Service.py
```

Next, call the file in test file in the test folder as follows:

```
cd test
python3 Banking_system_test.py
```

If this does not work, try manually writing the following code after opening up Python version 3.

```
python3
```

```
John_Smith = Customer("John", "Smith", "100 ABC Street", 100, "CheckingAccount")
bank_visit = John_Smith.visit_bank()

Select account type:

Type 1 for checking account and 2 for savings account.>? 1

You currently do not have a Checking Account.

A new checking account will be created automatically for you.

Set up PIN Code: >? 1234

Welcome to James' Deposit & Withdrawal Machine!

Enter first name: >? John

Enter last name: >? Smith

Enter address: >? 123 hizon ave

bank_visit.deposit()

Enter amount to deposit: >? 100

100.0

use_hizonhood = bank_visit.use_service()

Select service:
1 for Hizonhood
2 for Credit Card
3 for Loan>? 1

Enter amount to deposit into Hizonhood: >? 80

Enter Investor name: >? John

use_hizonhood.investment_portfolio

{}

use_hizonhood.json_dict

{'Investor Name': 'John', 'Investor Balance': 80.0, 'Investor Portfolio': {}}

use_hizonhood.invest("DOGE", 20)

{'Investor Name': 'John', 'Investor Balance': 60.0, 'Investor Portfolio': {'DOGE': 20}}

{'DOGE': 20}

$20.00 has been invested into DOGE

use_hizonhood.hizon_to_json()

'New JSON file created!'
```

The last part of the code will create a JSON file called "investment_data_file.json" with the following contents:

```
{"Investor Name": "John", "Investor Balance": 60.0, "Investor Portfolio": {"DOGE": 20}}
```

