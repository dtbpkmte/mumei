import framework
from ODrive import ODrive
from Robot import Robot
from Joint import JointTypes
from HURONJoint import HURONJoint
from TorqueMotor import TorqueMotor
from HURONEncoder import HURONEncoder
import time


if __name__ == '__main__':
    # Parameters
    velocity_limit = 15.0
    current_limit = 70.0

    # ODrives
    left_hip_pitch_od = ODrive("can0", 0x1)
    left_knee_pitch_od = ODrive("can0", 0x0)
    right_hip_pitch_od = ODrive("can1", 0x7)
    right_knee_pitch_od = ODrive("can1", 0x6)

    # Motors
    left_hip_pitch_motor = TorqueMotor(left_hip_pitch_od)
    left_knee_pitch_motor = TorqueMotor(left_knee_pitch_od)
    right_hip_pitch_motor = TorqueMotor(right_hip_pitch_od)
    right_knee_pitch_motor = TorqueMotor(right_knee_pitch_od)

    # Encoders
    left_hip_pitch_enc = HURONEncoder(left_hip_pitch_od)
    left_knee_pitch_enc = HURONEncoder(left_knee_pitch_od)
    right_hip_pitch_enc = HURONEncoder(right_hip_pitch_od)
    right_knee_pitch_enc = HURONEncoder(right_knee_pitch_od)

    # Joints
    left_hip_pitch_joint = HURONJoint(
        JointTypes.REVOLUTE, left_hip_pitch_motor, left_hip_pitch_enc)
    left_knee_pitch_joint = HURONJoint(
        JointTypes.REVOLUTE, left_knee_pitch_motor, left_knee_pitch_enc)
    right_hip_pitch_joint = HURONJoint(
        JointTypes.REVOLUTE, right_hip_pitch_motor, right_hip_pitch_enc)
    right_knee_pitch_joint = HURONJoint(
        JointTypes.REVOLUTE, right_knee_pitch_motor, right_knee_pitch_enc)

    # Calibrate ODrives
    print("Calibrating...")
    left_hip_pitch_od.calibrate()
    right_knee_pitch_od.calibrate()
    left_knee_pitch_od.calibrate()
    right_hip_pitch_od.calibrate()

    print("Setting up...")
    left_hip_pitch_od.set_up(velocity_limit, current_limit)
    left_knee_pitch_od.set_up(velocity_limit, current_limit)
    right_hip_pitch_od.set_up(velocity_limit, current_limit)
    right_knee_pitch_od.set_up(velocity_limit, current_limit)

    # robot = Robot()
    # robot.setup()

    # Move right knee
    print(f"Left knee: {left_knee_pitch_joint.get_position()} rad")

    print("Moving joint...")
    left_knee_pitch_joint.move(5)

    time.sleep(2)

    print("Stopping joint...")
    left_knee_pitch_joint.stop()

    print("Terminating joint...")
    left_knee_pitch_od.terminate()

    print(f"Left knee: {left_knee_pitch_joint.get_position()} rad")

    while True:
        framework.loop()

    framework.terminate()
