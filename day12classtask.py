
import re

def library():
    try:
        title = input("Enter the book title: ")
        if re.fullmatch('[A-Za-z ]+', title):
            pass
        else:
            raise ValueError("Title must contain only letters and spaces.")
        
        year = input("Enter the publication year: ")
        if re.match(r'^(19|20)\d{2}$', year):
            pass
        else:
            raise ValueError("Year must be a four-digit number starting with 19 or 20.")
        
        print(f"Book added , Book Title: {title}, Publication Year: {year}")

    except ValueError as ve:
        print(ve)

    finally:
        print("Thank you for using the library system.")

library()
