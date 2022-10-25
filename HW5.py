print('Hello World')


"""Assume that a chooclate bar consists of n squares. Assuming that only one piece can be broken at a time. Determine how many breaks you must
successively make to have n number of breaks"""

#One break adds one more peice
breaks = 5
pieces = 1

while breaks > 0:
    pieces = pieces + 1
    print(pieces)
    breaks = breaks - 1

