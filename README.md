# Smart-water-tap-using-rpi-and-android-application

The Smart Water Tap project employs a combination of hardware and software to create an efficient and automated water management system. At the heart of this system is a Raspberry Pi, which serves as the central microprocessor controlling the tap's servo motor. The servo motor enables precise control over the tap's opening and closing mechanisms.

Users interact with the system through an Android application, which allows them to schedule when the tap should be turned on. The application sends this scheduling data to the cloud service Ubidots, which acts as an intermediary, ensuring that the Raspberry Pi receives the correct information. When the designated time arrives, the Raspberry Pi fetches the data from Ubidots and activates the tap.

Simultaneously, an ultrasonic sensor begins monitoring the water level in the container. As the water fills the container, the sensor continuously measures the height of the water. Once the water reaches a pre-defined level, the Raspberry Pi signals the servo motor to turn off the tap, preventing overflow and conserving water. This integration of cloud computing, mobile technology, and sensor data ensures that water is dispensed efficiently and sustainably.

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
