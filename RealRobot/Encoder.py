from abc import ABC, abstractmethod


class Encoder(ABC):
    """
    Abstract class for encoders.
    """

    @property
    @abstractmethod
    def count(self) -> int:
        """
        Encoder count.
        """
        return self._count

    @property
    @abstractmethod
    def prev_count(self) -> int:
        """
        Previous encoder count.
        """
        return self._prev_count

    def reset(self) -> None:
        """
        Resets the encoder count to 0.
        """
        self._count = 0
        self._prev_count = 0

    def get_count(self) -> int:
        return self._count

    @abstractmethod
    def get_velocity(self) -> float:
        pass
