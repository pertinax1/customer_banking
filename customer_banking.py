# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('Enter your savings starting balance: '))
    savings_interest = float(input('Enter your interest rate: '))
    savings_maturity = float(input('Enter the number of months that interest will be earned: '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'Savings Interest earned is: ${round(interest_earned, 2):.2f}')
    print(f'Updated Savings account balance is: ${round(updated_savings_balance,2):.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('Enter your CD starting balance: '))
    cd_interest = float(input('Enter your annual percentiage interest rate/yield: '))
    cd_maturity = float(input('Enter the duration of the CD term in months that interest will be earned: '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    interest_earned = round(interest_earned, 2)
    print(f"")
    print(f'CD Interest earned is: ${round(interest_earned, 2):.2f}')
    print(f'Updated CD balance is: ${round(updated_cd_balance, 2):.2f}')

if __name__ == "__main__":
    # Call the main function.
    main()
