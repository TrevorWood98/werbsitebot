from asyncio.windows_events import NULL
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
PATH = (r"C:\Users\user\Desktop\websitebot\chromedriver.exe")

while True:
    #initializing driver variable to install chrome driver and open url link
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.website.com")

    #function that goes to element on website and clicks on element
    def gotoElement(webID):
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, webID)))
        element.click()
        time.sleep(3)



    try:
        #set the window size when opened
        driver.set_window_size(1200,1000)
        time.sleep(4)
        #we have the ID's to both vote button and submit button, which
        #is the parameter we need for our function
        gotoElement("ButtonID")
   
        gotoElement("ButtonID")    

        #delete cookies and quit the chromeDriver get request        
        driver.delete_all_cookies()
        driver.quit()

    except:
        #if any errors quit the driver and break out of while loop
        print("program exited")
        driver.quit()
        break

    time.sleep(3)
