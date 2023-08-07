from abc import ABC, abstractmethod
import math


class Encoder(ABC):
    """
    Abstract class for encoders.
    """

    @property
    def count(self) -> int:
        """
        Encoder count.
        """
        return self._count

    @property
    def prev_count(self) -> int:
        """
        Previous encoder count.
        """
        return self._prev_count

    @property
    def cpr(self) -> int:
        """
        Counts per revolution.
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
        return self.count / self.cpr * math.pi

    def get_angle_deg(self) -> float:
        """
        Unwrapped encoder angle in [deg].
        """
        return self.count / self.cpr * 180

    @abstractmethod
    def get_velocity(self) -> float:
        pass
