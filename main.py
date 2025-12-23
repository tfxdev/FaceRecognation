import cv2 as cv
import face_recognition

def capture_webcam_image():
    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Error: Couldnot open the Webcam!")
        exit()

    while True:
        ret, frame = capture.read()
        
        if not ret:
            break

        cv.imshow("Webcam", frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()
    
    return frame
    
    
def base_image(base_image_url):
    base_img = cv.imread(base_image_url)
    base_rgb_img = cv.cvtColor(base_img, cv.COLOR_BGR2RGB)
    base_img_encoding = face_recognition.face_encodings(base_rgb_img)[0]

    return base_img_encoding

def processed_captured_image():
    rgb_img2 = cv.cvtColor(capture_webcam_image(),cv.COLOR_BGR2RGB)
    captured_img_encoding = face_recognition.face_encodings(rgb_img2)[0]
    
    return captured_img_encoding

def compare(base_image_url):
    result = face_recognition.compare_faces([base_image(base_image_url)], processed_captured_image())
    print("Result", result)

compare("photos/Toufic.jpg")

cv.waitKey(0)