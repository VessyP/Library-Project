import profession

while True:
    try:
        user_role = int(input("Please enter 1 if you are a librarian and 2 if you are a vendor: "))
        if user_role == 1:
            break
        elif user_role == 2:
            break
        else:
            print("Invalid input. Please enter 1 for Librarian or 2 for Vendor.")
    except:
        print("Not a nuber. Please enter 1 for Librarian or 2 for Vendor.")

profession.Profession.get_user_role(user_role)

while user_role == 1:
    try:
        choice = int(input('''What would you like to do:
              press 1 to check how many books are issues,
              2 to search for a specific book,
              3 to verify a member,
              4 to check payments,
              5 to quit: '''))

        if choice == 1:
            profession.Librarian.check_issued_books()
        elif choice == 2:
            profession.Librarian.search_for_book()
        elif choice == 3:
            profession.Librarian.verify_a_member()
        elif choice == 4:
            profession.Librarian.check_payments()
        elif choice == 5:
            print("Thank you using our library.")
            break
        else:
            print("Please provide a valid number.")
    except:
        print("Not a nuber. Please provide a number between 1 and 5")

while user_role == 2:
    try:
        choice = int(input('''What would you like to do:
              press 1 to check how many books are issues,
              2 to check payment details,
              3 to quit: '''))
        if choice == 1:
            profession.Vendor.check_issued_books()
        elif choice == 2:
            profession.Vendor.initiate_from_csv()
            profession.Vendor.payment_details()
        elif choice == 3:
            print("Thank you using our library.")
            break
        else:
            print("Please provide a valid number.")
    except:
        print("Not a nuber. Please provide a number between 1 and 3")
