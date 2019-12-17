from com.feng.util import element_util
from com.feng.const import rtas_const

def login(driver,url):
    """
    登录操作
    :param driver:
    :param url:
    """
    # 发送首页
    driver.get(url)

    # 点击登录
    element_util.onclick_element(driver,"//*[@id='app']/div/div/div[1]/div/ul/li/a")

    # 获取当前页面的用户名、密码输入框
    driver.implicitly_wait(2)
    user_name = element_util.get_element(driver,"//*[@id='app']/div/section/div/div/form/div[1]/div/div/input")
    user_password = element_util.get_element(driver,'//*[@id="app"]/div/section/div/div/form/div[2]/div/div/input')

    # 输入用户名、用户密码
    user_name.send_keys(rtas_const.user_name)
    user_password.send_keys(rtas_const.user_password)

    # 点击登录
    element_util.onclick_element(driver,'//*[@id="app"]/div/section/div/div/form/div[3]/div/button')
    driver.implicitly_wait(2)

