#!/usr/bin/python3

"""
Defines an inherited classs MyList
"""

class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
