

# Ros2 Linux Installation Script For Sensors



## Installation For Sensors
- Kinect v1
- Kinect v2
- MYNT EYE S
<img src="your_image_url_here" alt="MYNT EYE S" width="250" style="transform: rotate(-90deg);"/>

- Ximea Cameras
- Thermoteknix Miricle
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/MIRICLE.jpg?raw=true" alt="Thermoteknix Miricle Camera" width="250"/>

- Velodyne
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/Velodyne.jpg?raw=true" alt="Velodyne Sensor" width="250"/>




## Installation

Make a workspace to contain the drivers and packages: 
```
mkdir -p cams/dev_ws
cd cams/dev_ws
git clone https://github.com/EgeSaykan/Camera-Synchronization-Measurement.git src
cd ..
sudo sh dev_ws/src/install.sh
```


<br>
<br>

# Build
Open the terminal at dev_ws folder created and run `colcon build`.

<br>
<br>

## Configuration

Configuration file: read_bag/config/params.yaml


<br>
<br>

- **MYNT Calibration:** <br>

Show RGB video: <br>
```
  mynteye_rectification:
    ros__parameters:
      on_display: true
```
<br>

Show sterio depth video,
```
  mynteye_rectification:
    ros__parameters:
      on_display: true
```
<br>
<br>

- **Kinect v1 Calibration:** <br>

Show laser depth video: <br>
```
  kinect_show_image:
    ros__parameters:
      showImgDepth: false
```
<br>

Show rgb video,
```
  kinect_show_image:
    ros__parameters:
      showImg: true
```
<br>
<br>

- **Kinect v2 Calibration:** <br>

Show rgb video: <br>
```
  kinect_show_image:
    ros__parameters:
      showImg2: true
```
<br>

Show laser depth video,
```
  kinect_show_image:
    ros__parameters:
      showImgDepth2: false
```
<br>

Show infrared video,
```
  kinect_show_image:
    ros__parameters:
      showIR2: false
```
<br>

Sensor ID, when you run the program wi th Kinect v2 connected and it doesn't run, the sensor ID might be different. The console will show the sensor ID of detected sensors, replace this with returned value.
```
  kinect2:
    ros__parameters:
      sensor: "502596141942"
```

<br>
<br>

- **Thermoteknix Miricle Calibration:** <br>
In order to set up the thermoteknix you need to run the script found in the Thermoteknix Miricle folder. You also need the hex file with the proprietary firmware which will allow the camera to then be used as a USB camera with the ros2_usb_camera Module.
<br>
<br>

## Usage

Open the terminal at dev_ws.
Run `source install/setup.bash` to source the packages.<br>
Run `ros2 launch read_bag collective_launch.py` to launch the ros scripts.
