from abc import ABC, abstractmethod


class GenericComponent(ABC):
    """
    API for robot components.
    """

    @abstractmethod
    def configure(self, *args, **kwargs):
        pass

    @abstractmethod
    def set_up(self, *args, **kwargs):
        pass

    @abstractmethod
    def terminate(self, *args, **kwargs):
        pass
