import framework
from Robot import Robot


if __name__ == '__main__':
    robot = Robot()
    robot.setup()

    while True:
        framework.loop()

    framework.terminate()
