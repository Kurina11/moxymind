from pages.PageElement import PageElement

# Dialer Elements
contactsTab = PageElement("Contacts tab in Dialer", '//android.widget.FrameLayout[@content-desc="Contacts"]')
searchRecycler = PageElement("Search recycler for focus reset", '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.dialer:id/search_recycler_view"]')

# Contacts Tab
createNewContactButton = PageElement("Create new contact button in Contacts tab", '//android.widget.TextView[@text="Create new contact"]')
contactFirstRow = PageElement("Contact Photo button first row", '(//android.widget.QuickContactBadge[contains(@content-desc,"Quick contact")])[1]')
contactsSpeedDial = PageElement("Contacts speed dial button", '//android.widget.ImageButton[@content-desc="key pad"]')

# New Contact Formular
firstNameContactInput = PageElement("New contact formular first name", '(//android.widget.LinearLayout[@resource-id="com.google.android.contacts:id/editors"])[1]/android.widget.LinearLayout[1]//android.widget.EditText')
lastNameContactInput = PageElement("New contact formular last name", '(//android.widget.LinearLayout[@resource-id="com.google.android.contacts:id/editors"])[1]/android.widget.LinearLayout[2]//android.widget.EditText')
phoneNumberContactInput = PageElement("New contact formular phone number", '(//android.widget.LinearLayout[@resource-id="com.google.android.contacts:id/editors"])[3]//android.widget.EditText')
saveContactButton = PageElement("Save new contact formular button", '//android.widget.LinearLayout[@resource-id="com.google.android.contacts:id/menu_save"]')

# Speed Dial
speedDialInput = PageElement("Speed dial input field", '//android.widget.EditText[@resource-id="com.google.android.dialer:id/digits"]')
createNewContactButtonSpeedDial = PageElement("Create new contact button in speed dial", '//android.widget.TextView[@resource-id="com.google.android.dialer:id/search_action_text" and @text="Create new contact"]')
speedDialContactFirstNameFormular = PageElement("New contact formular first name in speed dial", '//android.widget.EditText[@text="First name"]')
speedDialContactLastNameFormular = PageElement("New contact formular last name in speed dial", '//android.widget.EditText[@text="Last name"]')
speedDialContactFormularSaveButton = PageElement("Save new contact formular button in speed dial", '//android.widget.Button[@resource-id="com.google.android.contacts:id/save_button"]')

# Contact details
contactName = PageElement("Contact Name in Contact details", '//android.widget.TextView[@resource-id="com.google.android.contacts:id/large_title"]')
contactNumber = PageElement("Contact Number in Contact details", '//android.widget.TextView[@resource-id="com.google.android.contacts:id/header"]')
contactMoreOptionsButton = PageElement("Contact more options button in Contact details", '//android.widget.ImageView[@content-desc="More options"]')
contactDeleteButton = PageElement("Contact delete button in Contact details", '//android.widget.TextView[@resource-id="com.google.android.contacts:id/title" and @text="Delete"]')
deleteButtonInPopUp = PageElement("Contact delete button in verification pop-up", '//android.widget.Button[@resource-id="android:id/button1"]')