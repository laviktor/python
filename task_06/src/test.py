from solution import find_range
from datetime import datetime, timedelta

def read_data():
  with open('./input.txt') as file:
    data = []
    for line in file.readlines():
      line = line.strip().split()
      for x in line:
        data.append(int(x))
    return data

data_set = read_data()
def test(number, low, high, expected):
  print 'Test {}: all between {} to {}'.format(number, low, high)
  start = datetime.now()
  actual = find_range(data_set, low, high)
  time = datetime.now() - start
  if time > timedelta(microseconds = 1250):
    print 'Calculation took {} seconds; needs to be 1.25 milliseconds or less'.format(time)
  elif actual != expected:
    print 'Expected: {}, Found: {}'.format(expected, actual)
  else:
    print 'Passed in {} seconds!'.format(time)
  print

test(1, -1, 1, [1])
test(2, 7, 13, [7, 9, 10, 13])
test(3, 751, 775, [753, 758, 760, 766, 770])
test(4, 999, 1000, [])
test(5, 12000, 12100, [12004, 12012, 12020, 12028, 12029, 12032, 12039, 12043, 12046, 12054, 12057, 12061, 12064, 12070, 12077, 12082, 12088, 12092, 12094])
test(6, 22152, 22157, [])
test(7, 602354, 602371, [602355, 602364, 602370])
test(8, 0, 1000000, data_set)
test(9, 602950, 602960, [602954])
test(10, 575400, 575500, [575401, 575411, 575413, 575416, 575427, 575428, 575437, 575448, 575455, 575458, 575461, 575472, 575473, 575476, 575488, 575495, 575496, 575497])
