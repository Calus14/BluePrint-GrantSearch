
class GrantDotGovData:

    def __init__(self, urlLink, title, govAgency, govStatus, postedDate, closeDate, bpStatus):
        self.urlLink = urlLink
        self.title = title
        self.govAgency = govAgency
        self.govStatus = govStatus
        self.postedDate = postedDate
        self.closeDate = closeDate
        self.bpStatus = bpStatus
        self.relevance = 0

    def getAsCsvString(self):
        columns = ["\"" + self.title + "\"", "\"" + self.govAgency + "\"", self.postedDate, self.closeDate, self.urlLink, self.bpStatus]
        return ",".join(columns)

def _CreateFromCsvString(csvString):
    columnValues = csvString.split(",")

    # TODO Update if we add more columns to store in the CSV
    if(len(columnValues) != 6):
        print("ERROR! CSV format is expecting 6 columns!")

    try:
        grantData = GrantDotGovData(columnValues[4],
                                    columnValues[0],
                                    columnValues[1],
                                    "",
                                    columnValues[2],
                                    columnValues[3],
                                    columnValues[5])
    except Exception as e:
        print("Failed to fully set all values for grant data from csv string = \""+csvString+"\"")
        return None

    return grantData