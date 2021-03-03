"""
    import class datetime from datetime module for input date
    import sys for exit
"""
from datetime import datetime
import sys


def monthly_number_of_debit_and_credit(all_transaction_details):
    """
        this function is for getting monthly number of debit and credit
        Attributes:
            all_transaction_details -list[]
        return:
            monthly count of debit and credit
    """
    monthly_details = {}
    for transaction in all_transaction_details:
        month = transaction["date"].strftime('%B')
        if month not in monthly_details:
            monthly_details[month] = {
                'debit': 0,
                'credit': 0
            }
        if transaction["type"] == "debit":
            monthly_details[month]["debit"] += 1
        elif transaction["type"] == "credit":
            monthly_details[month]["credit"] += 1
    for month_name, monthly_info in monthly_details.items():
        print("month name:", month_name)
        for key in monthly_info:
            print(key+":", monthly_info[key])


def monthly_amount_of_debit_and_credit(all_transaction_details):
    """
        this function is for getting monthly amount of debit and credit
        Attributes:
            all_transaction_details -list[]
        return:
            monthly amount of debit and credit
    """
    monthly_details = {}
    for transaction in all_transaction_details:
        month = transaction.get("date").strftime('%B')
        if month not in monthly_details:
            monthly_details[month] = {
                'debit': 0,
                'credit': 0
            }
        if transaction["type"] == "debit":
            monthly_details[month]["debit"] += transaction["amount"]
        elif transaction["type"] == "credit":
            monthly_details[month]["credit"] += transaction["amount"]
    for month_name, monthly_info in monthly_details.items():
        print("month name:", month_name)
        for key in monthly_info:
            print(key+":", monthly_info[key])


def minimum_debit_credit_amount_of_year(all_transaction_details):
    """
        this function is for getting minimum number of debit and credit
        Attributes:
            all_transaction_details -list[]
        return:
            minimum number of debit and credit
    """
    tran = input("Enter debit or credit for minimum amount: ")
    if tran == "debit":
        minimum_debit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "debit":
                minimum_debit.append(transaction["amount"])
        print("Minimum amount of year:", min(minimum_debit, default=0))
    elif tran == "credit":
        minimum_credit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "credit":
                minimum_credit.append(transaction["amount"])
        print("Minimum amount of year:", min(minimum_credit, default=0))


def maximum_debit_credit_amount_of_year(all_transaction_details):
    """
        this function is for getting maximum amount number of debit and credit
        Attributes:
            all_transaction_details -list[]
        return:
            maximum amount number of debit and credit
    """
    tran = input("Enter debit or credit for minimum amount: ")
    if tran == "debit":
        maximum_debit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "debit":
                maximum_debit.append(transaction["amount"])
        print("Maximum debit amount of year:", max(maximum_debit, default=0))
    elif tran == "credit":
        maximum_credit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "credit":
                maximum_credit.append(transaction["amount"])
        print("Maximum amount of year:", max(maximum_credit, default=0))


def all_transtion_for_given_month(all_transaction_details, user_month):
    """
        this function is for getting all transaction for given month
        Attributes:
            all_transaction_details -list[]
            user_month -int()
        return:
            all transaction for given month by user
    """
    all_transaction_details_monthly = []
    for transaction in all_transaction_details:
        transaction_month = transaction["date"].strftime('%B')
        if user_month.lower() == transaction_month.lower():
            print("type:", transaction["type"])
            print("amount:", transaction["amount"])
            print("date:", transaction["date"])
            all_transaction_details_monthly.append(transaction)


def store_user_transactions():
    """
        this is a main function.from where we give call to another functions
    """
    # user input
    no_of_transaction = int(input("How many transaction you want to add?:"))
    # variable declaration
    all_transaction_details = []
    for transaction_no in range(no_of_transaction):
        # variable declaratcion
        transaction_details = {}
        print("________________________________________________________")
        print("Please enter transaction no {}..".format(transaction_no + 1))
        # get transaction_type, transaction_amount and transaction_date
        while True:
            if "type" not in transaction_details.keys():
                transaction_type = input("Transaction by Debit or Credit:")
                if transaction_type.lower() not in ['debit', 'credit']:
                    print("Invalid input, Enter debit or credit")
                    continue
                transaction_details["type"] = transaction_type
            try:
                if "amount" not in transaction_details.keys():
                    transaction_amount = float(input("Amount in Rs:"))
                    transaction_details["amount"] = transaction_amount
                transaction_date = input("Enter Date in format dd/mm/yyyy:")
                transaction_date = datetime.strptime(transaction_date, '%d/%m/%Y')
                current_year = datetime.now().year
                if transaction_date.year != current_year:
                    print("Invalid Inputplease enter current year")
                    continue
                transaction_details["date"] = transaction_date
                break
            except ValueError:
                print("Invalid Input,Please re-enter:")
                continue
        all_transaction_details.append(transaction_details)
    while True:
        print("1:Monthly number of credit and debit")
        print("2:Monthly amount of debit and credit")
        print("3:Minimum debit or credit amount of the year")
        print("4:Maximum debit or credit amount of the year")
        print("5:Give all the transaction for given month")
        print("0:Exit")
        print("________________________________________________________")
        user_choice = int(input("Please enter your choice between [0-7]:"))
        if user_choice == 1:
            monthly_number_of_debit_and_credit(all_transaction_details)
            print("________________________________________________________")
        elif user_choice == 2:
            monthly_amount_of_debit_and_credit(all_transaction_details)
            print("________________________________________________________")
        elif user_choice == 3:
            minimum_debit_credit_amount_of_year(all_transaction_details)
            print("________________________________________________________")
        elif user_choice == 4:
            maximum_debit_credit_amount_of_year(all_transaction_details)
            print("________________________________________________________")
        elif user_choice == 5:
            user_month = input("Enter month(January-December):")
            all_transtion_for_given_month(all_transaction_details, user_month)
            print("________________________________________________________")
        elif user_choice == 0:
            sys.exit()
        elif user_choice > 5:
            print("Invalid choice")


if __name__ == "__main__":
    store_user_transactions()
