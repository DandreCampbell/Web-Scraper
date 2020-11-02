"""
Will Print the Top 10 On the Youtube Trending Page
"""

from selenium import webDriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Firefox(PATH)

driver.get("https://www.youtube.com/feed/trending")
print(driver.title)
driver.quit()
