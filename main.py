from appium import webdriver
from testdriver.testdriver import *
import unittest
from pages.DialerPage import *
from pages.PhoneBasePage import *
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 7 Pro Assesment',
    platformVersion='13',
)

appium_server_url = 'http://localhost:4723/wd/hub'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        self.driver.press_keycode(3)
        sleep(3)

    def test1(self) -> None:
        """
        Test Case 1: New Contact Formular Basic Flow
        Steps:
            1. Open Dialer App
            2. Open Contacts Tab
            3. Open New Contact Formular
            4. Fill Formular with Base Data and Save
            5. Open Created Contact
            6. Verify Contact Values
            7. Press Contact Menu button
            8. Delete Contact
        """
        logStart("Test Case 1: New Contact Formular Basic Flow")
        self.setUp()
        # 1. Open Dialer App
        clickField(self.driver, dialerIcon)

        # 2. Open Contacts Tab
        clickField(self.driver, contactsTab)

        # 3. Open New Contact Formular
        clickField(self.driver, createNewContactButton)

        # 4. Fill Formular with Base Data and Save
        setFieldValue(self.driver, firstNameContactInput, "Dávid")
        setFieldValue(self.driver, lastNameContactInput, "Kurajda")
        setFieldValue(self.driver, phoneNumberContactInput, "0948530222")
        clickField(self.driver, saveContactButton)

        # 5. Open Created Contact
        clickField(self.driver, contactsTab) # To ensure correct tab is selected
        clickField(self.driver, contactFirstRow)

        # 6. Verify Contact Values
        verifyFieldValue(self.driver, contactName, "Dávid Kurajda")
        verifyFieldValue(self.driver, contactNumber, "0948530222")

        # 7. Press Contact Menu button
        clickField(self.driver, contactMoreOptionsButton)

        # 8. Delete Contact
        clickField(self.driver, contactDeleteButton)
        clickField(self.driver, deleteButtonInPopUp)

        self.tearDown()
        logEnd("Test Case 1: New Contact Formular Basic Flow")


    def test2(self) -> None:
        """
        Test Case 2: New Contact Fast Dial Basic Flow
        Steps:
            1.  Open Dialer App
            2.  Open Contacts Tab
            3.  Press Speed Dial Button
            4.  Fill Contact Number
            5.  Press Create New Contact
            6.  Fill Name in Small Formular and Save
            7.  Clear speed dial and reset focus
            8.  Open Created Contact
            9.  Verify Contact Values
            10. Press Contact Menu button
            11. Delete Contact
        """
        logStart("Test Case 2: New Contact Fast Dial Basic Flow")
        self.setUp()
        # 1. Open Dialer App
        clickField(self.driver, dialerIcon)

        # 2. Open Contacts Tab
        clickField(self.driver, contactsTab)

        # 3. Open New Contact Formular
        clickField(self.driver, contactsSpeedDial)

        # 4. Fill Contact Number
        setFieldValue(self.driver, speedDialInput, "0915530887")

        # 5. Press Create New Contact
        clickField(self.driver, createNewContactButtonSpeedDial)

        # 6. Fill Name in Small Formular and Save
        setFieldValue(self.driver, speedDialContactFirstNameFormular, "Jozef")
        setFieldValue(self.driver, speedDialContactLastNameFormular, "Kurajda")
        clickField(self.driver, speedDialContactFormularSaveButton)

        # 7. Clear speed dial and reset focus
        setFieldValue(self.driver, speedDialInput, "")
        clickField(self.driver, searchRecycler)

        # 8. Open Created Contact
        clickField(self.driver, contactFirstRow)

        # 9. Verify Contact Values
        verifyFieldValue(self.driver, contactName, "Jozef Kurajda")
        verifyFieldValue(self.driver, contactNumber, "0915530887")

        # 10. Press Contact Menu button
        clickField(self.driver, contactMoreOptionsButton)

        # 11. Delete Contact
        clickField(self.driver, contactDeleteButton)
        clickField(self.driver, deleteButtonInPopUp)

        self.tearDown()
        logEnd("Test Case 2: New Contact Fast Dial Basic Flow")

if __name__ == '__main__':
    unittest.main()