# Task 10. Determining time by angle
# Enter the angle (0–360) by which the minute hand of the clock is turned.
# Determine how many minutes it is now.

angle_rotation_minute_hand = int(
    input("Enter the angle (0–360) by which the minute hand of the clock is turned: ")
)

number_of_minutes = angle_rotation_minute_hand / 6

print(
    f"When the minute hand is turned at an angle of {angle_rotation_minute_hand} degrees, "
    f"the clock shows {int(number_of_minutes)} minutes"
)
