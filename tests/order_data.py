from enum import Enum

class ScooterColor(Enum):
    BLACK_PEARL = 1
    GRAY_HOPELESSNESS = 2

class OrderData:
    def __init__(self, first_name, last_name, address, station_index, phone_number, date_order, period_index, scooter_color: ScooterColor, comments):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.station_index = station_index
        self.phone_number = phone_number
        self.date_order = date_order
        self.period_index = period_index
        self.scooter_color = scooter_color
        self.comments = comments
