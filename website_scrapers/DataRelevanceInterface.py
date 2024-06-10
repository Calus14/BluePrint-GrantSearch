"""
Interface that each website should implement. Goal is that after the data has been extracted from the website
we can assign it a relevance value which is normalized (0-1) which tells us how likely this grant will be to ever
be given to BluePrint Agency.
"""
class DataRelevanceInterface:

    """
    Initial Implementation leaves constructor to be empty
    """
    def __init__(self):
        return

    """
    Method that will take an individual piece of data meant to represent a grant offering and based off its properties
    assigns it a rank between 0-1 where 1 is 100% likely we should apply and 0 is no chance we should apply.
    
    Contextual data might also be used for things like what page this entry was found on etc.
    """
    def rankData(self, data, contextData):
        return 0.0