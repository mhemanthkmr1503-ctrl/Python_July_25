from abc import ABC, abstractmethod

class MobilePhone(ABC):
    def calc(self):
        pass

    def security(self):
        pass

    @abstractmethod
    def increase_volume(self):
        pass

    @abstractmethod
    def decrease_volume(self):
        pass
    
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

class Xiomi(MobilePhone):
    def openCamera(self):
        print("Opening the Camera")

    def closeCamer(self):
        print("Closing the Camera")

    def takePicture(self):
        print("Taking the Picure")

    def power_on(self):
        print("Welcome")

    def power_off(self):
        print("Bye")

    def increase_volume(self):
        print("Increasing the Volume")

    def decrease_volume(self):
        print("Decreasing the Volume")

mobile_phone_1 = Xiomi()
mobile_phone_1.power_on()
mobile_phone_1.openCamera()
mobile_phone_1.takePicture()
mobile_phone_1.closeCamer()
mobile_phone_1.increase_volume()
mobile_phone_1.decrease_volume()
mobile_phone_1.power_off()