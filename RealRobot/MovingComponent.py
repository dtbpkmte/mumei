from abc import ABC, abstractmethod


class MovingComponent(ABC):
    """
    API for moving components.
    """

    @abstractmethod
    def move(self, *args, **kwargs):
        pass

    @abstractmethod
    def stop(self, *args, **kwargs):
        pass
