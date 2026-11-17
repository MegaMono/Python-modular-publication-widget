"""
Publication Widgets
Object Oriented Programming
Due: 12/07/2025
"""

from DateTime import DateTime
from Widget import Widget
from Quote import Quote

class Widgets():
    def main():
        """Create widget objects for testing"""
        # Initialize user input string.
        user_input = ""
   
        # DateTime class requires separator and width passed to it.
        dateTime = DateTime("#", 79)   

        # Quote class requires separator, width and filename  passed.
        quote = Quote("#", 79, "quotes.txt")

   
        # Loop until  user enters the letter "Q", case insensitive.
        while user_input.upper() != "Q":

            # Update date and time object and print.
            dateTime.update()
            print(f"{dateTime}\n")             

            # Update quote object and print.
            quote.update()
            print(f"{quote}\n")        

            # Prompt user for continuation of loop or quit to exit.
            user_input = input("Type \"Q\" to quit, enter to update the publication: ")

    main()
    #-------------------------------------------------------------#

    # Separator characters and widths for initial program testing.
    # separator1 = "$"
    # separator2 = "#"
    # separator3 = "!"
    # width1 = 1
    # width2 = 79
    # width3 = 200

    # Create a list of widgets with separator and width.
    # Commented, was just for initial testing.
    # widgets = [
    #     Widget(separator1, width1),
    #     Widget(separator2, width2),
    #     Widget(separator3, width3)        
    #     ]

    # Iterate over widgest list, update characters and print.
    # Commented out, was just for initial testing.
    # for w in widgets:
    #     w.update()
    #     print(f"{w}\n")
