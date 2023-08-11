from abc import ABC, abstractmethod


class GenericComponent(ABC):
    """
    API for robot components.
    """

    @abstractmethod
    def configure(self, *args, **kwargs) -> None:
        """
        Configure the component.
        """
        pass

    @abstractmethod
    def initialize(self, *args, **kwargs) -> None:
        """
        Initialize the component.
        """
        pass

    @abstractmethod
    def set_up(self, *args, **kwargs) -> None:
        """
        Set up the component.
        """
        pass

    @abstractmethod
    def terminate(self, *args, **kwargs) -> None:
        """
        Terminate the component.
        """
        pass
