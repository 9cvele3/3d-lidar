# Lidar

# Servo
* https://www.waveshare.com/wiki/ST3215_Servo

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
		* https://www.waveshare.com/wiki/ST3215_Servo#Demo

