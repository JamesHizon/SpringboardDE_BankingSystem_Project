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

I am currently working on fixing errors inside my code.


