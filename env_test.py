import olympe
import math
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged

# IP address of the simulated drone
DRONE_IP = "10.202.0.1"

def move(drone):
    # Take off
    drone(TakeOff()
          >> FlyingStateChanged(state="hovering", _timeout=5)
          ).wait()
    
    # move forward, backward, left, right, rotate.
    assert drone(moveBy(3, 0, 0, 0)
                 >> FlyingStateChanged(state="hovering", _timeout=5)
                 >> moveBy(-3, 0, 0, 0)
                 >> FlyingStateChanged(state="hovering", _timeout=5)
                 >> moveBy(0, -3, 0, 0)
                 >> FlyingStateChanged(state="hovering", _timeout=5)
                 >> moveBy(0, 3, 0, 0)
                 >> FlyingStateChanged(state="hovering", _timeout=5)
                 >> moveBy(0, 0, 0, math.pi)
                 >> FlyingStateChanged(state="hovering", _timeout=5)
                 >> moveBy(0, 0, 0, math.pi)
                 ).wait().success()

    # Land
    drone(Landing()).wait()

def main():
    # Connect to the drone
    with olympe.Drone(DRONE_IP) as drone:
        drone.connect()

        move(drone)

        drone.disconnect()

if __name__ == "__main__":
    main()