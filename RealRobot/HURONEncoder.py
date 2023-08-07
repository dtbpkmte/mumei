from Encoder import Encoder
from ODrive import ODrive


class HURONEncoder(Encoder):
    """
    Implements HURON-specific encoders.
    """

    def __init__(self, odrive: ODrive):
        self._count = 0
        self._prev_count = 0
        self._cpr = 4096

        self._odrive = odrive

    @property
    def count(self) -> int:
        # reads from ODrive
        self._count = self._odrive.get_cmd(
                "Get_Encoder_Count", "Shadow_Count")
        # updates self._count
        return self._count

    def reset(self) -> None:
        # Cannot reset ODrive!!
        super().reset

    def get_velocity(self):
        # reads from ODrive
        self._count = self._odrive.get_cmd(
                "Get_Encoder_Estimates", "Vel_Estimate")
