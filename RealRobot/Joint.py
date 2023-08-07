from Encoder import Encoder
from Motor import Motor


class Joint():
    """
    Base class that represents a 1-DoF joint. Each joint consists of a [Motor]
    and possibly an [Encoder].
    """

    def __init__(self, motor: Motor, encoder: Encoder = None):
        self._motor = motor
        self._encoder = encoder

        self._position = 0
        self._velocity = 0
        self._acceleration = 0

    def move(self, val: float):
        self._motor.move(val)

    def stop(self):
        self._motor.stop()

    def get_position(self) -> float:
        pass

    def get_velocity(self) -> float:
        pass

    def get_acceleration(self) -> float:
        pass
