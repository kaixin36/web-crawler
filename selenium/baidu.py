from selenium import webdriver

from selenium.webdriver.common.by import By


class BaiduOperate:
    # Chrome浏览器打开百度首页
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    # 搜索框
    searchInput = driver.find_element(By.ID, "kw")
    searchInput.send_keys("刘凡")

    # 搜索内容
    searchButton = driver.find_element(By.ID, "su")
    searchButton.click()
    while True:
        b = 1


BaiduOperate.openBadu()
