"""
Will Print the Top 10 On the Youtube Trending Page
"""

from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.fandango.com/11553_movietimes?mode=general&q=11553")
print(driver.title)
driver.quit()
