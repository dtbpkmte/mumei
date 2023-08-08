from abc import ABC, abstractmethod
import math


class Encoder(ABC):
    """
    Abstract class for encoders.
    """

    @property
    def count(self) -> float:
        """
        Encoder count.
        """
        return self._count

    @property
    def prev_count(self) -> float:
        """
        Previous encoder count.
        """
        return self._prev_count

    @property
    def cpr(self) -> float:
        """
        Counts per revolution.
        TODO: update documentation about position of encoder.
        """
        return self._cpr

    def reset(self) -> None:
        """
        Resets the encoder count to 0.
        """
        self._count = 0
        self._prev_count = 0

    def get_angle_rad(self) -> float:
        """
        Unwrapped encoder angle in [rad].
        """
        return self.count / self.cpr * 2 * math.pi

    def get_angle_deg(self) -> float:
        """
        Unwrapped encoder angle in [deg].
        """
        return self.count / self.cpr * 360

    @abstractmethod
    def get_velocity(self) -> float:
        pass

    def get_velocity_rad(self) -> float:
        return self.get_velocity() / self.cpr * 2 * math.pi
