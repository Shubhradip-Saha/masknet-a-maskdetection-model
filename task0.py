import cv2
import webbrowser
import time

# Load the cascades for face and nose detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

# Define the safe limit for unmasked faces
safe_limit = 2

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Initialize the counter variable
    red_faces = 0

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        # Detect the noses
        roi_gray = gray[y:y + h, x:x + w]
        noses = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)

        if len(noses) > 0:
            # Draw the rectangle in blue color
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            red_faces += 1
        else:
            # Draw the rectangle in red color
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Determine safety based on the number of unmasked faces
    if red_faces <= safe_limit:
        safety_message = "Safe"
        safety_color = "green"
    else:
        safety_message = "Unsafe"
        safety_color = "red"

    # Display the number of unmasked faces and safety message
    cv2.putText(img, f"Unmasked Faces: {red_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(img, f"Status: {safety_message}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the image
    cv2.imshow('img', img)

    # Stop if the escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == ord('q') or safety_message == "Unsafe":
        break

# Generate the HTML content
# Generate the HTML content
html_content = f'''<html>
<head>
    <style>
        body {{
            background-image: url('path/to/image.jphttps://drive.google.com/file/d/1QlT5Jjv_nDFxCgmhCzimh22D355MQfQQ/view?usp=share_link');
            background-repeat: no-repeat;
            background-size: cover;
        }}
    </style>
    <title>Welcome to Covid Zone Analyser</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body class="is-preload">
    <header id="header">
        <h1>Welcome to Covid Zone Analyser!</h1>
        <p>A simple approach to make your locality better and safer.<br /></p>
        <p>The Status of Your Zone is: <span style="color:{safety_color}; font-weight:bold; font-size: 1.5em;">{safety_message}</span></p>
    </header>
    <br class="return-to-main">
    <button onclick="window.location.href = 'http://127.0.0.1:5500/index.html';">Return to Main Page</button>
    </div>
    <footer id="footer">
        <ul class="icons">
            <li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
            <li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
            <li><a href="#" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
            <li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
        </ul>
        <ul class="copyright">
            <li>&copy; In Association with the Indian Government</li>
            <li>Credits: <a href="http://html5up.net">MaskNet Private Limited</a></li>
        </ul>
    </footer>
    <script src="assets/js/main.js"></script>
</body>
</html>'''


# Write the HTML content to a file
with open("index2.html", "w") as html_file:
    html_file.write(html_content)

# Close the VideoCapture object
cap.release()

# Delay to ensure the file is saved
time.sleep(2)

# Open the generated HTML file in a new tab
webbrowser.open_new_tab("index2.html")