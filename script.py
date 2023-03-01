from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os
from dotenv import load_dotenv

# import subprocess  -- future work to see which wifi connection connected to

#Headless Chrome so that it doesn't annoy you with a popup
from selenium.webdriver.chrome.options import Options

chrome_options=Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(0.5)

url="https://fw.bits-pilani.ac.in:8090/"

try:
    driver.get(url)
except:
    print("Error!")
    sys.exit(0)

#User credentials, please modify it according to your needs

load_dotenv()

uname=os.getenv('USERNAME')

pwd = os.getenv('PASSWORD')

#Login process
username=driver.find_element(By.ID, "username")

username.clear()

password=driver.find_element(By.ID, "password")

password.clear()

username.send_keys(uname)

password.send_keys(pwd)

driver.find_element(By.ID, "loginbtn").click()

print("Login successful!")

#closing the driver
driver.close()




