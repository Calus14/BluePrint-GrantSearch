from website_scrapers.GrantDataScraperInterface import GrantDataScraperInterface
from website_scrapers.grant_dot_gov.GrantDotGovDataPuller import GrantDotGovDataPuller
from website_scrapers.grant_dot_gov.GrantDotGovDataWriter import GrantDotGovDataWriter


class GrantDotGovGrantScraper(GrantDataScraperInterface):

    def __init__(self, webDriver):
        self.grantDataPuller = GrantDotGovDataPuller(webDriver)
        self.grantDataWriter = GrantDotGovDataWriter()
        self.pulledGrantData = []

    def pullNewGrantData(self):
        self.grantDataPuller.setupPageForPull(None)
        self.pulledGrantData = self.grantDataPuller.pullData(None)

    def getPulledGrantData(self):
        return self.pulledGrantData

    def updateGrantDataCsvWithData(self, grantData):
        self.grantDataWriter.getGrantDataFromCsv()
        self.grantDataWriter.clearFileData()
        self.grantDataWriter.writeCsvFileHeader()
        for grant in grantData:
            if self.grantDataWriter.shouldWriteGrantToFile(grant, .8):
                self.grantDataWriter.writeGrantAsCsv(grant)
            else:
                print("Not writing data - " + grant.urlLink)
