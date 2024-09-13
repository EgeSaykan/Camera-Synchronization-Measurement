##################################################################################

# install miricle 307k drivers on Unbuntu 22.x- T. Breckon

##################################################################################

set -e

##################################################################################

sudo cp 10-udev-local.rules /usr/lib/udev/rules.d/
sudo mkdir -p /opt/miricle/firmware/
sudo cp Miricle307.hex /opt/miricle/firmware/Miricle307.hex
sudo apt install fxload

sudo udevadm control --reload-rules 
sudo udevadm trigger

##################################################################################
