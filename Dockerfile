FROM ros:noetic-ros-base

# Install basic dependencies
RUN sudo apt-get update
RUN sudo apt-get install git pip python3-catkin-tools nano -y

# Create user
RUN useradd -ms /bin/bash default

# Copy ROS code
ADD ros /home/default/ros

# Install Python requirements
WORKDIR /home/default/ros
RUN pip3 install -r requirements.txt

# Install MoveIt
WORKDIR /home/default/ros/src
RUN wstool init .
RUN wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
RUN wstool remove  moveit_tutorials
RUN wstool update -t .
RUN rosdep update
RUN rosdep install -y --from-paths . --ignore-src --rosdistro noetic

# Build packages
WORKDIR /home/default/ros
RUN catkin config --extend /opt/ros/noetic --cmake-args -DCMAKE_BUILD_TYPE=Release
RUN catkin build

USER default
WORKDIR /home/default