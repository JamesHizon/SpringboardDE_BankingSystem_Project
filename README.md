# Springboard Data Engineering Banking System Mini-Project

![img.png](https://www.bcsconsulting.com/wp-content/uploads/2018/12/bank-system-tile.png)


The following Python script includes three parent classes to simulate a simple banking system:
1. Person (Child classes: Customer, Employee)
2. Account (Child classes: CheckingAccount, SavingsAccount)
3. Services (Child classes: Hizonhood, CreditCard, Loan)

The purpose of inheriting from the Service class is to be able to see what other Services are available,
in case the user decides to want to select a different type of service. It is simple, for the sake of building 
knowledge of OOP.

### Command Line Interface User Interaction (requires Python Version 3)

First, call each file after switching to src directory inside terminal.

```
cd src
python3 Banking_system_test.py
```

For the sake of simplicity, I include a simple working solution of the banking system which does not include usage of Services class. The test file basically requests for user information, asks whether the person is an employee or customer, asks about the amount of cash available, requests for account type, and then automatically creates an account for the user. Next, the customer chooses to deposit $500 into his account.

```
Enter first name: James
Enter last name: Hizon
Enter address: 123 Code Avenue
Are you a Customer or an Employee?
Enter 1 for 'Customer'
Enter 2 for 'Employee'
1
Currently, you have no cash available.
Enter 'Y' if this is the case.
Otherwise, enter new cash amount: 500
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
Enter amount to deposit: 500
Would you like to perform another action?
Enter 'Y' for another action and 'N' to stop using the banking system: N
```

The other classes can be implemented if necessary, but is not included in the test file "Banking_system_test.py".
