import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtCore import Qt
from bot_app import BotApp
from GUIs.qt_factory import QtFactory
 

    
    
if __name__ == '__main__':


    # app = QApplication(sys.argv)

    # # Создание основного окна
    # mainWindow = QMainWindow()
    # mainWindow.setWindowTitle("Плавающая панель инструментов")

    # # Создание панели инструментов
    # toolBar = QToolBar("Панель инструментов", mainWindow)
    # toolBar.setFloatable(True)  # Разрешаем плавающую панель
    # mainWindow.addToolBar(toolBar)

    # # Добавление кнопок на панель инструментов
    # action1 = QAction("Действие 1", mainWindow)
    # toolBar.addAction(action1)

    # action2 = QAction("Действие 2", mainWindow)
    # toolBar.addAction(action2)

    # # Отображение основного окна
    # mainWindow.show()

    # # Запуск основного цикла приложения
    # sys.exit(app.exec_())
    qt_factory = QtFactory()
    bot_app = BotApp(qt_factory)
    #bot_app.init_selenium_driver()
    bot_app.run_gui()
    