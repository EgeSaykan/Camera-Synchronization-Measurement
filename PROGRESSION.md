
# My Progression On Sensors I Worked With For This Project

## SICK LD-MRS 400001
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/SINK.jpg?raw=true" alt="SICK Sensor" width="250"/>

<br>

### Sensor Info

LD-MRS 400001 is an lidar sensor that can detect objects up to 50m very accurately, and up to 320m less accurately.

For more information about specifications please see [this link](https://cdn.sick.com/media/pdf/5/55/355/dataSheet_LD-MRS400001_1045046_en.pdf).

<br>

### My Progression On Sensor

The sensor uses 9V-27V for power and connects via ethernet. I powered up the sensor with a switching mode power supply and connected to a Linux machine.

The machine did not recognise the ethernet connection to be connected so I set the IP address manually which completed the connection.

## Unsupported Cameras

### Progression with Point Grey Research / Firefly Cameras

The cameras use IEEE1394 standard for data transmission from the camera, I was unable to get them to work within Ubuntu 22.04.4
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/Firefly.jpg?raw=true" alt="Firefly Camera" width="250"/>
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/Point%20Grey.jpg?raw=true" alt="Point Grey Camera" width="250"/>

### Creative TOF cameras

I could not get the creative TOF cameras to work. They require a specific SDK in order to interact with however the website from the company that distributes the SDK is inaccessable as the company has since been bought out by sony. I have sent an email to the company asking if I could have access to the SDK or if they knew somewhere I would be able to access it, but I am yet to recieve a response
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/Creative1.jpg?raw=true" alt="Creative Camera" width="250"/>
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/Creative2.jpg?raw=true" alt="Creative Camera" width="250"/>
<img src="https://github.com/EgeSaykan/Camera-Synchronization-Measurement/blob/main/docs/Creative3.jpg?raw=true" alt="Creative Camera" width="250"/>

### Here 3 GPS

I started working with the here3 gps but could not find a good ros2 driver
