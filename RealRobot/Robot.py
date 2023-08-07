import framework
from Limb import Limb


class Robot():
    """
    Represents a robot.
    """

    def __init__(self, limbs: Limb, *args):
        self._limbs = limbs

    @framework.setup
    def setup(self):
        for limb in self._limbs:
            limb.setup()
