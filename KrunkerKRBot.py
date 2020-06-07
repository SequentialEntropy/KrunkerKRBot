from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from webdriver_manager.chrome import ChromeDriverManager

import datetime
import os
import time

class KRBot():
    def __init__(self):

        # self.driver = webdriver.Chrome(ChromeDriverManager("83.0.4103.39").install())
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ["GOOGLE_CHROME_BIN"]
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(os.environ["CHROMEDRIVER_PATH"], options=chrome_options)
        self.username = os.environ["USERNAME"]
        self.password = os.environ["PASSWORD"]
        self.maxattempts = int(os.environ["MAX_ATTEMPTS"])
        self.timeout = int(os.environ["TIMEOUT"])
        self.driver.get("https://krunker.io")


    def AcceptCookies(self):
        result = "(Accept Cookies) - All Attempts Failed"
        for attempt in range(self.maxattempts):
            try:
                element = self.driver.find_element_by_xpath("//*[contains(text(), 'Accept')][@class='termsBtn']")
                result = element.click()
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Accept Cookies) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Accept Cookies) - Exception Caught: " + str(e))
        return result

    def Login(self):
        result = "(Login Menu) - All Attempts Failed"
        for attempt in range(self.maxattempts):
            try:
                element = self.driver.find_element_by_xpath("//*[contains(text(), 'Login')][@class='button lgn']")
                result = element.click()
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Login Menu) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Login Menu) - Exception Caught: " + str(e))
        if result != None:
            return result
        
        result = "(Username Field) - All Attempts Failed"
        for attempt in range(self.maxattempts):
            try:
                element = self.driver.find_element_by_xpath("//*[@id='accName']")
                result = element.send_keys(self.username)
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Username Field) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Username Field) - Exception Caught: " + str(e))
        if result != None:
            return result

        result = "(Password Field) - All Attempts Failed"
        for attempt in range(self.maxattempts):
            try:
                element = self.driver.find_element_by_xpath("//*[@id='accPass']")
                result = element.send_keys(self.password)
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Password Field) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Password Field) - Exception Caught: " + str(e))
        if result != None:
            return result

        result = "(Send Login Credentials) - All Attempts Failed"
        for attempt in range(self.maxattempts):
            try:
                element = self.driver.find_element_by_xpath("//*[contains(text(), 'Login')][@class='accountButton']")
                result = element.click()
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Send Login Credentials) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Send Login Credentials) - Exception Caught: " + str(e))
        return result

    def Claim(self):
        result = "(Claim Button) - All Attempts Failed"
        for attempt in range(self.maxattempts):
            try:
                element = self.driver.find_element_by_xpath("//*[@id='claimHolder']")
                result = element.click()
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Claim Button) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Claim Button) - Exception Caught: " + str(e))
        if result != None:
            return result

        result = "(Spin Button) - Timed Out"
        for attempt in range(self.timeout):
            try:
                element = self.driver.find_element_by_xpath("//*[@id='spinButton']")
                result = element.click()
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Spin Button) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result == None:
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Spin Button) - Exception Caught: " + str(e))
            time.sleep(1)
        if result != None:
            return result

        result = "(Spin Item Name) - Timed Out"
        for attempt in range(self.timeout):
            try:
                element = self.driver.find_element_by_xpath("//*[@id='spinItemName']")
                result = element.text
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Spin Item Name) - Returned: " + str(result) + " - Attempt: " + str(attempt))
                if result != "":
                    break
            except Exception as e:
                timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("[" + timenow + "] (Spin Item Name) - Exception Caught: " + str(e))
            time.sleep(1)
        return result

    def Quit(self):
        self.driver.quit()

    def Run(self):
        print(str(self.AcceptCookies()))
        print(str(self.Login()))
        print(str(self.Claim()))
        print(str(self.Quit()))

bot = KRBot()
bot.Run()
