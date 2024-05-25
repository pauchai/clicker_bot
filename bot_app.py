import re
import os
import time
from selenium import webdriver
from chromedriver_py import binary_path
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from GUIs.qt_factory import QtFactory
import sys

import commands.near_commands

class BotApp:
    #driver: webdriver.remote.webdriver.WebDriver
    gui_factory: QtFactory
    webdriver: None
    def __init__(self, gui_factory: QtFactory ):
        self.gui_factory = gui_factory


    def init_selenium_driver(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--allow-profiles-outside-user-dir')
        #options.add_argument('--enable-profile-shortcut-manager')
        #options.add_argument(r'--user-data-dir=C:\Users\pauk\AppData\Local\Google\Chrome\User Data')
        #options.add_argument('--profile-directory=Profile 1')
        #options.add_argument('--headless')
        service  = webdriver.ChromeService(executable_path=binary_path)
        self.webdriver = webdriver.Chrome(service = service, options = options)  
    
    

    def run_gui(self):

        main_window = self.gui_factory.createMainWindow()
        tool_bar = self.gui_factory.createToolBar()     

        near_wallet_create = commands.near_commands.CreateWalletCommand(self)
        action1 = self.gui_factory.createAction(main_window, "Создать кошелек", near_wallet_create.execute)
        
        tool_bar.addAction(action1)
        self.init_selenium_driver()
        self.gui_factory.exec_gui()
        
        