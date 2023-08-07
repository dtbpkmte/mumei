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
    pass


def terminate() -> None:
    print("Framework terminating...")
