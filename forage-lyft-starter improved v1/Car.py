from abc import ABC, abstractmethod

from Serviceable import *
from Serviceable import *

class Car(ABC, Serviceable):
    
    @abstractmethod
    def needs_service(self):
        if __self__.create_calliope()==True:
            return True
        else:
            return False
