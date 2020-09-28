from all_imports import *

url = "http://automationpractice.com/index.php"
sign_in_link = "//a[@class='login']"
email_create = "//input[@id='email_create']"
button_create = "//button[@id='SubmitCreate']"
gender_input = "//input[@id='id_gender1']"
first_name_input = "//input[@id='customer_firstname']"
last_name_input = "//input[@id='customer_lastname']"
password_input = "//input[@id='passwd']"
day_sel = "//select[@id='days']"
month_sel = "//select[@id='months']"
year_sel = "//select[@id='years']"
address_input = "//input[@id='address1']"
city_input = "//input[@id='city']"
state_select = "//select[@id='id_state']"
zip_input = "//input[@id='postcode']"
country_select = "//select[@id='id_country']"
mobile_phone_input = "//input[@id='phone_mobile']"
register_button = "//button[@id='submitAccount']"
main_path = "//p[@class='info-account']"
sign_out_link = "//a[@class='logout']"

email = "kirill3393367@mail.com"
pwd = "12345qwerty"
name = "Kirill"
last_name = "New"
address = "145 East 50th st"
city = "New York"
zip = "12345"
phone = "2344563455"

def launch_website():
    driver.get(url)
    print(f"Opened the browser and website: {url}")
    time.sleep(2)


def click_element_by_xpath(xpath, text):
    element = driver.find_element_by_xpath(xpath)
    print(f"Clicking the element: {text}")
    element.click()
    time.sleep(2)


def enter_text_by_xpath(xpath, text):
    element = driver.find_element_by_xpath(xpath)
    print(f"Email entering: {text}")
    element.send_keys(text)
    time.sleep(2)


def radio_button(xpath):
    element = driver.find_element_by_xpath(xpath)
    element.click()
    print("Gender option")
    time.sleep(2)



def select(xpath, text):
    element = driver.find_element_by_xpath(xpath)
    element_selection = Select(element)
    element_selection.select_by_value(text)
    text_selected_ones = [option.text for option in element_selection.all_selected_options]
    print("Options selected: ", text_selected_ones)
    time.sleep(2)


def account_ready(xpath):
    element = driver.find_element_by_xpath(xpath)
    assert "Welcome to your account" in element.text
    print("Account verified")
    time.sleep(2)

def sign_out(xpath):
    element = driver.find_element_by_xpath(sign_out_link)
    element.is_displayed()
    print("Sign out button is present")

def close():
    print("Account created successfully! Browser closing...")
    driver.quit()



