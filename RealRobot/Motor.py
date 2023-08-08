from abc import ABC, abstractmethod


class Motor(ABC):

    @property
    def desired_value(self) -> float:
        """
        Returns the desired value that the motor wants to reach
        """
        return self._desired_value

    @abstractmethod
    def configure(self, *args, **kwargs) -> bool:
        """
        Configure the motor.
        """
        pass

    @abstractmethod
    def set_up(self, *args, **kwargs) -> None:
        """
        Puts the motor into ready-to-run mode.
        """
        pass

    @abstractmethod
    def move_motor(self, val: float) -> bool:
        pass

    @abstractmethod
    def stop_motor(self) -> bool:
        pass

    """
    Returns true if the motor reaches the desired value
    """

    @abstractmethod
    def reach_goal(self) -> bool:
        pass
