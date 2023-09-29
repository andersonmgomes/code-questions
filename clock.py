# Problem: Given a time, calculate the angle between the hour and minute hands.

def get_angle(hour, minutes):
    hour_angle = 30*hour + 0.5*minutes
    min_angle = 6*minutes
    angle = abs(hour_angle - min_angle)
    if angle > 180:
        angle = 360 - angle
    # else
    return angle

# test cases
print(get_angle(3, 30)) # 75
print(get_angle(12, 30)) # 165
print(get_angle(3, 15)) # 7.5
print(get_angle(12, 15)) # 82.5
print(get_angle(6, 0)) # 180
print(get_angle(9, 0)) # 90
print(get_angle(12, 0)) # 0
print(get_angle(1, 0)) # 30
print(get_angle(2, 0)) # 60