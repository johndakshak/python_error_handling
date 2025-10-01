# ===== TASK 1: Password Validator =====
# Create a custom WeakPasswordError exception
# The function should validate password strength and raise WeakPasswordError if:
# - Password is less than 8 characters
# - Password doesn't contain at least one digit
# If input is empty, raise ValueError with message "Error: password cannot be empty"
# Keep asking until a valid password is entered

print("=== Task 1: Password Validator ===")
print("Password must be at least 8 characters and contain at least one digit\n")

class WeakPasswordError(Exception):
    pass

def validate_password(prompt):
    #
    # Write your code here.
    # Define WeakPasswordError class
    # Validate password rules
    # Handle exceptions and keep prompting
    #
    flag = True

    while flag:
        try:
            password = input(prompt).strip()
            password_has_atleast_one_digit = False

            for char in password:
                if char.isdigit():
                    password_has_atleast_one_digit = True

            if password == "":
                raise ValueError("Error: password cannot be empty") 
            
            if len(password) < 8:
                raise WeakPasswordError("Error: Password must be at least eight characters long")
            
            if not password_has_atleast_one_digit:
                raise WeakPasswordError("Error: Password must have at least one digit")
            
            flag = False
            return password
            
        except ValueError as value_error:
            print(value_error)

        except WeakPasswordError as weak_password:
            print(weak_password)
        

password = validate_password("Enter your password: ")
print(f"Password accepted: {'*' * len(password)}")
print()