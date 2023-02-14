# First method: Modifying the OGS_image2SGF code.

# Given there's a black stone in that location, scan the surrounding area, if there's any spot that is
# very white, then that must be the last move
# Do the same with the white stones, if there's something around it that's very black, then that's the last move

# Second method: Use an external library to detect the hollow circles

# Without using the OGSimage2sgf, use a library to scan the image, if there's a hollow circle (either white or black)
# on it, then that's the last move.  If that image has the last move, then move that image into the front of the Anki
# card. All other images where that hollow circle isn't detected are the moved onto the back of the anki cards (answers)

# For hough circles method, you can set a maximum radius.  The hollow circle will always be smaller than the size of the
# stones, so this shouldn't be too hard... right?

