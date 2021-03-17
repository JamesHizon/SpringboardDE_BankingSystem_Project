# Springboard Data Engineering Banking System Mini-Project

![img.png](https://www.bcsconsulting.com/wp-content/uploads/2018/12/bank-system-tile.png)


The following Python script includes three parent classes to simulate a simple banking system:
1. Person (Child classes: Customer, Employee)
2. Account (Child classes: CheckingAccount, SavingsAccount)
3. Services (Child classes: Hizonhood, CreditCard, Loan)


### Command Line Interface User Interaction (requires Python Version 3)

First, call each file after switching to src directory inside terminal.

```
cd src
python3 Banking_system_test.py
```

A Python Script will then ask for the user to provide input. 
The following includes full implementation of all the main base classes 
with a corresponding child class:


```
(venv) (base) jameshizon@Jamess-MBP src % python3 Banking_system_test.py                         
Enter first name: James
Enter last name: Hizon
Enter address: 123 Code Avenue
Are you a Customer or an Employee?
Enter 1 for 'Customer'
Enter 2 for 'Employee'
1
Currently, you have no cash available.
Enter 'Y' if this is the case.
Otherwise, enter new cash amount: Y
Would you like to get or set customer accounts?
Enter 1 to get customer accounts
Enter 2 to set customer accounts
Enter 3 to extract customer data from JSON file (if exists)
Enter 4 to perform none of the listed actions: 
4
Did not perform an action.
Would you like to visit the bank?
Enter 'Y' for Yes and 'N' for No: Y
Select account type:
Type 1 for checking account and 2 for savings account.1
You currently do not have a Checking Account.
A new checking account will be created automatically for you.

Set up PIN Code: 1234
Welcome to James' Deposit & Withdrawal Machine!
Enter first name: James
Enter last name: Hizon
Enter address: 123 Code Avenue
Person has chosen to visit the bank!
Enter number for specified action:
Enter 1 to withdraw
Enter 2 to deposit
Enter 3 to display current balance: 2
Enter amount to deposit: 1000
Would you like to perform another action?
Enter 'Y' for another action and 'N' to stop using the banking system: Y
Enter number for specified action:
Enter 1 to withdraw
Enter 2 to deposit
Enter 3 to display balance
Enter 4 to use a service: 3
Available Balance:  1000.0
Would you like to perform another action?
Enter 'Y' for another action and 'N' to stop using the banking system.Y
Enter number for specified action:
Enter 1 to withdraw
Enter 2 to deposit
Enter 3 to display balance
Enter 4 to use a service: 4
Select service:
1 for Hizonhood
2 for Credit Card
3 for Loan1
Enter amount to deposit into Hizonhood: 500
Enter Investor name: James Hizon
Would you like to perform any additional service requests?
Enter 'Y' for Yes and 'N' to stop using services: Y
Would you like to invest using Hizonhood?
Type 'Y' for Yes and 'N' for No: Y
Select 1 for Hizonhood as follows.
Select service:
1 for Hizonhood
2 for Credit Card
3 for Loan1
Enter amount to deposit into Hizonhood: 500
Enter Investor name: James Hizon
Enter stock ticker: BTC 
Enter stock investment amount: 250
$250.00 has been invested into BTC
Would you like to make a purchase using your credit card?
Enter 'Y' for Yes, otherwise, type anything: No
No purchase made.
Would you like to take out a loan?
Enter 'Y' for Yes, otherwise, type anything: No
Would you like to perform any additional service requests?
Enter 'Y' for Yes and 'N' to stop using services: No
Would you like to perform another action?
Enter 'Y' for another action and 'N' to stop using the banking system.N

```

The last part of the code will create a JSON file called "investment_data_file.json" with the following contents:

```
{"Investor Name": "James Hizon", "Investor Balance": 250.0, "Investor Portfolio": {"BTC": "250"}}
```

In addition, while working with the Customer and Employee classes, two files can be created in similar JSON format: customer_data.json and employee_data.json.
