# Challenge 3

Write a bubble sort algorithm using recursion to sort an unordered list of numbers in ascending order. The input may be provided through any form of your choice (e.g., via an argument, from input, etc.).

### How bubble sort works

Given an unordered list of numbers, you compare the first two numbers and swap them if the first number is larger than the second:
<pre>
<b>5</b>, <b>3</b>, 8, 2, 7  -->  <b>3</b>, <b>5</b>, 8, 2, 7
</pre>

Then you compare the first number to the third number and swap them if necessary, first with fourth, etc.:
<pre>
<b>3</b>, 5, <b>8</b>, 2, 7  -->  <b>3</b>, 5, <b>8</b>, 2, 7
<b>3</b>, 5, 8, <b>2</b>, 7  -->  <b>2</b>, 5, 8, <b>3</b>, 7
<b>2</b>, 5, 8, 3, <b>7</b>  -->  <b>2</b>, 5, 8, 3, <b>7</b>
</pre>

You will then move onto the second number and repeat the above process, etc.:
<pre>
2, <b>5</b>, <b>8</b>, 3, 7  -->  2, <b>5</b>, <b>8</b>, 3, 7
2, <b>5</b>, 8, <b>3</b>, 7  -->  2, <b>3</b>, 8, <b>5</b>, 7
2, <b>3</b>, 8, 5, <b>7</b>  -->  2, <b>3</b>, 8, 5, <b>7</b>
2, 3, <b>8</b>, <b>5</b>, 7  -->  2, 3, <b>5</b>, <b>8</b>, 7
2, 3, <b>5</b>, 8, <b>7</b>  -->  2, 3, <b>5</b>, 8, <b>7</b>
2, 3, 5, <b>8</b>, <b>7</b>  -->  2, 3, 5, <b>7</b>, <b>8</b>
</pre>

## Expected skills

You are expected to know the following for this task:
- Recursive functions
- Bubble sort

## Sample input

```
5, 3, 8, 2, 7
```

## Sample output

```
2, 3, 5, 7, 8
```
