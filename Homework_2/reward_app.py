from abc import ABC, abstractmethod
from random import randint, choices


class IGameItem(ABC):

    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):

    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):

    def open(self):
        print('Gold!')


class Gem(IGameItem):

    def open(self):
        print('Gem!')


class Muffin(IGameItem):

    def open(self):
        print('Muffin!')


class Candy(IGameItem):

    def open(self):
        print('Candy!')


class Chocolate(IGameItem):

    def open(self):
        print('Chocolate!')


class CocaCola(IGameItem):

    def open(self):
        print('Coca-cola!')


class IceCream(IGameItem):

    def open(self):
        print('Ice Cream!')


class GoldGenerator(ItemFabric):

    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):

    def create_item(self):
        return Gem()
    

class MuffinGenerator(ItemFabric):

    def create_item(self):
        return Muffin()


class CandyGenerator(ItemFabric):

    def create_item(self):
        return Candy()


class ChocolateGenerator(ItemFabric):

    def create_item(self):
        return Chocolate()


class CocaColaGenerator(ItemFabric):

    def create_item(self):
        return CocaCola()


class IceCreamGenerator(ItemFabric):

    def create_item(self):
        return IceCream()
    

if __name__ == '__main__':
    rewards = [GemGenerator(), 
               GoldGenerator(), 
               MuffinGenerator(), 
               CandyGenerator(), 
               ChocolateGenerator(), 
               CocaColaGenerator(), 
               IceCreamGenerator()]
    
    num_gold = num_gem = num_muffin = num_candy = num_chocolate = num_coca_cola = num_ice_cream = 0

    lst = [0,1,2,3,4,5,6]
    weights = [1,3,10,10,10,10,10]

    # for _ in range(5400):
    #     reward = choices(lst, weights=weights)
    #     rewards[reward[0]].create_item().open()
    #     # блок для подсчета результатов
    #     match reward[0]:
    #         case 0:
    #             num_gem += 1
    #         case 1:
    #             num_gold += 1
    #         case 2:
    #             num_muffin += 1
    #         case 3:
    #             num_candy += 1
    #         case 4:
    #             num_chocolate += 1
    #         case 5:
    #             num_coca_cola += 1
    #         case 6:
    #             num_ice_cream += 1
        
    for _ in range(5400):
        temp = randint(0, 53)
        if temp == 0:
            reward = 0
            num_gem += 1
        elif temp <= 3:
            reward = 1
            num_gold += 1
        elif temp <= 13:
            reward = 2
            num_muffin += 1
        elif temp <= 23:
            reward = 3
            num_candy += 1
        elif temp <= 33:
            reward = 4
            num_chocolate += 1
        elif temp <= 43:
            reward = 5
            num_coca_cola += 1
        else:
            reward = 6
            num_ice_cream += 1
        rewards[reward].create_item().open()
    
    # Вывод подсчета результата
    print(f"Gem = {num_gem}\n",
          f"Gold = {num_gold}\n",
          f"Muffin = {num_muffin}\n",
          f"Candy = {num_candy}\n",
          f"Chocolate = {num_chocolate}\n",
          f"Coca-cola = {num_coca_cola}\n",
          f"IceCream = {num_ice_cream}\n")

# Результат по первому методу (вызов 5400 раз)
# Gem = 95
#  Gold = 296
#  Muffin = 993
#  Candy = 971
#  Chocolate = 1005
#  Coca-cola = 1038
#  IceCream = 1002

# Результат по второму методу (вызов 5400 раз)
# Gem = 104
#  Gold = 330
#  Muffin = 1009
#  Candy = 1009
#  Chocolate = 1016
#  Coca-cola = 990
#  IceCream = 942