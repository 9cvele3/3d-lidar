# Lidar

* https://www.slamtec.com/en/Lidar/A1
* Sample rate (8000)
* Scan rate - motor pwm (2Hz - 10Hz)

# Servo

* https://www.waveshare.com/wiki/ST3215_Servo
* https://www.waveshare.com/wiki/SC15_Servo (torque 17kgcm, 180 degrees, 1024 units)

* ESP32 servo driver board is necessary to control the servo.

* Servo can be controlled in two ways:
	* Via the web app
		* WIFI pass: 12345678
		* IP addr: 192.168.4.1
		* Set it to servo mode if you want to manually change servo position => LED will confirm servo mode
		* Speed 100 is enough
	* Via python code running on Raspberry Pi
		* Raspberry Pi is connected to the ESP32 servo driver via USB (A -> C)
		* Serial forwarding must be enabled on the ESP32 servo driver (eg. via web app)
        * `watch "dmesg | tail -n30"`
		* https://www.waveshare.com/wiki/ST3215_Servo#Demo

# Raspberry PI

* Reminna - set client resolution, use FullScreen if needed

# Open3D

* Is it supported on Raspberry PI?

