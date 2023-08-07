from Joint import Joint


class HURONJoint(Joint):
    """
    Base class that represents a 1-DoF joint. Each joint consists of a [Motor]
    and possibly an [Encoder].
    """

    def get_position(self) -> float:
        return self._encoder.get_angle_rad()

    def get_velocity(self) -> float:
        return self._encoder.get_velocity() / self._encoder.cpr

    def get_acceleration(self) -> float:
        pass
