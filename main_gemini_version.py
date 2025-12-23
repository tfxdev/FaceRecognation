import cv2 as cv
import face_recognition
import os
import sys

def capture_webcam_image():
    capture = cv.VideoCapture(0)
    if not capture.isOpened:
        print("Error: Could not open the Webcam!")
        sys.exit()
    
    print("Press 'q' to capture your photo...")
    final_frame = None
    
    while True:
        ret, frame = capture.read()
        
        if not ret:
            break
        
        cv.imshow("Webcam - Press 'q' to Capture", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            final_frame = frame
            break
    
    capture.release()
    cv.destroyAllWindows()
    
    return final_frame

def get_encoding(img_bgr):
    """Converts BGR to RGB and return encoding if a face is found."""
    rgb_img = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    encoding = face_recognition.face_encodings(rgb_img)
    
    if len(encoding) > 0:
        return encoding[0]
    return None

def compare():
    base_image_path = ask_user_for_choosing_file()
    if not base_image_path:
        return
    
    # Precess Base Image
    
    base_img = cv.imread(base_image_path)

## to be continued ...
        