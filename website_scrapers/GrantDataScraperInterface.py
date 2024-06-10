
class GrantDataScraperInterface:

    """
    pulls data using Data Puller Interface into a data format that will be used with teh writer and relevance evaluator.
    """
    def pullNewGrantData(self):
        pass

    def getPulledGrantData(self):
        return self.pulledGrantData

    """
    Method exists to de-couple writing of data with the process of getting the data so i can easily have programatic 
    updates to the csv data.
    """
    def updateGrantDataCsvWithData(self, grantData):
        pass