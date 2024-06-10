from selenium.webdriver.common.by import By
from website_scrapers.DataPullerInterface import DataPullerInterface
from website_scrapers.grant_dot_gov.GrantDotGovData import GrantDotGovData
from website_scrapers.grant_dot_gov.GrantDotGovRelevanceEvaluator import GrantDotGovRelevanceEvaluator


class GrantDotGovDataPuller(DataPullerInterface):

    baseUrl = 'https://grants.gov/search-grants'
    keywords = 'Women, Trauma, PTSD, Peer support, Financial literacy, Housing, Domestic violence, Sexual assault, Human trafficking, Sex trafficking, Mental health, Wellness, Job coaching'

    relevanceEvaluator = GrantDotGovRelevanceEvaluator()

    def __init__(self, webDriver):
        super().__init__(webDriver)

    def setupPageForPull(self, options):
        #Go to the basic page
        self.driver.get(self.baseUrl)

        # Input the keywords for the search
        keywordsTextBox = self.getElementButWaitUntilLocated('//input[@id="inp-keywords"]')
        keywordsTextBox.send_keys(self.keywords)

        # click off the forecasted
        forcastedButton = self.getElementButWaitUntilLocated('//input[@id="forecasted"]')
        self.clickElementSafely(forcastedButton)

        # Only Look at Grants type
        grantButton = self.getElementButWaitUntilLocated('//input[@id="fi_G"]')
        self.clickElementSafely(grantButton)

        # Might want to disable this one or at least look for the div and then make sure its input label
        # Is what we are expecting
        eligibilityButton = self.getElementButWaitUntilLocated('//input[@id="el_12"]')
        self.clickElementSafely(eligibilityButton)

        transportCategoryButton = self.getElementButWaitUntilLocated('//input[@id="cat_HL"]')
        self.clickElementSafely(transportCategoryButton)

        searchButton = self.getElementButWaitUntilLocated('//button[@id="btn-search"]')
        self.clickElementSafely(searchButton)

        return

    def pullData(self, arguments):
        pulledData = []

        maxPages = self.getMaxPageNumber()

        for i in range(1, maxPages+1):
            if i > maxPages or \
                    self.clickPageNumber(i) == False:
                break

            #Get each row
            tableRows = self.driver.find_elements(By.XPATH, '//tbody/tr')
            for tableRow in tableRows:
                rowColumns = tableRow.find_elements(By.XPATH, './td')
                rowData = {}

                if len(rowColumns) != 6:
                    print("Unable to find a row with 6 columns")
                    continue

                grantData = GrantDotGovData(rowColumns[0].find_element(By.XPATH, './a').get_attribute('href'),
                                            rowColumns[1].text,
                                            rowColumns[2].text,
                                            rowColumns[3].text,
                                            rowColumns[4].text,
                                            rowColumns[5].find_element(By.XPATH, './span').text,
                                            'NEW')
                # Apply the relevance Evaluator and set its ranking
                grantData.relevance = self.relevanceEvaluator.rankData(grantData, None)

                pulledData.append(grantData)

        return pulledData;

    def getMaxPageNumber(self):
        pageElementList = self.getElementsButWaitUntilLocated('//li[contains(@class, "usa-pagination__page-no")]/a')
        lastPageNumber = pageElementList[-1].text
        return int(lastPageNumber)

    def clickPageNumber(self, pageNumber):
        pageElementList = self.getElementsButWaitUntilLocated('//li[contains(@class, "usa-pagination__page-no")]/a')
        for pageLinkElement in pageElementList:
            if pageLinkElement.text == str(pageNumber):
                self.clickElementSafely(pageLinkElement);
                return True

        print("Failed to find page number " + str(pageNumber) + " in Grants.gov!")
        return False




