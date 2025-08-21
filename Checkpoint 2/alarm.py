def main():
    is_armed = True
    motion_detected = True
    door_open = False
    is_afternoon = True
    display_alarm(is_armed, motion_detected, door_open, is_afternoon)

def display_alarm(iar, ms, dop, an):
    if iar:
        if ms:
            print("There is motion detected at the front door")
        if dop:
            print("door is open")
    else: 
        if an:
            print("Welcome home! Turning on the light")

main()