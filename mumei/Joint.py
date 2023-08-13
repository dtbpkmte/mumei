from enum import Enum
from MovingComponent import MovingComponent
from Encoder import Encoder
from Motor import Motor


class JointTypes(Enum):
    REVOLUTE = 1
    PRISMATIC = 2


class Joint(MovingComponent):
    """
    Base class that represents a 1-DoF joint. Each joint consists of a [Motor]
    and possibly an [Encoder].
    """

    def __init__(self,
                 joint_type: JointTypes,
                 motor: Motor,
                 encoder: Encoder = None,
                 gear_ratio_1: float = 1,
                 gear_ratio_2: float = 1):
        self._joint_type = joint_type
        self._motor = motor
        self._encoder = encoder
        self._gear_ratio_1 = gear_ratio_1
        self._gear_ratio_2 = gear_ratio_2

        self._position = 0
        self._velocity = 0
        self._acceleration = 0

    def move(self, val: float, *args, **kwargs):
        self._motor.move_motor(val)

    def stop(self, *args, **kwargs):
        self._motor.stop_motor()

    def get_position(self) -> float:
        """
        Joint position in [rad] for REVOLUTE joints, [m] for PRISMATIC joints.
        """
        # TODO: move this to a separate RevoluteJoint class
        return self._encoder.get_angle_rad() / self._gear_ratio_1 / \
            self._gear_ratio_2

    def get_velocity(self) -> float:
        """
        Joint velocity in [rad/s] for REVOLUTE joints,
        [m/s] for PRISMATIC joints.
        """
        # TODO: move this to a separate RevoluteJoint class
        return self._encoder.get_velocity_rad() / self._gear_ratio_1 / \
            self._gear_ratio_2

    def get_acceleration(self) -> float:
        """
        Joint acceleration in [rad/s^2] for REVOLUTE joints,
        [m/s^2] for PRISMATIC joints.
        """
        pass
