import keyboard
import olympe
import os
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, PCMD
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
'''
PCMD command is used to implement a contoller, it contols the drone to roll, pitch, yaw or gaz.
The function takes 6 parameters flag, roll, pitch, yaw, gaz, timestampAndSeqNum.
flag: 1 if the roll and pitch values should be taken in consideration. 0 otherwise.
timestampAndSeqNum: for debuggeing perposes.
'''

DRONE_IP = os.environ.get("DRONE_IP", "10.202.0.1") 

def start_control(drone):
    print("\n----------start piloting the drone----------\n")
    while True:
        # Wait for a key to be pressed
        key_pressed = keyboard.read_key()

        # Perform actions based on the pressed key
        if key_pressed == 't': # takeoff
            assert drone(TakeOff()).wait().success()

        elif key_pressed == 'q': # yaw counter-clockwise
            assert drone(PCMD(0, 0, 0, -100, 0, 0)).wait().success()

        elif key_pressed == 'e': # yaw clockwise
            assert drone(PCMD(0, 0, 0, 100, 0, 0)).wait().success()

        elif key_pressed == 'w': # forward
            assert drone(PCMD(1, 0, 100, 0, 0, 0)).wait().success()

        elif key_pressed == 'a': # left
            assert drone(PCMD(1, -100, 0, 0, 0, 0)).wait().success()
            
        elif key_pressed == 's': # backward
            assert drone(PCMD(1, 0, -100, 0, 0, 0)).wait().success()

        elif key_pressed == 'd': # right
            assert drone(PCMD(1, 100, 0, 0, 0, 0)).wait().success()

        elif key_pressed == 'ctrl': # down
            assert drone(PCMD(0, 0, 0, 0, -100, 0)).wait().success()

        elif key_pressed == 'space': # up
            assert drone(PCMD(0, 0, 0, 0, 100, 0)).wait().success()

        elif key_pressed == 'esc': # exit
            print("\n----------drone will start to land----------\n")
            break  
        else:
            print(f"The '{key_pressed}' key was pressed, but no action is defined for it.")


def main():
    # Connect to the drone
    with olympe.Drone(DRONE_IP) as drone:
        drone.connect()
        start_control(drone)
        assert drone(Landing()).wait().success()
        drone.disconnect()

if __name__ == "__main__":
    main()