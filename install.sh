
# install mynt sdk
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
cd .. # path: cams/


# install mynt wrapper
sudo apt-get install ros-iron-camera-info-manager ros-iron-launch-testing-ament-cmake
cd dev_ws/src       # path: cams/dev_ws/src
git clone https://github.com/EgeSaykan/MYNT-EYE-S-ROS2-WRAPPER-IRON.git
git clone https://github.com/ros-perception/image_pipeline.git
cd image_pipeline   # path: cams/dev_ws/src/image_pipeline
git checkout iron 
cd ../../../        # path: cams/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib


# install libreenect (kinect v1 sdk) 
git clone https://github.com/OpenKinect/libfreenect
cd libfreenect
mkdir build
cd build
cmake -L ..
make

cmake .. -DBUILD_PYTHON3=ON
make

sudo apt-get install git cmake build-essential libusb-1.0-0-dev

cd ../../   # path: cams/


# download libreenect2 (kinect v2 sdk)
git clone https://github.com/OpenKinect/libfreenect2.git
cd libfreenect2
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libusb-1.0-0-dev
sudo apt-get install libturbojpeg0-dev
sudo apt-get install libglfw3-dev
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/freenect2
make
make install
cmake -Dfreenect2_DIR=$HOME/freenect2/lib/cmake/freenect2
sudo cp ../platform/linux/udev/90-kinect2.rules /etc/udev/rules.d/
cd ../../   # path: cams/


# install kinect v2 wrapper
cd dev_ws/src/
git clone https://github.com/YuLiHN/kinect2_ros2
cd kinect2_ros2
rosdep install -r --from-paths .
cd ../.. # path: cams/dev_ws

#XiAPI install
wget https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz
tar xzf XIMEA_Linux_SP.tgz
cd package
./install
cd ..

#Ximea ros2 driver install
git clone https://github.com/African-Robotics-Unit/ximea_ROS2_driver.git
cd /ximea_ROS2_driver
colcon build --packages-select ximea_ros2_cam
cd ..

# velodyne install
sudo apt search ros-iron-velodyne
sudo apt install ros-iron-velodyne-driver

# usb camera install
git clone https://github.com/klintan/ros2_usb_camera.git
cd ros2_usb_camera
colcon build
cd ..


