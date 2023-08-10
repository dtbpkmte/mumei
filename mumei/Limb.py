import Joint


class Limb:
    def __init__(self):
        self.joints = []
        self.position = 0
        self.velocity = 0
        self.acceleration = 0

    def add_joint(self, joint):
        self.append(joint)

    def move_limb_by_velocity(self):
        pass

    def move_limb_to_position(self):
        pass

    def set_velocity(self, val: float):
        self.velocity = float

    def get_velocity(self) -> float:
        return self.velocity

    def forward_kinematics(self):
        pass
