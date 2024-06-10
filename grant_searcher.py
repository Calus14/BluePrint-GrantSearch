from selenium import webdriver
from website_scrapers.grant_dot_gov.GrantDotGovGrantScraper import GrantDotGovGrantScraper


class GrantSearcher:

    def __init__(self):
        self.chromeDriver = webdriver.Chrome()
        #TODO Put all websites that i build scrapers for here!
        self.websitesScrapers = [GrantDotGovGrantScraper(self.chromeDriver)]

    def scrapeWebsites(self):
        for scraper in self.websitesScrapers:
            scraper.pullNewGrantData()

    def finishScrapping(self):
        for scraper in self.websitesScrapers:
            scraper.updateGrantDataCsvWithData(scraper.getPulledGrantData())
        self.chromeDriver.quit()


if __name__ == "__main__":
    test_runner = GrantSearcher()
    test_runner.scrapeWebsites()
    test_runner.finishScrapping()
