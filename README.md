# raspi-button
## Description:
Monitors the button on a PiCase and takes actions based on the pressed patterns.

## Table of contents:
- [History](#history)
- [Main features](#main-features)
- [Installation](#installation)

## History:
The initial idea came from using an enclosure with a "power button". The app that was supplied to manage that button was combined with a performance monitor, which not only made it bulky, and put a permanent load on the pi, but also was only available within a desktop environment.  
In the need of a lightweight and easily customisable solution, the raspi-button was born.

## Main features:
- Customisable trigger patterns
- Adaptable trigger times for long and short button presses
- Easy pattern creation and functions matching
- Integration as systemd service
- Logging via syslog

## Installation:
### Prequisits
- Python3
- gpiozero

### Locating files (only *.py and *.ini files)
The default location to place the (*.ini and *.py) files is (/root/PiCase/).  
**_Note_: If a different location is chosen this has to be adapted in raspi-button.service**

### Locating files for systemd (only *.service file)
The _raspi-button.service_ has to be placed in */etc/systemd/system/*.  
**_Note_: To trigger reboot and poweroff functions elevated privileges are needed (_default configuration_).**

 ### Activate service
`sudo systemctl enable /etc/systemd/system/raspi-button.service` # enables the service  
`sudo service raspi-button start # starts the service` # starts the service`  

## Future plans:
Depending on the overall interest the next step would be creating an installation script.
