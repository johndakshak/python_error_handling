# ===== TASK 2: Email Validator =====
# Create a custom InvalidEmailError exception
# The function should validate email format and raise InvalidEmailError if:
# - Email doesn't contain exactly one '@' symbol
# - Email doesn't contain at least one '.' after the '@'
# If input is empty, raise ValueError with message "Error: email cannot be empty"
# Keep asking until a valid email is entered

print("=== Task 2: Email Validator ===")
print("Email must contain '@' and a domain with '.'\n")

class InvalidEmailError(Exception):
    pass

def validate_email(prompt):
    #
    # Write your code here.
    # Define InvalidEmailError class
    # Validate email format
    # Handle exceptions and keep prompting
    #
    flag = True

    while flag:
        try:
            email = input(prompt)

            if email == "":
                raise InvalidEmailError("Error: Email cannot be empty")
            
            email_1, email_2 = email.split("@")

            if "." not in email_2:
                raise InvalidEmailError("Error: Email must contain at least one '.' after '@'")

            flag = False
            return email

        except ValueError as value_error:
            print(value_error)

        except InvalidEmailError as invalid_email:
            print(invalid_email)

email = validate_email("Enter your email: ")
print(f"Email accepted: {email}")
print()
