FROM moveit/moveit:noetic-release

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

USER default
WORKDIR /home/default