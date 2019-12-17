from com.feng.util import element_util
from selenium.webdriver.common.keys import Keys


def wiki(driver):
    """
    操作wiki模块
    :param driver:
    :param xpath:
    """
    # 进入wiki模块
    element_util.onclick_element(driver,'//*[@id="item-list"]/li[4]/a')
    driver.implicitly_wait(2)

    # 获取搜索框
    search_input = element_util.get_element(driver,'//*[@id="left-side"]/div/ul/div[1]/input')

    # 输入搜索内容
    search_input.send_keys("服")

    # 按回车键
    search_input.send_keys(Keys.ENTER)
