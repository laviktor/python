"""
Helper function to read in the input file.
"""
def read_input(filename):
  with open(filename) as file:
    return [ int(i) for i in file.readline().split(', ')]

