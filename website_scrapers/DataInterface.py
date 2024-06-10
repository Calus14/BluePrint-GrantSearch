
"""
Interface to inherit from to store our data in some defined structure that can be read from a csv line and also
transformed into a csv line
"""
class DataInterface:

    """
    Must implment this in child classes
    """
    def __init__(self, csvString):
        pass

    """
    Must implment this in child classes 
    """
    def getAsCsvString(self):
        pass
