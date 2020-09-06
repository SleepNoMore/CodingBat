'''
Given a number n, return True if n is in the range 1..10, inclusive.
Unless outside_mode is True,
in which case return True if the number is less or equal to 1,
or greater or equal to 10.
'''

def in1to10(n, outside_mode):
    if outside_mode:
        return n < 2 or n > 9
    else:
        return 0 < n < 11

# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True