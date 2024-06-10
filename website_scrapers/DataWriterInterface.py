
class DataWriterInterface:

    def __init__(self):
        pass

    """
    Uses the provided threshold and all its other context data to see if we need to write it.
    """
    def shouldWriteGrantToFile(self, grantData, relevanceThreshhold, fileData):
        return False

    """
    Will be using this because we are re-writing the file entirely each update.
    """
    def writeCsvFileHeader(self):
        pass

    """
    Iterative method allows for us to use the Main scrapper interface as the controller of how we write/update the file
    """
    def writeGrantAsCsv(self, grantData):
        pass

    """
    Method that gets all existing grants (and whatever user data we want input into the CSV) out and into the format
    that we are chosing to store it as. Then we can do manipulations, orderings, etc. and it can be written to later.
    """
    def getGrantDataFromCsv(self):
        pass

    def clearFileData(self):
        pass
