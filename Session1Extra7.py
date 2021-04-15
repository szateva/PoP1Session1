# Session 1* Clock face

""" STATEMENT: Hour hand turned by A degrees since the midnight. Determine the angle by which minute
hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

For example, on input 190 output must be 120
TEMPLATE:

TESTS:
Input: 190 Output: 120
Input: 5 Output: 60
Input: 29 Output: 348
Input: 192 Output: 144 """

hour_hand_degree = float(input("How many degrees had the hour hand moved? "))
minute_hand_degree = hour_hand_degree * 12

hours_passed = minute_hand_degree // 360
current_hour_degree = hours_passed * 30
current_minute_degree = int(minute_hand_degree % 360)
print(current_minute_degree)
