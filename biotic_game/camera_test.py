#_______OK_______
import cv2 

def list_cam(max_index = 5):
    available_cams = []

    for i in range(max_index + 1):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ob, frame = cap.read()
            if ob:
                available_cams.append(i)
                print(f"Camera found at index {i}")
            cap.release()
        else:
            print(f"No camera at index {i}")
    return available_cams

def test_cam(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Could not open camera at index {index}")
        return
    
    print(f"Video from camera at index {index}. 'q' to quit")
    while True:
        ob, frame = cap.read()
        if not ob:
            print("failed to grab frame")
            break
        cv2.imshow(f"Camera {index}", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Scanning for cameras...")
    cams = list_cam(5)
    if not cams:
        print("No cameras detected")
    else: 
        print(f"Available cams: {cams}")

        test_cam(cams[1])
