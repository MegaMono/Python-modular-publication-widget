"""
Publication Widgets
Object Oriented Programming
Due: 12/07/2025
"""

from Widget import Widget
from typing import List
import random

class Quote(Widget):
    """Quote class attributes"""
    _separator: str
    _width: int
    _quotes: List[str]
    _current_quote: str

    def __init__(self, separator: str, width: int, quote_filename: str):
        """Initialize Quote class with existing separator and width functions
        inherited from superclass"""
        super().__init__(separator, width)
        self._separator = separator
        self._width = width
        # Call read quotes method, passing it filename.
        self._quotes = self.read_quotes(quote_filename)       

    def read_quotes(self, filename: str) -> List[str]:
        """Read quotes from file, strip space and append to quotes list"""
        # Create list to store quotes.
        quotes: List[str] = []

        # Open and read file.
        with open(filename, "r") as file:
            # Iterate over lines in file, strip newlines and 
            # append to quotes list.
            for line in file:
                quote = line.strip()
                quotes.append(quote)

        return quotes        

    def update(self):
        """Update current quote using the random method to randomize
        printing of the quotes in quote list"""
        # Call super update.
        super().update
        # Randomize quotes stored in list.
        self._current_quote = random.choice(self._quotes)

    def __str__(self) -> str:
        """Inherit str functionality from superclass and 
        print current quote from this class"""
        return f"{super().__str__()}\n{self._current_quote}"
