from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataPullerInterface:

    def __init__(self, webDriver):
        self.driver = webDriver;

    """
    Method that is called before pulling data which will perform whatever operations (clicking buttons, etc.) 
    before data is read from the driver. 
    """
    def setupPageForPull(self, options):
        return

    # Method that executes the pulling of data once the page has had all operations done on it
    def pullData(self, arguments):
        return;

    # Method that wraps the search for an element by XPath so that we wait up to 10 seconds
    def getElementButWaitUntilLocated(self, xpath, timeout=10):
        if timeout == None or timeout < 0:
            timeout = 10

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def getElementsButWaitUntilLocated(self, xpath, timeout=10):
        if timeout == None or timeout < 0:
            timeout = 10

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

    def clickElementSafely(self, element):
        self.driver.execute_script("arguments[0].click();", element)