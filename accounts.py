__doc__ = "Classes for different financial accounts"
__author__ = "Eve Chase <eve.adde.chase@gmail.com>"

import numpy as np


applications_per_year = {
    'daily': 365, #FIXME leap year
    'monthly': 12,
    'yearly': 1,
}

class AccruingAccount():
    """
    Generic account that accrues interest over time
    """

    def __init__(self, value=1000, interest_rate=0.07,
        compound_freq='daily'):
        """
        Parameters:
        -----------
        value: float
            initial value of account

        interest_rate: float
            interest rate of investment. Value between 0 and 1
        
        compound_freq: str
            frequency that interest is compounded.
            Options: daily, monthly, yearly
        """
        self.init_value = value

        assert interest_rate >= 0
        if interest_rate > 1:
            interest_rate /= 100
        self.interest_rate = interest_rate
        
        assert compound_freq in ['daily', 'monthly', 'yearly']
        self.compound_freq = compound_freq
        self.accruals_per_year = applications_per_year[compound_freq]



    def compound_interest(self, time=1):
        """
        Compute compound interest

        time: float or numpy array
            Time in years that account is accruing
        """
        #FIXME: make time an object
        return self.init_value * (
            1 + self.interest_rate/self.accruals_per_year) ** (
            self.accruals_per_year * time)



