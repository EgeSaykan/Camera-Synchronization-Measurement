sudo apt-get update && sudo apt-get install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

sudo apt-get update && sudo apt-get install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

sudo apt-get update
sudo apt-get install ros-iron-desktop python3-colcon-common-extensions python3-rosdep
sudo apt-get install python3-pip
pip3 install -U argcomplete

sudo apt-get install python3-opencv

sudo rosdep init
rosdep update

echo "source /opt/ros/iron/setup.bash" >> ~/.bashrc

sudo apt-get install build-essential cmake git
git clone https://github.com/EgeSaykan/MYNT-EYE-S-SDK.git
cd MYNT-EYE-S-SDK
make init
make install
make samples

sudo apt-get install ros-iron-camera-info-manager ros-iron-launch-testing-ament-cmake
cd dev_ws/src
git clone https://github.com/EgeSaykan/MYNT-EYE-S-ROS2-WRAPPER-IRON.git
git clone https://github.com/ros-perception/image_pipeline.git
cd image_pipeline
git checkout iron
cd ../../
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

