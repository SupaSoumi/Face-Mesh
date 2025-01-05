import cv2
import mediapipe as mp
import time

class FaceMeshDetector():

    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        # Initialize MediaPipe face mesh model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            max_num_faces=self.maxFaces,
            min_detection_confidence=self.minDetectionCon,
            min_tracking_confidence=self.minTrackCon
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img, draw=True):
        # Convert image to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        faces = []

        # If faces are detected, draw landmarks and extract coordinates
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                if draw:
                    # Use FACEMESH_TESSELATION or FACEMESH_CONTOURS for connections
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION,
                                               self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
                faces.append(face)
        return img, faces

def main():
    cap = cv2.VideoCapture(0)  # Use webcam for live video feed
    pTime = 0
    detector = FaceMeshDetector(maxFaces=2)

    # Resize video capture resolution to minimize output
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, img = cap.read()
        if not success:
            break  # Exit loop if video ends or fails to read

        img, faces = detector.findFaceMesh(img)

        # Limit the number of faces printed (optional)
        if len(faces) != 0:
            print(faces[0])  # Print only the first face

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display FPS in smaller font size and different position
        cv2.putText(img, f'FPS: {int(fps)}', (20, 30), cv2.FONT_HERSHEY_PLAIN,
                    1, (255, 0, 0), 2)

        # Resize the image to minimize the window output
        img = cv2.resize(img, (640, 480))

        cv2.imshow("Face Mesh", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()

