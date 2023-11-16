from decimal import Decimal, getcontext
from uuid import uuid4
from datetime import datetime

from ticket import Ticket

# Для Decimal точность 2 знака после запятой
getcontext().prec = 2


class User:

    def __init__(self, name: str, login: str, password: str):
        # по логике где-то должен хранится список с Пользователями
        # и тогда необходимо добавить проверку на совпадение id_
        self.id_ = int(uuid4())
        self.name = name
        self.tickets = []
        self.login = login
        self.password_hash_code = hash(password)

    def create_account(self):
        """Создание аккаунта."""
        self.account = Account(self.id_)

    def deposit_account(self, amount: int):
        """Пополнение средств на аккаунте."""
        self.account.balance += Decimal(amount)

    def deduct_from_account(self, amount: int):
        """Списание средств с аккаунта."""
        if self.account.balance > Decimal(amount):
            self.account.balance -= Decimal(amount)
        else:
            raise "Недостаточно средств на счету!"
    
    def buy_ticket(self):
        """Покупка билета"""
        # вводим зону отправления и зону прибытия
        departure_zone = None
        arrival_zone = None
        # вызываем метод get_route_numbers и получаем список с маршрутами, временем отправлени и местами
        User.get_route_numbers(departure_zone, arrival_zone)
        # выбираем маршрут
        route_number: int = None
        # выбирает время отправления
        departure_time: datetime = None
        # выбираем место
        place: int = None
        # цена билета
        price: Decimal = None
        # списываем деньги с аккаунта
        User.deduct_from_account(price)
        # создаем билет и добавляем его в список билетов данного пользователя
        self.tickets.append(Ticket(departure_zone, 
                                   arrival_zone,
                                   route_number,
                                   departure_time,
                                   place,
                                   price))

    @staticmethod
    def get_route_numbers(departure_zone: int, arrival_zone: int):
        """По точке отправления и прибытия получаем номера маршрутов и цену билета"""
        list_route_numbers = []  # получаем какие-то маршруты (их может быть несколько)
        for _ in list_route_numbers:
            places = [] # получаем свободные места в маршруте
            if len(places) != 0:    # если список не пуст (места есть)
                list_departure_time = []    # для каждого маршрута получаем время отправления
        price: Decimal = None    # получаем цену из БД
        return list_route_numbers, price


class Account:

    def __init__(self, user_account_id: int):
        self.user_account_id = user_account_id
        self.balance = None
