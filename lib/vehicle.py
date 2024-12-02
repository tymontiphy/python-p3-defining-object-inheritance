class Vehicle:
    def __init__(self,wheel_size, wheel_number) -> None:
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
    def go(self) -> None:
        return "vrrrrrrrooom!"
    def fill_up_tank(self) -> None:
        return "filling up!"
    pass
