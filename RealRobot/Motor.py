from abc import ABC, abstractmethod
import time


class Motor(ABC):
    """
    Returns the desired value that the motor wants to reach
    """

    @property
    def desired_value(self):
        return self._desired_value

    def calibrate(self) -> None:
        print("Motor %2d: Calibrating..." % self.can_id)
        self._o_drive.change_state("calib")
        time.sleep(25)  # Standard time for motor calibration
        print("Motor %2d: Done calibrating." % self.can_id)

    @abstractmethod
    def move_motor(self, val: float) -> bool:
        self._o_drive.change_state("idle")

    """
    Private method
    """

    def terminate(self) -> None:
        self._o_drive.change_state("idle")
        print("Motor %2d: Terminated." % self.can_id)
        pass

    """
    Returns true if the motor reaches the desired value
    """

    @abstractmethod
    def reach_goal(self) -> bool:
        pass

    """
        Setup the velocity and current limit for the motor => Motor is ready to use
        """

    def set_up(self, velocity_limit, current_limit):
        self._o_drive.send_cmd('Set_Controller_Mode', {
            'Input_Mode': 1, 'Control_Mode': 3})
        self._o_drive.change_state("closeloop")
        print("Entering closed loop")
        time.sleep(1)
        self._o_drive.send_cmd(
            'Set_Limits', {'Velocity_Limit': velocity_limit, 'Current_Limit': current_limit})
