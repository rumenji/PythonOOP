"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
        
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """
        Add class attributes for start and 
        keep the initial unchancged to be able to reset later
        """
        self.start = start
        self.initial = start
    
    def __repr__(self):
        """Show representation for the class"""

        return f"<SerialGenerator start={self.initial} next={self.start}>"


    def generate(self):
        """
        Return the serial number and increment start for next time
        """
        serial = self.start
        self.start += 1
        return serial
    
    def reset(self):
        """
        Reset start to the saved initial value
        """
        self.start = self.initial


