# Exercise 1.26 - Grades and Points

The table below describes how the grade for a particular course is determined. Write a program that gives a course grade according to the provided table.

| points | grade       |
| ------ | ----------- |
| < 0    | impossible! |
| 0-49   | failed      |
| 50-59  | 1           |
| 60-69  | 2           |
| 70-79  | 3           |
| 80-89  | 4           |
| 90-100 | 5           |
| > 100  | incredible! |

Sample outputs:

```plaintext
Give points [0-100]:
*37*
Grade: failed
```

```plaintext
Give points [0-100]:
*76*
Grade: 3
```

```plaintext
Give points [0-100]:
*95*
Grade: 5
```

```plaintext
Give points [0-100]:
*-3*
Grade: impossible!
```
