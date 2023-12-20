""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        # The balance and interest attributes are set to the values passed in the parameters.
        # I would normally make these read only so the setters HAD to be used to change the values after initialization.
        #self.__balance = balance
        #self.__interest = interest
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest
