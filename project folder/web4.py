import subprocess
import os
import MySQLdb
import cv2
from flask import Flask, redirect, render_template, jsonify, request, session, url_for, flash
import re
from flask_mysqldb import MySQL
from python.data_set import open_camera
import threading


#face rec
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

from datetime import datetime, timedelta
import time
import face_recognition
import cv2
import numpy as np
import mysql.connector
import os
# from app import app

app = Flask(__name__, static_url_path="/static")
app.secret_key = 'your_secret_key'

#database connection start
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="face_rec_db"

db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',  # your MySQL password
            'database': 'face_rec_db'
            }
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='face_rec_db'
)

#main page
@app.route("/")
def main_page():
    return render_template("main_page.html")


#navigate login
@app.route("/nav_dept_login")
def nav_dept_login():
    return render_template("dept_login.html")

#attendance_data nav
@app.route('/search_data')
def search_data():
    return render_template('search_data.html')



app.static_folder = os.path.join(app.root_path, '/photos')


#dept login
@app.route("/dept_login", methods=['POST','GET'])
# @app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output a message if something goes wrong...
    msg = ''
                   # Check if "dept_id" and "dept_passwd" POST requests exist (user submitted form)
    if request.method == 'POST' and 'dept_id' in request.form and 'dept_passwd' in request.form:
        # Create variables for easy access
        dept_id = request.form['dept_id']
        dept_passwd = request.form['dept_passwd']

        # Establish the connection
        mysql_connection = mysql.connector.connect(**db_config)

        # Create a dictionary cursor
        cursor = mysql_connection.cursor(dictionary=True)
        # Check if dept exists using MySQL
        
        cursor.execute('SELECT * FROM dept_login WHERE dept_id = %s AND dept_passwd = %s', (dept_id, dept_passwd,))
        # Fetch one record and return result
        dept = cursor.fetchone()
        # If dept exists in dept_login table in out database
        if dept:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['dept_id'] = dept['dept_id']
            session['dept_head_name']=dept['dept_head_name']
            session['dept_branch']=dept['dept_branch']
            session['dept_passwd'] = dept['dept_passwd']
            # Redirect to home page
            msg="logged in sucessfully !"
            return render_template('search.html', msg=msg, dept=dept)
        else:
            # dept doesnt exist or dept_id/dept_passwd incorrect
            msg = 'Incorrect dept_id/dept_passwd!'
    # Show the login form with message (if any)
            return render_template('dept_login.html', msg=msg)
    return render_template('dept_login.html', msg=msg)



#logout session
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main_page'))

#navigation index
@app.route("/ind")
def navindex():
    # Check if the user is logged in
    if 'loggedin' in session:
        # Create a cursor with dictionary cursor type
        cursor = db.cursor(dictionary=True)
        
        # Query the database for department login data based on the department branch
        dept_branch = session['dept_branch']
        query = "SELECT * FROM dept_login WHERE dept_branch = %s"
        cursor.execute(query, (dept_branch,))
        dept_dbss = cursor.fetchone()
        
        # Close the cursor
        cursor.close()
        
        # Check if data was retrieved
        if dept_dbss:
            # Set session data for later use
            session['dept_head_name'] = dept_dbss['dept_head_name']
            session['dept_branch'] = dept_dbss['dept_branch']
            
            # Render the index.html template with department data
            return render_template("search.html", dept_dbs=dept_dbss)
    
    # Redirect the user to the login page if not logged in
    return redirect(url_for('login'))

#home navigation
@app.route("/index")
def index():
        if 'loggedin' in session:
            cur = db.cursor(dictionary=True)

            deptu=cur.execute("SELECT * FROM dept_login WHERE dept_branch=%s", (session['dept_branch'],))
            dept_dbss=cur.fetchone()
            if deptu:
            # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['dept_head_name']=deptu['dept_head_name']
                session['dept_branch']=deptu['dept_branch']
                return render_template("index.html", dept_dbs=dept_dbss)
        return render_template(url_for(login)) 

#attendance navigation
@app.route("/search")
def search():
        return render_template("search.html") 

#student view navigation
@app.route('/existing_list')
def existing_list():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    mysql_connection = mysql.connector.connect(**db_config)
    cursor = mysql_connection.cursor(dictionary=True)
    
    try:
        cursor.execute('SELECT * FROM student_db ')
        student_dbs = cursor.fetchall()
        
        if student_dbs:
            return render_template('existing_list.html', student_dbs=student_dbs)
        else:
            return render_template('existing_list.html', student_dbs=[])
    
    except Error as e:
        print(f"Database error: {e}")
        return render_template('not_found.html', error='Database error occurred.')
    


from flask import request, render_template, redirect, url_for
from mysql.connector import Error 



@app.route("/delete_student", methods=["POST"])
def delete_student():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        usn = request.form.get("usn")
        
        # Connect to the database
        mysql_connection = mysql.connector.connect(**db_config)
        cursor = mysql_connection.cursor()
        
        try:
            # Execute the delete query
            delete_query = "DELETE FROM student_db WHERE usn = %s"
            cursor.execute(delete_query, (usn,))
            mysql_connection.commit()  # Commit the transaction


            delete_query = "DELETE FROM attendance_log WHERE usn = %s"
            cursor.execute(delete_query, (usn,))
            mysql_connection.commit()
            # Redirect back to the existing list page after deleting
            return redirect(url_for("existing_list"))
        
        except Error as e:
            print(f"Database error: {e}")
            # Handle database error appropriately
            # You can render an error template or redirect to an error page
            return render_template('not_found.html', error='Database error occurred.')

    # Handle invalid requests or methods
    return "Invalid request"


#add_student navigation
@app.route("/add_student")
def add_student():
    return render_template("add_student.html")

#add_staff navigation
@app.route("/add_staff")
def add_staff():
    return render_template("add_staff.html")


@app.route("/data_search")
def data_search():
    # Check if the user is logged in as a department
    if 'loggedin' not in session or not session['loggedin']:
        # Redirect to login page if not logged in
        return redirect('/dept_login')
    
    # Get the logged-in department's branch from the session
    dept_branch = session['dept_branch']

    # Establish a connection to the database
    mysql_connection = mysql.connector.connect(**db_config)
    cursor = mysql_connection.cursor()

    # Query the subject_log table to get subject codes that match the department's branch
    cursor.execute('SELECT subject_code FROM subject_log WHERE branch_allot = %s', (dept_branch,))
    # Fetch all results
    subject_codes = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    mysql_connection.close()

    # Render the data in HTML
    # Passing the list of subject codes to the template to display in a dropdown
    return render_template('data_search.html', subject_codes=subject_codes)



db = mysql.connector.connect(**db_config)  
root_folder = os.path.join(os.getcwd(), 'photos')  

#add_subject navigation
@app.route("/submit_form", methods=["GET", "POST"])
# Path to the root folder for saving image
def submit_form():
    if request.method == 'POST':
        # Retrieve data from the form
        usn = request.form.get('usn')
        name = request.form.get('name')
        

        # Define the regular expression patterns for USN and name validation
        usn_pattern = r'^\d{1}[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{3}$'
        name_pattern = r'^[a-zA-Z\s]+$'
    

        # Validate the USN and name format
        if not re.match(usn_pattern, usn):
            flash("Invalid USN format. Please enter a valid USN in the format: int(1)char(2)int(2)char(2)int(3).")
            return render_template('add_student.html')
        
        if not re.match(name_pattern, name):
            flash("Invalid name format. Name must contain only letters and spaces.")
            return render_template('add_student.html')

        # Check for duplicate USN in the database
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM student_db WHERE usn = %s", (usn,))
        count = cursor.fetchone()[0]

        if count > 0:
            # If the USN already exists, notify the user and render the form page again
            flash(f"USN {usn} already exists. Please enter a different USN.")
            return render_template('add_student.html')

        # Proceed with inserting data into the database
        cursor.execute("INSERT INTO student_db (usn, name) VALUES (%s, %s)", (usn, name))
        db.commit()
        cursor.close()

        # Capture images using the capture_images function
        image_paths = capture_images(usn)

        # Render the student view template with context data
        return render_template('existing_list.html', usn=usn, name=name, image_paths=image_paths)

        # Capture images using the capture_images function
        image_paths = capture_images(usn)

        # Render the student view template with context data
        return render_template('existing_list.html', usn=usn, name=name, branch=branch, sem=sem, image_paths=image_paths)

def capture_images(usn):
    cap = cv2.VideoCapture(0)
    image_paths = []

    for i in range(2):
        ret, frame = cap.read()
        if ret:
            image_name = f'{usn}_{i + 1}.png'
            image_path = os.path.join(root_folder, image_name)
            cv2.imwrite(image_path, frame)
            image_paths.append(image_path)
            cv2.imshow('Captured Image', frame)
            cv2.waitKey(500)  # Wait for 500 ms

    cap.release()
    cv2.destroyAllWindows()

    return image_paths  # Return the list of image paths


