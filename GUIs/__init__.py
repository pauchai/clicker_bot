from abc import ABC, abstractmethod


class AbstractGUIFactory(ABC):
    
    @abstractmethod
    def init_app(self):
        pass   
   

    @abstractmethod
    def exit_app(self, app):
        pass

    @abstractmethod
    def other(self):
        pass

    
