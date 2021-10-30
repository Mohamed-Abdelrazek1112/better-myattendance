from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import schedule
import time

URL = "https://my.manchester.ac.uk/MyCheckIn"


user = "##############"
pas = "###############"
path = "./chromedriver_linux64/chromedriver"

options = Options()
options.headless = False
service = Service(path)

course_schedule=[]

def signup(user,pas,driver):   
    driver.get(URL)
    username = driver.find_element(By.ID,"username")
    password = driver.find_element(By.ID,"password")

    username.clear()
    username.send_keys(user)

    password.clear()
    password.send_keys(pas)
    password.send_keys(Keys.RETURN)

def get_schedule():
    driver = webdriver.Chrome(options=options, service=service)
    signup(user,pas,driver)
    course_schedule = [x.text[:5] for x in list(driver.find_elements(By.TAG_NAME,"time")) if len(x.text) > 0]
    driver.close()

def checkin():
    driver = webdriver.Chrome(options=options, service=service)
    signup(user,pas,driver)
    driver.find_element(By.NAME,"StudentSelfCheckinSubmit").click()
    driver.close()

schedule.every().day.at("01:51").do(get_schedule)

for course_time in course_schedule:
    print(course_time)
    schedule.every().day.at(course_time).do(checkin)

while True:
    schedule.run_pending()
    time.sleep(1)
###################################################################################################

