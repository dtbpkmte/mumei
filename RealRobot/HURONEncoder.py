from Encoder import Encoder
from ODrive import ODriveController


class HURONEncoder(Encoder):
    """
    Implements HURON-specific encoders.
    """

    def __init__(self, odrive: ODriveController):
        self._count = 0
        self._prev_count = 0
        self._cpr = 4096

        self._odrive = odrive

    @property
    def count(self) -> float:
        # reads from ODrive
        # self._count = self._odrive.get_cmd(
        #         "Get_Encoder_Count", "Shadow_Count")
        self._count = self._odrive.get_cmd(
                "Get_Encoder_Estimates", "Pos_Estimate") * self._cpr
        # updates self._count
        return self._count

    def reset(self) -> None:
        # Cannot reset ODrive!!
        super().reset()

    def get_velocity(self):
        # reads from ODrive
        return self._odrive.get_cmd(
                "Get_Encoder_Estimates", "Vel_Estimate") * self._cpr
