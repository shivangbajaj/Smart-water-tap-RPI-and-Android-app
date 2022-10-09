# Smart-water-tap-using-rpi-and-android-application

Smart water tap uses microprocessor i.e Rpi to control the tap(servo motor). An Android application is used to set the time which sends the data to the cloud. The could service used is Ubidots. The data is then fetched from the cloud by the RPI. Further at the particular time the tap is turned on and the ultrasonic sensor starts to take the reading. When the water is filled at a particular height the tap is turned off.

# Requirements
1. Raspberry Pi(RPI)
2. Servo Motor
3. Ultrasonic Sensor
4. Android Device

# Setup
1. Signup on Ubidots and create your variable.
2. Open .py file and add your TOKEN and the necessary values described in the file.
3. Open the app in android studio and replace the value of API and Variable name with your API and the Variable name.
4. For the connection, the pin numbers are mentioned in the file connect the servo motor and the ultrasonic sensor with RPI
5. Place the ultrasonic sensor at the edge of the bucket. (Change the value of depth in the .py file according to the size of your bucket)
5. Run the python file on RPI and use the android app to set the time.
