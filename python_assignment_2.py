"""
    import class datetime from datetime module for input date
    import sys for exit
    import csv for file handling
"""
import csv
import os
import sys
import re
from datetime import datetime


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
        datetime_obj = datetime.strptime(transaction["date"], '%Y-%m-%d %H:%M:%S')
        month = datetime_obj.strftime('%B')
        if month not in monthly_details:
            monthly_details[month] = {
                'debit': 0,
                'credit': 0
            }
        if transaction["type"].lower() == "debit":
            monthly_details[month]["debit"] += 1
        elif transaction["type"].lower() == "credit":
            monthly_details[month]["credit"] += 1

    for month_name, monthly_info in monthly_details.items():
        print("month name: {}".format(month_name))
        for key in monthly_info:
            print("{}: {}".format(key, monthly_info[key]))


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
        month = datetime.strptime(transaction["date"], '%Y-%m-%d %H:%M:%S')
        month = month.strftime('%B')
        if month not in monthly_details:
            monthly_details[month] = {
                'debit': 0,
                'credit': 0
            }
        if transaction["type"] == "debit":
            monthly_details[month]["debit"] += float(transaction["amount"])
        elif transaction["type"] == "credit":
            monthly_details[month]["credit"] += float(transaction["amount"])
    for month_name, monthly_info in monthly_details.items():
        print("month name:", month_name)
        for key in monthly_info:
            print(key + ":", monthly_info[key])


def minimum_debit_credit_amount_of_year(all_transaction_details):
    """
        this function is for getting minimum number of debit and credit
        Attributes:
            all_transaction_details -list[]
        return:
            minimum number of debit and credit
    """
    type_name = input("Enter debit or credit for minimum amount:")
    if type_name == "debit":
        minimum_debit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "debit":
                minimum_debit.append(float(transaction["amount"]))
        print("Minimum amount of year:", min(minimum_debit, default=0))
    elif type_name == "credit":
        minimum_credit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "credit":
                minimum_credit.append(float(transaction["amount"]))
        print("Minimum amount of year:", min(minimum_credit, default=0))


def maximum_debit_credit_amount_of_year(all_transaction_details):
    """
        this function is for getting maximum amount number of debit and credit
        Attributes:
            all_transaction_details -list[]
        return:
            maximum amount number of debit and credit
    """
    type_name = input("Enter debit or credit for maximum amount:")
    if type_name == "debit":
        maximum_debit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "debit":
                maximum_debit.append(float(transaction["amount"]))
        print("Maximum debit amount of year:", max(maximum_debit, default=0))
    elif type_name == "credit":
        maximum_credit = []
        for transaction in all_transaction_details:
            if transaction["type"] == "credit":
                maximum_credit.append(float(transaction["amount"]))
        print("Maximum amount of year:", max(maximum_credit, default=0))


def all_transaction_for_given_month(all_transaction_details, user_month):
    """
        This function is for getting all transaction for given month
        Attributes:
            all_transaction_details -list[]
            user_month -int()
        return:
            all transaction for given month by user
    """
    is_transactions_available = False
    for transaction in all_transaction_details:
        datetime_obj = datetime.strptime(transaction["date"], '%Y-%m-%d %H:%M:%S')
        transaction_month = datetime_obj.strftime('%B')
        if user_month.lower() == transaction_month.lower():
            is_transactions_available = True
            print("type:", transaction["type"])
            print("amount:", transaction["amount"])
            print("date:", transaction["date"])
    if not is_transactions_available:
        print("{} month has no transactions".format(user_month))


def get_existing_transactions_from_file():
    all_transaction_details = []

    # get csv file
    csv_file = os.getenv('CSV_FILE')

    if os.path.exists(csv_file):
        with open(csv_file, 'rt') as file:
            data = csv.DictReader(file)
            for row in data:
                print(row)
                all_transaction_details.append(row)
    return all_transaction_details


def add_new_transactions_to_file():
    """
    This is a main function from where we give call to another functions.
    """
    # get csv file
    csv_file = os.getenv('CSV_FILE')

    # user input
    while True:
        try:
            no_of_transaction = int(input("How many transaction you want to add?:"))
            break
        except ValueError:
            print("Invalid input, Please enter correct input")
            continue

    # variable declaration
    all_transaction_details = []
    if not os.path.exists(csv_file):
        all_transaction_details.append(["type", "amount", "date"])

    # Opening file for append operation
    file = open(csv_file, 'a+', newline='')
    writer = csv.writer(file)

    for transaction_no in range(no_of_transaction):
        # variable declaration
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
                    print("Invalid Input,please enter current year")
                    continue
                transaction_details["date"] = transaction_date
                break
            except ValueError:
                print("Invalid Input,Please re-enter:")
                continue
        all_transaction_details.append(transaction_details.values())
    writer.writerows(all_transaction_details)


def delete_all_transactions_from_file():
    """

    """
    # get csv file
    csv_file = os.getenv('CSV_FILE')

    if os.path.exists(csv_file) and os.path.isfile(csv_file):
        os.remove(csv_file)
        print("File removed")
    else:
        print("File not found")


def file_operations():
    while True:
        print("1:Do you want to use existing records in file")
        print("2:Do you want to add new record in the file")
        print("3:Do you want to delete the file")
        print("0:exit")
        print("________________________________________________________")
        try:
            user_input = int(input("Please enter your choice between [0-3]:"))
        except ValueError:
            print("Invalid input, Please enter number between [0-3]...")
            continue
        print("________________________________________________________")
        if user_input == 1:
            all_transaction_details = get_existing_transactions_from_file()
            if not all_transaction_details:
                print('File not available, please add new transactions...')
                continue
            select_operations(all_transaction_details)
        elif user_input == 2:
            add_new_transactions_to_file()
            all_transaction_details = get_existing_transactions_from_file()
            select_operations(all_transaction_details)
        elif user_input == 3:
            delete_all_transactions_from_file()
        elif user_input == 0:
            sys.exit()
        elif user_input > 2:
            print("Invalid input")
            continue


def select_operations(all_transaction_details):
    while True:
        print("1:Monthly number of credit and debit")
        print("2:Monthly amount of debit and credit")
        print("3:Minimum debit or credit amount of the year")
        print("4:Maximum debit or credit amount of the year")
        print("5:Give all the transaction for given month")
        print("0:Exit")
        print("________________________________________________________")
        try:
            user_choice = int(input("Please enter your choice between [0-5]: "))
        except ValueError:
            print("Invalid input, Please enter number between [0-5]")
            continue
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
            try:
                user_month = input("Enter month [January-December]: ")
                user_month = int(user_month)
                print("Please enter valid month from given choices..")
                continue
            except ValueError:
                if user_month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]:
                    print("Please enter valid month from given choices..")
                    continue
                all_transaction_for_given_month(all_transaction_details, user_month)
                print("________________________________________________________")
        elif user_choice == 0:
            break
        elif user_choice > 5:
            print("Invalid choice")


if __name__ == "__main__":
    try:
        os.environ['CSV_FILE']
    except KeyError:
        print('Please set CSV FILE in env first..')
        csv_file = input('Please enter CSV FILE name: ')
        csv_extention = re.search(".csv$", csv_file)
        if not csv_extention:
            csv_file = csv_file + '.csv'
        os.environ['CSV_FILE'] = csv_file

    file_operations()
