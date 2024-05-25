from . import AbstractGUIFactory
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtCore import Qt
import sys


#import commands.near_commands


class QtFactory():
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = None    


    def createMainWindow(self):
        self.main_window = QMainWindow()
        self.main_window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.main_window.setWindowTitle("Плавающая панель инструментов")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Устанавливаем размеры и положение окна
        window_width = screen_geometry.width()
        window_height = 50  # Высота панели инструментов
        self.main_window.setGeometry(0, screen_geometry.height() - window_height, window_width, window_height)


        return self.main_window

    def createToolBar(self):
        tool_bar = QToolBar("Панель инструментов", self.main_window)
        #tool_bar.setFloatable(True)  # Разрешаем плавающую панель
        self.main_window.addToolBar(tool_bar)
        return tool_bar

    def createAction(self, parent, text, callback):
        action = QAction(text, parent)
        action.triggered.connect(callback)
        return action

    def getApp(self):
        return self.app  # Возвращаем созданный QApplication

    def exec_gui(self):
        if self.main_window is None:
            raise RuntimeError("Main window not created. Call createMainWindow() first.")

        self.main_window.show()
        return sys.exit(self.app.exec_())  # Запускаем цикл обработки событий Qt и возвращаем код завершения

    
    
