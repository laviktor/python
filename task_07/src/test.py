from solution import lunar_add, lunar_mul

def test_add(number, x, y, expected):
  print 'Test {}.a: Calculating {} + {}'.format(number, x, y)
  actual = lunar_add(x, y)
  if actual != expected:
    print 'Expected: {}, Found: {}'.format(expected, actual)
  else:
    print 'Correct!!'

def test_mul(number, x, y, expected):
  print 'Test {}.b: Calculating {} x {}'.format(number, x, y)
  actual = lunar_mul(x, y)
  if actual != expected:
    print 'Expected: {}, Found: {}'.format(expected, actual)
  else:
    print 'Correct!!'

def test(number, x, y, expected_a, expected_b):
  test_add(number, x, y, expected_a)
  test_mul(number, x, y, expected_b)
  print

test(1, 123, 45, 145, 1233)
test(2, 357, 64, 367, 3564)
test(3, 13579, 8642, 18679, 13578642)
test(4, 5, 472749, 472749, 452545)
test(5, 0, 368, 368, 0)