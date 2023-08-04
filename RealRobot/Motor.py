from abc import ABC, abstractmethod


class Motor(ABC):

    @abstractmethod
    def calibrate(self) -> None:
        pass

    @abstractmethod
    def move(self, val: float) -> bool:
        pass
