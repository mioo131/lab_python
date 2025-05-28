from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def inscribed_circle_radius(self) -> float:
        pass

    @abstractmethod
    def circumscribed_circle_radius(self) -> float:
        pass

    def __str__(self):
        return f"Shape: {self.__class__.__name__}"
