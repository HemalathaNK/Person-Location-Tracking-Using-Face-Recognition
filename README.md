# Person Location Tracking Using Face Recognition

## Overview
This project implements a facial recognition-based person location tracking system. It uses Python for the backend and HTML/CSS for the frontend. The system captures and processes video from cameras, identifies individuals using facial recognition, and logs attendance data in a MySQL database.

## Technologies Used
* __Backend:__ Python
* __FrontEnd:__ HTML, CSS
* __Database:__ MySQL (via XAMPP)
* __IDE:__ VS Code

## Requirements

### Software
* __VS Code:__ For coding and development
* __DroidCam:__ To use a mobile device as an external camera
     * [DroidCam Client for Laptop](https://www.dev47apps.com/droidcam/windows/)
     * DroidCam app for mobile (available on respective app stores)
       
### Libraries
The code utilizes several libraries for functionalities like web development, computer vision, and facial recognition.

1. __Flask:__ A lightweight web application framework for Python.
2. __MySQL Connector/Python:__ Enables connecting to MySQL databases from Python applications.
3. __OpenCV (cv2):__ A powerful library for computer vision tasks like image and video processing.
4. __face_recognition:__ A wrapper library built on top of dlib, simplifying facial recognition tasks.

### Installation

#### Using `pip`
Open a terminal or command prompt and run the following command to install all the required libraries:

`pip install flask mysql-connector-python opencv-python face-recognition
`
### Using Virtual Environments (Recommended)
It's highly recommended to create a virtual environment for this project to isolate its dependencies from other Python projects on your system. You can use tools like `venv` or `virtualenv` to create a virtual environment. Refer to their documentation for specific instructions.

Once you have a virtual environment activated, run the pip install command mentioned earlier to install the libraries within the isolated environment.

### Additional Notes
* Ensure you have Python 3.x installed on your system before proceeding.
* If you encounter any issues during installation, refer to the official documentation of each library for troubleshooting steps.

















