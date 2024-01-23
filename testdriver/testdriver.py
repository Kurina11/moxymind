from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("my_log_file.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def logStart(testCaseName):
    logger.info("Start of the test " + testCaseName)
    print("INFO: Start of the test " + testCaseName)

def logEnd(testCaseName):
    logger.info("End of the test " + testCaseName)
    logger.info("Test Passed Successfully")
    print("INFO: End of the test " + testCaseName)

def clickField(driver, element):
    logger.info("Click field " + element.description)
    elementFound = driver.find_element(by=AppiumBy.XPATH, value=element.xPath)
    elementFound.click()
    print("INFO: Click field " + element.description)
    sleep(1.5)


def setFieldValue(driver, element, value):
    logger.info("Set field value " + element.description + " to: " + value)
    elementFound = driver.find_element(by=AppiumBy.XPATH, value=element.xPath)
    elementFound.clear()
    elementFound.send_keys(value)
    print("INFO: Set field value " + element.description + " to: " + value)
    sleep(1)


def verifyFieldValue(driver, element, text):
    logger.info("Verify field value " + element.description + " is: " + text)
    elementFound = driver.find_element(by=AppiumBy.XPATH, value=element.xPath)
    if elementFound.text != text:
        raise Exception(element.description + "'s text: '" + elementFound.text + "' Do not match expected: " + text)
    print("INFO: Verify field value " + element.description + " is: " + text)
    sleep(1)
