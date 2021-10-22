from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://my.manchester.ac.uk/MyCheckIn"

user = "########"
pas = "#########"
path = "#########"


driver = webdriver.Chrome(path)
driver.get(URL)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.clear()
username.send_keys(user)

password.clear()
password.send_keys(pas)
password.send_keys(Keys.RETURN)

data = [x.text for x in list(driver.find_elements_by_class_name("li")) if (x.text).contains("Check-in at")]
print(data)