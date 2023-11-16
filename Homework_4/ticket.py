from decimal import Decimal, getcontext
from uuid import uuid4
from datetime import datetime

# Для Decimal точность 2 знака после запятой
getcontext().prec = 2


class Ticket:

    def __init__(self, id_: int, 
                 departure_zone: int, 
                 arrival_zone: int, 
                 route_number: int, 
                 departure_time: datetime, 
                 place: str, 
                 price: Decimal):
        # по логике где-то должен хранится список всех билетов всех пользователей
        # и тогда необходимо добавить проверку на совпадение id_
        self.id_ = int(uuid4())
        self.departure_zone = departure_zone    # зона отправления
        self.arrival_zone = arrival_zone    # зона прибытия
        self.route_number = route_number    # маршрут
        self.departure_time = departure_time    # время отправления
        self.arrival_time = Ticket.get_arrival_time()   # время прибытия
        self.is_used = False # флаг использовался ли билет
        self.place = place   # местов автобусе
        self.price = price   # цена

    def get_arrival_time(self):
        # по номеру маршрута и времени отправления
        # self.route_number
        # self.departure_time
        self.arrival_time = None    # присваиваем какое-то значение из БД
    
    def set_is_used(self):
        """Если билет использовался, то is_used устанавливаем в True"""
        self.is_used = True
