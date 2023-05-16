from time import sleep


def simpleCountdown(seconds, message="Waiting..."):
    """Simple countdown with message

    Args:
        seconds (int): Duration of countdown in seconds
        message (str, optional): Message of countdown. Defaults to "Waiting...".
    """
    while seconds > 0:
        print(f" [{seconds}] {message}", end='\r')
        seconds -= 1
        sleep(1)