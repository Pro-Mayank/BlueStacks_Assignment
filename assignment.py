import time

from selenium import webdriver
chromedriver = "F:\\chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get("https://www.game.tv/")
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
gameNames = driver.find_elements_by_css_selector("li.games-item")
print("Game Name")
for game in gameNames:
    print(game.text)


driver.close()



