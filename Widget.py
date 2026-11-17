"""
Publication Widgets
Object Oriented Programming
Due: 12/07/2025
"""

class Widget():
    """Widget attributes"""
    _separator : str
    _width : int

    def __init__(self, separator : str, width : int) -> None:
        """Initialize new Widget object, passing it values."""
        # Initialize variables for separator, and width values.
        self._separator = separator
        self._width = width

    def update(self) -> None:
        """Base update method, pass only"""
        pass

    def __str__(self) -> str:
        """Create string superclass used for printing separator characters
        in subclasses"""
        return self._separator * self._width
