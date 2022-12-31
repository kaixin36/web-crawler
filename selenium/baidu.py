from selenium import webdriver

from selenium.webdriver.common.by import By


# Chrome浏览器打开百度首页
class BaiduOperate:
    url = ""

    def __init__(self):
        self.url = "https://www.baidu.com"

    def openBaidu(self):
        driver = webdriver.Chrome()
        driver.get(self.url)

        # 搜索框
        search_input = driver.find_element(By.ID, "kw")
        search_input.send_keys("宫崎骏")

        # 搜索内容
        search_button = driver.find_element(By.ID, "su")
        search_button.click()
        while True:
            b = 1


y = BaiduOperate()
y.openBaidu()
