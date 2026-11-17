"""
Publication Widgets
Object Oriented Programming
Due: 12/07/2025
"""

import datetime
from Widget import Widget

class DateTime(Widget):
    """DateTime attributes"""
    _separator: str
    _width: int
    _date: str
    _time: str

    def __init__(self, separator: str, width: str):
        """Initialize DateTime class object inheriting superclass initialization"""
        super().__init__(separator, width)
        self._separator = separator
        self._width = width

    def update(self):
        """Update method fetch date and time from datetime method
        split date and time for printing."""
        super().update()
        # Fetch current time from datetime method.
        date_time = str(datetime.datetime.now()) 
        # Split date time (returned as 2 parts separated by ",")
        self._date = date_time.split()[0]
        # Split time by "." to omit nanoseconds from print line.
        self._time = date_time.split()[1].split(".")[0]

    def __str__(self) -> str:
        """Inherit str from superclass, print date and time
        on separate lines."""
        return f"{super().__str__()}\n{self._date}\n{self._time}"
