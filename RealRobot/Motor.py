from abc import ABC, abstractmethod
import time


class Motor(ABC):
    """
    Returns the desired value that the motor wants to reach
    """

    @property
    def desired_value(self):
        return self._desired_value

    @abstractmethod
    def move_motor(self, val: float) -> bool:
        pass

    """
    Returns true if the motor reaches the desired value
    """

    @abstractmethod
    def reach_goal(self) -> bool:
        pass
