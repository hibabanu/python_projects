
def restaurant():
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")
        
        feedback = input("Write your feedback: ").strip()
        if not feedback:
            raise ValueError("Feedback cannot be empty")
        
        print(f"Thank you! Name: {name}\nFeedback: {feedback}")

    except ValueError as ve:
        print(ve)

    finally:
        print("Thank you for visiting our restaurant.")

restaurant()
