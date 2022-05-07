import csv

import BookShelf


class Profession:

    @staticmethod
    def get_user_role(user_role):
        if user_role == 1:
            return Librarian()
        elif user_role == 2:
            return Vendor()


class Librarian(Profession):
    """Virtual Library"""

    def __init__(self):
        self.name = input("How would you like to be called: ")

    def check_issued_books():
        issued_books_count = 0
        for book in BookShelf.books:
            for key, value in book.items():
                if book["issued"]:
                    issued_books_count += 1
                    break
                else:
                    continue
        print(f"The number of issued books is {issued_books_count}.")
        print()

    def search_for_book():
        list_of_all_values = list()
        for book in BookShelf.books:
            for value in book.values():
                list_of_all_values.append(value)

        searched_book = input("Which book are you searching for: ")
        if searched_book in list_of_all_values:
            print(f"{searched_book} is available.")
        else:
            print(f"{searched_book} is not available.")

    def verify_a_member():
        approved_universities = ["Sofia University", "Technical University", "New Bulgarian University"]
        user_univercity = input("Please enter the name of your university.")
        if user_univercity in approved_universities:
            print("You are verified as a member of our Library.")
        else:
            print("Your university is not on our members list.")
        print()

    def check_payments():
        payments = 0
        for book in BookShelf.books:
            for key, value in book.items():
                if book["issued"]:
                    payments += book["price"]
                    break
        print(f"The full payments made are {payments} BGN.")
        print()


class Vendor(Profession):
    """Virtual Library"""

    def __init__(self):
        self.name = input("How would you like to be called: ")

    @classmethod
    def initiate_from_csv(cls):
        with open('PaymentDetails.csv', 'r') as f:
            file = csv.DictReader('PaymentDetails.csv')
            payment_method = []
            age_requirement = []
            max_limit = []

            for col in file:
                payment_method.append(col['payment_method'])
                age_requirement.append(col['age_requirement'])
                max_limit.append(col['max_limit'])

    def check_issued_books():
        issued_books_count = 0
        for book in BookShelf.books:
            for key, value in book.items():
                if book["issued"]:
                    issued_books_count += 1
                    break
                else:
                    continue
        print(f"The number of issued books is {issued_books_count}.")
        print()

    def payment_details():
        payment_choice = int(input("How would you like to pay? Please enter 1 for cash,2 for Credit Card, "
                                   "3 for PayPal: "))
        if payment_choice == 1:
            print(
                f"You can pay by {Profession.payment_method[1]} until you reach the limit of {Profession.Vendor.max_limit[1]} BGN")
        elif payment_choice == 2:
            age = int(input("Please share your age: "))
            if age >= Profession.Vendor.age_requirement[2]:
                print(
                    f"You can pay by {Profession.Vendor.payment_method[2]} until you reach the limit of {Profession.Vendor.max_limit[2]} BGN")
            else:
                print(
                    f"You are too young to use this payment method. Try again after {18 - age} years. For now you can "
                    f"pay by cash.")
        elif payment_choice == 3:
            age = int(input("Please share your age: "))
            if age >= Profession.Vendor.age_requirement[3]:
                print(
                    f"You can pay by {Profession.Vendor.payment_method[3]} until you reach the limit of {Profession.Vendor.max_limit[3]} BGN")
            else:
                print(
                    f"You are too young to use this payment method. Try again after {18 - age} years. For now you can "
                    f"pay by cash.")
