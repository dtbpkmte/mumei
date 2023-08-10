from mumei.Joint import Joint


class HURONJoint(Joint):
    """
    A revolute joint of HURON, which consists of a motor and an encoder.
    """

    # def get_position(self) -> float:
    #     return self._encoder.get_angle_rad()
    #
    # def get_velocity(self) -> float:
    #     return self._encoder.get_velocity_rad()

    def get_acceleration(self) -> float:
        pass
