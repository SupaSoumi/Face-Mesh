# Face-Mesh
Tracks Face; Can be used on videos and on multiple people.
Face Mesh Detector
A Python project that uses OpenCV and MediaPipe to detect facial landmarks in real-time through your webcam or from a video file. The program draws facial landmarks on detected faces and shows the live FPS (frames per second).

Features:
Detects up to 2 faces in real-time.
Draws facial landmarks on the detected faces.
Displays FPS in the top-left corner.
Can process live webcam feed or video files.
Prerequisites:
Make sure you have Python installed on your machine along with the required dependencies:

Python 3.x
OpenCV
MediaPipe
Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/FaceMeshDetector.git
cd FaceMeshDetector
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Or, if you don't have requirements.txt, install manually:

bash
Copy code
pip install opencv-python mediapipe
Usage
Live Webcam Feed:

Simply run the Python script to use your webcam as the input source.
bash
Copy code
python facemesh.py
The script will open a window showing the live video feed with facial landmarks drawn on detected faces.

Video File Input:

To process a video file, replace 0 with the file path of your video (e.g., "Videos/1.mp4") in the cv2.VideoCapture function within the script.
python
Copy code
cap = cv2.VideoCapture("Videos/1.mp4")
Adjust Parameters:

The number of faces to detect, the detection confidence, and the tracking confidence can be adjusted by modifying the following parameters in the script:
maxFaces: Max number of faces to detect (default: 2).
minDetectionCon: Minimum detection confidence (default: 0.5).
minTrackCon: Minimum tracking confidence (default: 0.5).
Exit:

Press q to close the window.
How It Works:
The script uses MediaPipe's Face Mesh model to detect and track facial landmarks.
It processes the video frame-by-frame, converts the frame to RGB, and then detects face landmarks using the FaceMesh API.
The landmarks are drawn on the frame, and the FPS is displayed in the top-left corner.
Example Output:
The program will display a window showing your face (or faces) with landmarks drawn on the facial features. The FPS will be shown at the top-left of the window.

Screenshot:
(Include a screenshot here if you want)

Troubleshooting
Issue: Webcam not detected.
Solution: Make sure your webcam is connected and accessible. You may need to change the index in cv2.VideoCapture(0) if you're using a different camera.
Issue: Video file not playing.
Solution: Ensure the video path is correct and the file format is supported by OpenCV.
License
This project is licensed under the MIT License - see the LICENSE file for details.

