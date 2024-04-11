import olympe
import os
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged

DRONE_IP = os.environ.get("DRONE_IP", "10.202.0.1")

with olympe.Drone(DRONE_IP) as drone:
    drone.connect()

    assert drone(TakeOff()
          >> FlyingStateChanged(state="hovering", _timeout=10)
          ).wait().success()

    assert drone(
        moveBy(0, 0, -8, 0)
        >> FlyingStateChanged(state="hovering", _timeout=20)
        >> moveBy(0, 0, 8, 0)
        >> FlyingStateChanged(state="hovering", _timeout=20)
    ).wait().success()

    assert drone(Landing()).wait().success()

    drone.disconnect()
