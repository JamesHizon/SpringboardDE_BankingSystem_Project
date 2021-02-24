import json


class Service:

    def __init__(self):
        self.services_list = "Hizonhood\nLoan\nCreditCard"

    def display_all_services(self):
        # Print upcoming services to be available
        print("Upcoming services available soon: Webull\nTD Ameritrade\nVenmo\nPayPal")
        return "Available services: ".format(self.services_list)


class Hizonhood(Service):
    """
    Simple Investment Portfolio service class which will track how much money is invested
    (will not record gains or losses, however, for the sake of simplicity.)
    """
    def __init__(self, investor_balance):
        self.name = input("Enter Investor name: ")
        self.investor_balance = investor_balance
        self.investment_portfolio = {}
        self.json_dict = {"Investor Name": self.name,
                          "Investor Balance": self.investor_balance,
                          "Investor Portfolio": self.investment_portfolio}

    def invest(self, stock_ticker, amount):
        self.investor_balance -= amount
        self.json_dict["Investor Balance"] = self.investor_balance
        if stock_ticker in self.investment_portfolio.keys():
            self.investment_portfolio[stock_ticker] += amount
            self.json_dict["Investor Portfolio"] = self.investment_portfolio
        else:
            self.investment_portfolio[stock_ticker] = amount
            self.json_dict["Investor Portfolio"] = self.investment_portfolio
        for key, value in self.investment_portfolio.items():
            print("${}0 has been invested into {}".format(float(value), key))

    def hizon_to_json(self):
        """
        Using dictionary, we want to dump the data into a JSON object.
        """
        with open("../investment_data_file.json", "w") as write_file:
            json.dump(self.json_dict, write_file)
        return "New JSON file created!"

    def hizon_from_json(self):
        """
        Retrieve JSON file and set to self.investment_portfolio.
        """
        with open("../investment_data_file.json", "r") as read_file:
            self.json_dict = json.load(read_file)
        return "JSON file has been read!"


class CreditCard(Service):

    def __init__(self, name, account_no, expiration_date, cvv, balance):
        self.name = name
        self.account_no = account_no
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.balance = balance
        self.json_dict = {"Name": self.name,
                          "Account": self.account_no,
                          "Expiration Date": self.expiration_date,
                          "CVV": self.cvv,
                          "Balance": self.balance}

    def make_purchase(self, purchase_amount):
        if purchase_amount > self.balance:
            print("Insufficient amount on card.")
        else:
            self.balance -= purchase_amount
            self.json_dict["Balance"] = self.balance
            return "Purchase has been made."

    def credit_to_json(self):
        with open("credit_card_data.json", "w") as credit_card_file:
            json.dump(self.json_dict, credit_card_file)
        return "New JSON file created!"

    def credit_from_json(self):
        with open("credit_card_data.json", "r") as credit_card_file:
            data = json.load(credit_card_file)
        print("JSON file has been loaded!")
        return data


class Loan(Service):

    def __init__(self, loan_amount, consumer_name):
        self.name = consumer_name
        self.loan_amount = loan_amount
        self.json_dict = {"Name": self.name, "Loan Amount": self.loan_amount}

    def take_loan(self, customer_balance):
        customer_balance -= self.loan_amount
        return f"Loan of {self.loan_amount} has been taken!\nCustomer now has {round(customer_balance, 2)} left."