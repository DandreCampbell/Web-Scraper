from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.fandango.com/11553_movietimes?mode=general&q=11553")
print(driver.title)

driver.quit()

"""
# Theater Name
# Path = "/html/body/main/div/section[2]/div[1]/div[7]/ul/li[1]/div[1]/div[2]"
# class = "fd-thearter__name"
"""