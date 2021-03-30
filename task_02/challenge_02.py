# string1 = input()
# list1 = list(string1)
# print('This is your string: ', string1)

# print(string1.find(' ')) - Alternatives for understanding how to go about the "space" as a method


operators = [' + ', ' - ', ' * ', ' / ']
string1 = '2 + 1'

print(string1.count(' '), 'spaces')
print('\n')

for i in range(0, len(string1)):
	print(string1[i])
	print(type(string1[i]))
