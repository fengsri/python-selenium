from selenium import webdriver
from com.feng.xhrtas.login import *
from com.feng.xhrtas.wiki import *

class Rtas:
    def __init__(self) -> None:
        self.chrome_driver = rtas_const.chrome_driver

        # 无头形式运行
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=self.chrome_driver)

        # 打开本地浏览器运行
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver)
        self.driver.maximize_window()
        self.login_url = rtas_const.login_url

    def run(self):
        # 1、登录
        login(self.driver, self.login_url)

        # 2、搜索wiki
        wiki(self.driver)
