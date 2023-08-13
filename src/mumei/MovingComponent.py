from typing import List, Union
from abc import abstractmethod
from .GenericComponent import GenericComponent


class MovingComponent(GenericComponent):
    """
    API for moving components.
    """

    @abstractmethod
    def move(self, val: Union(float, List[float]), *args, **kwargs) -> bool:
        """
        Move the component by specified value(s).

        Args:
            val (float or List[float]): Movement amount.

        Returns:
            bool: True if the operation succeeded.
        """
        pass

    @abstractmethod
    def stop(self, *args, **kwargs) -> bool:
        """
        Stop the component.

        Returns:
            bool: True if the operation succeeded.
        """
        pass
