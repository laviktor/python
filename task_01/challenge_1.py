#with open('challenge_1.txt', 'w') as challenge:
#	challenge.write('A man stood over there\nQuietly in the warm sun\nBasking without care')

with open('challenge_1.txt', 'r') as file:
	print(file.read() + '\n')

#To find the number of lines - not including line breaks
lines = 0
with open('challenge_1.txt', 'r') as file:
	i = 0
	for line in file:
		if line == '\n':
			i = i + 0
		else:
			i = i + 1
	print('Lines: ' + str(i))
	lines = i

#To find the number of characters - not including line breaks
chars = 0
with open('challenge_1.txt', 'r') as file:
	j = 0
	for line in file:
		if line == '\n':
			j = j + 0
		else:
			j = j + len(line) - 1
	print('Characters: ' + str(j))
	chars = j

#To find the average characters per line - not including line breaks
print('Average characters: ' + str(chars/lines))

#to find the longest line 
with open('challenge_1.txt', 'r') as file:
	k = 0
	l = 0
	longest = 0
	for line in file:
		if (len(line)) > longest:
			longest = len(line)
			l = k
		k = k + 1
	print('Longest line: ' + str(l + 1) + ', with ' + str(longest - 1) + ' characters')