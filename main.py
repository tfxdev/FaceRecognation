import cv2 as cv
import face_recognition
import sys
import os

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
    print(base_image_url)
    result = face_recognition.compare_faces([base_image(base_image_url)], processed_captured_image())
    print("Result", result)
    cv.waitKey(0)
    sys.exit()
    

def ask_user_for_choosing_file():
    image_files = os.listdir("./photos")

    if len(image_files) > 0:
        print("\nAvailable images are listed bellow: \n")
        count = 1
        for i in image_files:
            print(count,"::", i, end="\n")
            count += 1
        
        while True:
            try:
                base_image_num_input = int(input(f"\nType the image number between [1:{count-1}]:"))
                if base_image_num_input > 0 and base_image_num_input < count:
                    break
            except:
                print(f"Only numbers between [1:{count-1}] are allowed!\n")
                continue
            
        base_image_number = base_image_num_input - 1
        print(base_image_number)
        return "./photos/" + image_files[base_image_number]


if __name__ == "__main__":
    try:
        compare(ask_user_for_choosing_file())
    except Exception as e:
        print(f"Something not right! {e}")


