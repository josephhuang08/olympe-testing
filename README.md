# olympe-testing
This repository contains a set of Python scripts for testing drone functionalities using the [Olympe SDK](https://developer.parrot.com/docs/olympe/index.html)  . The scripts are designed to interact with a simulated drone and perform various maneuvers to validate different aspects of the drone's behavior.

- **env_empty.py:** Performs basic operations such as takeoff, fly up, fly down, and landing.
- **env_test.py:** This script tests the drone's movement capabilities in different directions. It performs movements forward, backward, left, right, and rotation.
- **env_planet.py:** This script is testing in the [parrot-ue4-planet](https://developer.parrot.com/docs/sphinx/world_planet.html) enviroment. It simulates a scenario where the drone takes off, moves to a specified GPS location, and then lands.
- **pilot_via_keyboard.py:** This script make use of pitch, roll, yaw commands to implements a keyboard controller to control the drone.  
- **record_video.py:**  
   - Records the streaming video of the drone's camera.
   - Opens up a HUD to show the steaming of camera.
   - After flight, .mp4 file will be saved to the current directory.
   - Notes: when recording the downward-facing camera, the quality is not good and when playback .mp4 file sometimes will crash for some unknown reason.
