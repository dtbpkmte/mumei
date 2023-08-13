import sys
import signal


def setup(f_setup) -> None:
    def wrapper():
        # Pre-processing
        signal.signal(signal.SIGINT, terminate)
        print("MUMEI setup...")

        # User-defined setup function
        f_setup()

        # Post-processing
    return wrapper


def loop() -> None:
    while True:
        pass


def terminate() -> None:
    print("MUMEI terminating...")
    sys.exit(0)
