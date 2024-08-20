# ROS2_Pick_and_Place
ROS2 Package to simulate pick and place task using Franka Panda Robot Arm in Rviz and Gazebo
## Prerequisites
Ubuntu with compatible ROS2 distro, Moveit2, and Gazebo installed. If required, find the links below to install ROS2 and Moveit2

## Installation
### ROS2
To install ROS2, please follow the instructions listed in the link: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

**Note: The link provided above directs you to installation page of ROS2 Humble distro. Please choose the ROS2 distro that is available and supported in your Ubuntu verison. Ubunut 20.04 with ROS2 Humble is used in this project to develop the ROS2_Pick_and_Place package**

### MoveIt2
To install MoveIt2, please follow the instructions listed in the link: https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html

**Note: At the time of writing, MoveIt2 only released stable versions untill ROS2 Iron. Latest ROS2 version Jazzy still doesn't have a stable release. Therefore, choose the MoveIt2 version carefully based on your ROS2 distro. The link provided above is for Humble distro**

**While installing MoveIt2 from the source, if the build process fails using the `colcon build --mixin release` command mentioned in the above link, use the command `colcon build --mixin release --executor sequential --parallel-workers 1` to successfully build MoveIt2. This command is useful if you are using a Virtual Machine or a device with low capability**

### ROS2_Pick_and_Place Package installation
To install the pick and plcae package, clone the repository into the same workspace you have created and cloned MoveIt2 into. Change the directory to that location on your CLI
```
~/ws_moveit/src/
```

Clone the ROS2 package using the command below:
```
git clone https://github.com/aganirudh06/ROS2_Pick_and_Place.git
```

Aft successful clone of the ROS2 package into the same wokspace as MoveIt2, build the package
```
colcon build --packages-select mtc_tutorial
```

The ROS2 package is ready to use and the launch files can be used to run te Pick and Place simulation in Rviz and Gazebo

## Launching the simulation

Firstly, source the setup script of the wokspace in the Terminal tab you are going to run the launch files from and the setup script of ROS to run ROS package

```
source ~/ws_moveit/install/setup.bash
source /opt/ros/humble/setup.bash
```

Launch the rviz simulation with the Panda robot arm
```
ros2 launch moveit2_tutorials mtc_demo.launch.py
```

Now, Launch the Gazebo simulation
```
ros2 launch mtc_tutorial spawn_panda.launch.py
```

Finally, run the simulation of pick and place sequence
```
ros2 launch mtc_tutorial pick_place_demo.launch.py
```
