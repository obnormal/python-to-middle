import abc
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass
class Animal:
    """Абстрактное животное"""
    name: str = ''  # имя
    legs_count: int = 0  # количество ног
    wing_exist: bool = False  # флаг, есть ли крылья или нет
    roar: str = None  # рев


class BuilderAnimal(metaclass=abc.ABCMeta):
    """Абстрактный построитель животных"""
    def __init__(self):
        self._animal = Animal()

    @abstractmethod
    def set_name(self):
        """Назначим имя животному"""
        pass

    @abstractmethod
    def set_legs_count(self):
        """Установим количество ног"""
        pass

    @abstractmethod
    def set_wing_exist(self):
        """Отметим, есть крылья или нет"""
        pass

    @abstractmethod
    def set_roar(self):
        """Установим, может ли животное говорить и что оно говорит"""
        pass

    @property
    def animal(self):
        """Получение животного"""
        return self._animal


class CatBuilder(BuilderAnimal):
    """Создание кошки"""

    def set_wing_exist(self):
        self.animal.wing_exist = False

    def set_roar(self):
        self.animal.roar = 'meow'

    def set_legs_count(self):
        self.animal.legs_count = 4

    def set_name(self):
        self.animal.name = 'cat'
    # добавьте свой код сюда


class CuckooBuilder(BuilderAnimal):
    """Создание кукушки"""

    def set_name(self):
        self.animal.name = 'cuckoo'

    def set_legs_count(self):
        self.animal.legs_count = 2

    def set_wing_exist(self):
        self.animal.wing_exist = True

    def set_roar(self):
        self.animal.roar = 'cucu'


class FishBuilder(BuilderAnimal):
    """Создание рыбы"""

    def set_name(self):
        self.animal.name = 'fish'

    def set_legs_count(self):
        pass

    def set_wing_exist(self):
        pass

    def set_roar(self):
        pass


class ZooOwner:
    """Владелец зоопарка"""
    @staticmethod
    def create_animal(builder: BuilderAnimal):
        """
            Создание животного с помощью конкретного билдера
        :param builder: билдер
        :return:
        """
        builder.set_name()
        builder.set_legs_count()
        builder.set_wing_exist()
        builder.set_roar()
