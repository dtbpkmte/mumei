import Motor
import can


class TorqueMotor(Motor):
    """
    Initialization to start reading the motor
    """

    def __init__(self, odrive):
        # Init CAN port and store database
        self._desired_value = 0
        self._o_drive = odrive

    def move_motor(self, goal: float) -> bool:
        print("Motor %2d: Setting torque to %f" % (self.can_id, goal))
        self._desired_value = goal
        self.change_state("idle")
        msg = self.db.get_message_by_name('Set_Input_Pos')
        data = msg.encode({'Input_Pos': 0, 'Vel_FF': 0, 'Torque_FF': goal})
        msg = can.Message(arbitration_id=self.axis << 5 | msg.frame_id, data=data, is_extended_id=False)
        self.bus.send(msg)

    """
    Returns true if the motor reaches the desired value
    """

    def reach_goal(self, print_value) -> bool:
        threshold = 0.6
        msg = self.bus.recv()
        arbID = ((self.axis << 5) | self.db.get_message_by_name(
            'Get_Encoder_Estimates').frame_id)
        if msg.arbitration_id == arbID:
            pos = self.db.decode_message('Get_Encoder_Estimates', msg.data)[
                'Pos_Estimate']
            vel = self.db.decode_message('Get_Encoder_Estimates', msg.data)[
                'Vel_Estimate']
            tor = pos * vel  # TODO: fix this, temp only
            if self.axis > -1:
                if print_value:
                    print("Axis")
                    print(self.axis)
                    print("Desired Torque")
                    print(self.desired_value)
                    print("Current Torque")
                    print("IDK calculate from velocity and pos ?!?")
                    print("Error")
                    print(abs(pos - self.desired_pos))
                    print("")
            return abs(tor - self.desired_value) <= threshold  # TODO:change this to torque
        return False
