# Challenge 1

The goal of this challenge is to read an input file and print out the following stats into console:
- Total number of lines with characters (ignoring empty lines)
- Total number of characters, not counting line breaks
- Average characters per line (again, ignoring empty lines)
    - While a floating point average is preferred, an integer answer is also acceptable
- Number of characters in the longest line(s)
- Line number of the longest line
    - If more than one line tie for the longest, output the first one

If an input file does not contain any non-empty lines, then simply output "File contains no content".

## Expected skills

You are expected to utilize the following skills for this task:
- Reading files
- Simple string operations
- Simple mathematical operations
- Loops

## Sample input

```
A man stood over there
Quietly in the warm sun
Basking without care
```

## Sample output

```
Lines: 3
Characters: 65
Average characters: 21.666667 // 22 is also acceptable
Longest line: 2, with 23 characters
```

## Bonus activity

You can also optionally write the output to a file in the `output` folder.
