count = 1
total = 0

# BUG: The while statement was missing a colon, so I added a colon at the end.
# BUG: The loop stopped before processing 5, so I changed < 5 to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer, so I used an f-string instead of joining it directly to a string.
print(f"Sum of 1 to 5 is: {total}")