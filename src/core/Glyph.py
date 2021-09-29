from abc import ABC, abstractmethod


class Glyph(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def intersection(self):
        pass

    @abstractmethod
    def insert(self):
        pass
