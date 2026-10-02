# Week 3 Assignment - Conditions and Loops

## Files

- `grade_reporter.py` - Calculates grades, pass and fail counts, and the average score.
- `bug_hunt.py` - Fixes three bugs in a program that calculates the sum from 1 to 5.

The hardest bug to find was the loop condition in `bug_hunt.py` because it did not produce an error message. The program ran normally, but it gave the wrong answer because `count < 5` stopped the loop before 5 was added. I knew something was wrong because the required answer was 15, but the program produced a different result.