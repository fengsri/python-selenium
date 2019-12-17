from retrying import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

@retry(stop_max_attempt_number=4)
def get_element(driver,xpath):
    """
    通过xpath获取元素
    :param driver:
    :param xpath:
    :return:
    """
    #element = driver.find_element_by_xpath(xpath)
    element = WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
    if element is not None:
        return element
    return None


def onclick_element(driver,xpath):
    """
    点击元素
    :param driver:
    :param xpath:
    """
    element = get_element(driver,xpath)
    if element is not None:
        driver.execute_script("arguments[0].click();", element)