from abc import ABC, abstractmethod
from datetime import datetime
from Serviceable import *
from Car import *


class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

class Car(ABC, Serviceable):
    
    @abstractmethod
    def needs_service(self):
        if __self__.create_calliope()==True:
            return True
        else:
            return False