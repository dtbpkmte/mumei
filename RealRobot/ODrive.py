import can
import cantools


class ODrive:
    def __init__(self, can_id: str, axis_id: int) -> None:
        # Init CAN port and store database
        self.axis = axis_id
        self.can_id = can_id
        self.database = cantools.database.load_file("odrive-cansimple.dbc")
        self._states = {"idle": 0x01, "calib": 0x03, "close-loop": 0x08}
        self.bus = can.Bus(can_id, bustype="socketcan")

    def send_cmd(self, name_of_command, cmd_input) -> None:
        msg = self.db.get_message_by_name(name_of_command)
        data = msg.encode(cmd_input)
        msg = can.Message(arbitration_id=self.axis << 5 | msg.frame_id,
                          is_extended_id=False, data=data)
        self.bus.send(msg)

    def __change_state(self, s):
        try:
            self._states[s]
        except KeyError:
            print("Motor %2d :Unknown state" + s % self.can_id)
        self._o_drive.send_cmd('Set_Axis_State',
                               {'Axis_Requested_State': self._states[s]})

    def get_cmd(self, name_of_command, cmd_input):
        msg = self.bus.recv()
        arbID = ((self.axis << 5) |
                 self.db.get_message_by_name(name_of_command).frame_id)

        while True:
            msg = self.bus.recv()
            if msg.arbitration_id == arbID:
                break
        return self.db.decode_message(name_of_command, msg.data)[cmd_input]


    """
        Setup the velocity and current limit for the motor => Motor is ready to use
    """

    def set_up(self, velocity_limit, current_limit):
        self._o_drive.send_cmd('Set_Controller_Mode', {
            'Input_Mode': 1, 'Control_Mode': 3})
        self._o_drive.change_state("closeloop")
        print("Entering closed loop")
        time.sleep(1)
        self._o_drive.send_cmd(
            'Set_Limits', {'Velocity_Limit': velocity_limit, 'Current_Limit': current_limit})

    def calibrate(self) -> None:
        print("Motor %2d: Calibrating..." % self.can_id)
        self._o_drive.change_state("calib")
        time.sleep(25)  # Standard time for motor calibration
        print("Motor %2d: Done calibrating." % self.can_id)

    """
        Private method
    """

    def terminate(self) -> None:
        self._o_drive.change_state("idle")
        print("Motor %2d: Terminated." % self.can_id)
        pass
