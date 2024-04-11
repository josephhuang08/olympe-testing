import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveTo, moveBy
from olympe.enums.ardrone3.Piloting import MoveTo_Orientation_mode
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged, moveToChanged                            
from olympe.enums.ardrone3.PilotingState import MoveToChanged_Status as status                 

# IP address of the simulated drone
DRONE_IP = "10.202.0.1"
destination_latitude = 50.815018248189766 # Example latitude 50.81556186099587
destination_longitude = 12.930500297421975 # Example longitude 12.929785592382526
destination_altitude = 23 # Example altitude
#50.8147897227367, 12.93103881289524
def move(drone):
    # Take off
    assert drone(TakeOff()
          >> FlyingStateChanged(state="hovering", _timeout=10)
          ).wait().success()
    
    # Ascend to desired altitude
    result = drone(moveBy(0, 0, -23, 0)
          >> FlyingStateChanged(state="hovering", _timeout=40)
          ).wait()
    
    print("----------", result)
    assert drone(moveTo(
                    destination_latitude,
                    destination_longitude,
                    destination_altitude,
                    MoveTo_Orientation_mode.TO_TARGET,
                    0.0
                    )
                    >> moveToChanged(status=status.DONE, _timeout=1000)
                    >> FlyingStateChanged(state="hovering", _timeout=10)
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