from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# Chrome浏览器打开百度首页
class BaiduOperate:

    def __init__(self):
        self.url = "https://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_by_element_Id(self):
        self.driver.get(self.url)

        # 搜索框
        search_input = self.driver.find_element(By.ID, "kw")
        search_input.send_keys("宫崎骏")

        # 搜索内容
        search_button = self.driver.find_element(By.ID, "su")
        search_button.click()
        sleep(10)

    def open_by_element_link(self):
        self.driver.get(self.url)
        # 搜索框
        search_input = self.driver.find_element(By.ID, "kw")
        search_input.send_keys("宫崎骏")

        # 搜索内容
        search_button = self.driver.find_element(By.ID, "su")
        search_button.click()
        sleep(10)

        # 点击“百度首页”(超链接)
        baidu_home_page = self.driver.find_element(By.PARTIAL_LINK_TEXT, "百度首页")
        baidu_home_page.click()
        sleep(10)
        self.driver.back()
        sleep(10)

    def open_by_element_xpath(self):
        self.driver.get(self.url)
        # 搜索框
        search_input = self.driver.find_element(By.ID, "kw")
        search_input.send_keys("宫崎骏")

        # 搜索内容
        search_button = self.driver.find_element(By.ID, "su")
        search_button.click()
        sleep(10)

        # xpath “百度首页”
        baidu_home_page = self.driver.find_element(By.XPATH, "//*[@id="u"]/a[1]")
        baidu_home_page.click()
        sleep(10)

    def save_screenshot(self):
        self.driver.get(self.url)
        # 搜索框
        search_input = self.driver.find_element(By.ID, "kw")
        search_input.send_keys("宫崎骏")

        # 搜索内容
        search_button = self.driver.find_element(By.ID, "su")
        search_button.click()
        sleep(10)
        self.driver.save_screenshot("百度截图.png")

    def login_zos(self):
        self.driver.get("http://www.zongbu.release.local/")
        sleep(10)

        # 搜索框
        userNo = self.driver.find_element(By.ID, "userName")
        userNo.send_keys("Z1211")


        password = self.driver.find_element(By.ID, "password")
        password.send_keys("zemic")
        sleep(2)

        # 搜索内容
        search_button = self.driver.find_element(By.ID, "button")
        search_button.click()
        sleep(30)
        self.driver.save_screenshot("百度截图.png")


if __name__ == "__main__":
    y = BaiduOperate()
    y.login_zos()
