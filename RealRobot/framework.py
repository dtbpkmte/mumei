# This file will be renamed

def setup(f_setup):
    def wrapper():
        # Pre-processing
        print("Framework terminating...")

        # User-defined setup function
        f_setup()

        # Post-processing
    return wrapper


def loop() -> None:
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("Keyboard interrupted. Exitting...")
            break


def terminate() -> None:
    print("Framework terminating...")
