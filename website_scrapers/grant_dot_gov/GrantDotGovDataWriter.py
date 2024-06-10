import os

from website_scrapers.DataWriterInterface import DataWriterInterface
from website_scrapers.grant_dot_gov.GrantDotGovData import GrantDotGovData, _CreateFromCsvString


class GrantDotGovDataWriter(DataWriterInterface):

    columns = ['Title', 'Agency', 'Date Posted', 'Date Closing', 'URL Link', 'BluePrint Status']

    def __init__(self):
        # All grants scraped should go in the users Documents -> ScrapedGrants folder on their P.C.
        self.directory = os.path.join(os.path.expanduser('~'), 'Documents', 'ScrapedGrants')
        os.makedirs(self.directory, exist_ok=True)
        self.grantFilePath = os.path.join(self.directory, 'grant_dot_gov.csv')

        # Initial instilation of the file to track grants
        if not os.path.exists(self.grantFilePath):
            self.grantFile = open(self.grantFilePath, 'w')
            self.grantFile.close()
            self.writeCsvFileHeader()

        self.getGrantDataFromCsv()

    """
    Uses the provided threshold and all its other context data to see if we need to write it.
    """
    def shouldWriteGrantToFile(self, grantData, relevanceThreshhold):
        # TODO change to be a real relevance threshold
        if(grantData.relevance < 0.8):
            return False

        # For right now we are not going to update any grant Data after it has been seen once
        # fileGrants must be a dictionary with the grant link as the key
        if(grantData.urlLink in self.fileGrants):
            return False

        return True

    """
    Will be using this because we are re-writing the file entirely each update.
    """
    def writeCsvFileHeader(self):
        self.grantFile = open(self.grantFilePath, 'a+')
        headerLine = ",".join(self.columns)
        self.grantFile.write(headerLine + "\n")
        self.grantFile.close()

    """
    Iterative method allows for us to use the Main scrapper interface as the controller of how we write/update the file
    """
    def writeGrantAsCsv(self, grantData):
        self.grantFile = open(self.grantFilePath, 'a+')
        self.grantFile.write(grantData.getAsCsvString() + "\n")
        self.grantFile.close()

    """
    Method that gets all existing grants (and whatever user data we want input into the CSV) out and into the format
    that we are chosing to store it as. Then we can do manipulations, orderings, etc. and it can be written to later.
    """
    def getGrantDataFromCsv(self):
        self.grantFile = open(self.grantFilePath, 'r')
        grantLines = self.grantFile.readlines()[1:] # Avoid the first line which should be the headers.

        self.fileGrants = {}
        for line in grantLines:
            readGrantData = _CreateFromCsvString(line)
            if readGrantData == None:
                continue
            self.fileGrants[readGrantData.urlLink] = readGrantData

        self.grantFile.close()

    def clearFileData(self):
        self.backUpData = self.getGrantDataFromCsv()
        self.grantFile = open(self.grantFilePath, 'w')  # Open the file in write mode to clear its contents
        self.grantFile.close()