@app.route("/search_data_view", methods=["GET", "POST"])
def search_data_view():
    if request.method == "POST":
        usn = request.form.get("search_usn")
        print("Received USN:", usn)
        
        mysql_connection = mysql.connector.connect(**db_config)
        cursor = mysql_connection.cursor(dictionary=True)
        
        try:
            cursor.execute('SELECT usn, log_date, time, camera_id FROM attendance_log WHERE usn = %s ORDER BY log_date DESC, time DESC LIMIT 1', (usn,))
            student_dbs = cursor.fetchall()
            
            if student_dbs:
                return render_template('search_data_view.html', student_dbs=student_dbs)
            else:
                return render_template('not_found.html')  # Render not found template
        
        except Error as e:
            print(f"Database error: {e}")
            return render_template('not_found.html', error='Database error occurred.')

    return render_template('search_data_view.html', student_dbs=[])



#thigsgshhsdgws
@app.route("/tryy")
def tryy():
    return render_template("try.html")


import mysql.connector
# Define a function to fetch start and end times from the database
def fetch_start_end_times():

    # Connect to the MySQL database using a context manager
    with mysql.connector.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            # Define the query to retrieve start and end times
            query = "SELECT start_time, end_time FROM subject_log"

            # Execute the query
            cursor.execute(query)

            # Fetch the first row
            row = cursor.fetchone()

            if row:
                start_time_str, end_time_str = row
                
                # Convert string times to datetime objects
                current_date = datetime.now().date()
                start_time = datetime.combine(current_date, datetime.strptime(start_time_str, '%H:%M:%S').time())
                end_time = datetime.combine(current_date, datetime.strptime(end_time_str, '%H:%M:%S').time())

                return start_time, end_time

    return None, None


def process_video(video_capture, camera_id, known_face_encodings, known_face_names, current_date, window_name, db_connection):
    recognized_names_during_period = set()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print(f"Failed to capture frame from camera {camera_id}.")
            break

        # Resize frame
        resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Convert frame to RGB color space
        rgb_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                recognized_names_during_period.add((name, camera_id))

                # Draw a rectangle around the recognized face
                cv2.rectangle(resized_frame, (left, top), (right, bottom), (0, 255, 0), 2)
                # Display the name of the recognized person
                cv2.putText(resized_frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the frame
        cv2.imshow(window_name, resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Insert recognized names into the database
    for name, camera_id in recognized_names_during_period:
        cursor = db_connection.cursor()
        current_time = datetime.now().strftime("%H:%M:%S")
        cursor.execute(
            "INSERT INTO attendance_log (usn, time, log_date, camera_id) VALUES (%s, %s, %s, %s)",
            (name, current_time, current_date, camera_id)
        )
        db_connection.commit()
        cursor.close()

    video_capture.release()

@app.route("/run_prg", methods=['POST'])
def prg_run():
    try:
        # Connect to MySQL database
        db_connection = mysql.connector.connect(**db_config)
        video_captures = [cv2.VideoCapture(0), cv2.VideoCapture(1)]

        # Load known faces from folder
        folder_path = "photos/"
        known_face_encodings = []
        known_face_names = []

        for filename in os.listdir(folder_path):
            if filename.endswith((".jpg", ".jpeg", ".png")):
                image_path = os.path.join(folder_path, filename)
                image = face_recognition.load_image_file(image_path)
                print("Loaded image:", image_path)
                
                face_encodings = face_recognition.face_encodings(image)
                print("Face encodings:", face_encodings)
                
                if face_encodings:
                    encoding = face_encodings[0]
                    name = os.path.splitext(filename)[0]
                    known_face_encodings.append(encoding)
                    known_face_names.append(name)
                else:
                    print("No face found in image:", image_path)

        # Define the current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Open video captures for both cameras
        video_captures = [cv2.VideoCapture(0), cv2.VideoCapture(1)]
          # Index 0 for the built-in camera, index 1 for the external camera

        # Check if video captures are opened
        if not all(vc.isOpened() for vc in video_captures):
            print("Failed to open video capture device(s).")
            return "Error: Failed to open video capture device(s).", 500

        # Create threads for each camera
        threads = []
        for idx, video_capture in enumerate(video_captures):
            thread = threading.Thread(target=process_video, args=(video_capture, idx, known_face_encodings, known_face_names, current_date, f"Camera {idx}", db_connection))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Release resources
        for video_capture in video_captures:
            if video_capture.isOpened():
                video_capture.release()
        cv2.destroyAllWindows()
        db_connection.close()

    return render_template("search.html"), 200
# Run the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)