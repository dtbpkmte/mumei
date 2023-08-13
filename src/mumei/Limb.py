from .MovingComponent import MovingComponent
from .Joint import Joint
from overrides import override
from typing import List


class Limb(MovingComponent):
    """
    A Limb contains a list of Joints.
    """

    def __init__(self):
        self._joints = []

    def add_joint(self, joint: Joint):
        self.append(joint)

    @override
    def move(self, val: List[float], *args, **kwargs) -> bool:
        ret = True
        for joint in self._joints:
            ret &= joint.move(val, *args, **kwargs)
        return ret

    @override
    def stop(self, *args, **kwargs) -> bool:
        ret = True
        for joint in self._joints:
            ret &= joint.stop()
        return ret

    def forward_kinematics(self):
        pass
