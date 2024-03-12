#Author:  Vineeth Kanoor
#Date Written:  3/11/2023
# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the td banking investing page
driver.get("https://www.td.com/ca/en/investing/diy-investing")
time.sleep(3)

# Accepting Cookies permissions
cookies = driver.find_element("xpath","/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/button[2]")
cookies.click()
time.sleep(5)

# Selecting the type of investment service required
td_direct_invest = driver.find_element("xpath","/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/p/span/a")
td_direct_invest.click()
time.sleep(5)

# Clicking on get offer
get_offer = driver.find_element("xpath","/html/body/div[1]/div/main/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/a")
get_offer.click()
time.sleep(5)

# Clicking on open an account
open_account = driver.find_element("id","optBtn2")
open_account.click()
time.sleep(5)

# Clicking on box of not yet to open a new account
not_yet = driver.find_element("xpath","/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/a")
not_yet.click()
time.sleep(8)

# Selecting one checkbox in type of accounts selection
checkbox = driver.find_element("xpath","/html/body/app-root/div/section/product-selector-self-serve-view/form/app-cards/div/app-card[2]/div/div/section/div[1]/ul[1]/li[1]/div/div[1]/input")
driver.execute_script("arguments[0].click();", checkbox)
time.sleep(4)

# Click on Continue
continue_button = driver.find_element("xpath","/html/body/app-root/div/section/product-selector-self-serve-view/form/app-cards/div/app-card[3]/div/div[1]/div/button")
continue_button.click()
time.sleep(4)

# Click on continue again
continue_button = driver.find_element("xpath","/html/body/app-root/div/section/add-features-view/form/app-cards/div/app-card[3]/div/div/div/button[2]")
continue_button.click()
time.sleep(5)

# Click on top left of the page with TD Logo to redirect to Banking investing homepage
invest_home_page = driver.find_element("xpath","/html/body/app-root/div/app-header/a[1]/img")
invest_home_page.click()
time.sleep(5)

# Closing the webdriver
driver.close()
