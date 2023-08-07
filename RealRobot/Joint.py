from enum import Enum
from Encoder import Encoder
from Motor import Motor


class JointTypes(Enum):
    REVOLUTE = 1
    PRISMATIC = 2


class Joint():
    """
    Base class that represents a 1-DoF joint. Each joint consists of a [Motor]
    and possibly an [Encoder].
    """

    def __init__(self,
                 joint_type: JointTypes,
                 motor: Motor,
                 encoder: Encoder = None):
        self._joint_type = joint_type
        self._motor = motor
        self._encoder = encoder

        self._position = 0
        self._velocity = 0
        self._acceleration = 0

    def move(self, val: float):
        self._motor.move_motor(val)

    def stop(self):
        self._motor.stop_motor()

    def get_position(self) -> float:
        """
        Joint position in [rad] for REVOLUTE joints, [m] for PRISMATIC joints.
        """
        pass

    def get_velocity(self) -> float:
        """
        Joint velocity in [rad/s] for REVOLUTE joints,
        [m/s] for PRISMATIC joints.
        """
        pass

    def get_acceleration(self) -> float:
        """
        Joint acceleration in [rad/s^2] for REVOLUTE joints,
        [m/s^2] for PRISMATIC joints.
        """
        pass
