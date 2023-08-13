from abc import abstractmethod
from .MovingComponent import MovingComponent


class Motor(MovingComponent):

    @property
    def desired_value(self) -> float:
        """
        Returns the desired value that the motor wants to reach
        """
        return self._desired_value

    @abstractmethod
    def reach_goal(self) -> bool:
        """
        Returns true if the motor reaches the desired value
        TODO: Move this method to Joint class.
        """
        pass
