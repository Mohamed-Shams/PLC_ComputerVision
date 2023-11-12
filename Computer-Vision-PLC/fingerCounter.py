from opcua import Client
import cv2
import time
import os
import HandTrackingModule as ht
import sys


    # Connect to OPC UA server
url = "opc.tcp://Shams:53530/OPCUA/SimulationServer"  # Replace with OPC UA server URL

try:
        client = Client(url)
        client.connect()
        print("Connected to OPC UA")
except Exception as err:
        print("err", err)
        sys.exit(1)

camera_width, camera_height = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, camera_width)
cap.set(4, camera_height)

folder_path = "FingerImages"
myList = os.listdir(folder_path)
print(myList)

overLayList = []
for img_path in myList:
    image = cv2.imread(f"{folder_path}/{img_path}")
    # print(f"{folder_path}/{img_path}")
    overLayList.append(image)
# print(len(overLayList))

prev_time = 0
curr_time = 0

detector = ht.handDetector(min_detection=0.75)
top_fingers_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)
    # print(lm_list)

    if len(lm_list) != 0:
        finger_state = []
        # for thump (special case)
        if lm_list[top_fingers_ids[0]][1] > lm_list[top_fingers_ids[0] - 1][1]:
            # if finger is open
            finger_state.append(1)
        else:
            # if finger is closed
            finger_state.append(0)

        # rest of fingers
        for f_id in range(1, 5):
            if lm_list[top_fingers_ids[f_id]][2] < lm_list[top_fingers_ids[f_id] - 2][2]:
                # if finger is open
                finger_state.append(1)
            else:
                # if finger is closed
                finger_state.append(0)

        # print(finger_state)
        total_fingers = finger_state.count(1) # find how many Ones do you have in the list
        print(total_fingers)

        if __name__ == '__main__':
             new_node = client.get_node("ns=3;i=1008")                  # To be changed With prosys(OPC UA) Variable
             client.set_values([new_node], [float(total_fingers)])

     ##   h, w, c = overLayList[total_fingers - 1].shape
     ##   img[0: h, 0: w] = overLayList[total_fingers - 1]

     ##   cv2.rectangle(img, (20, 225), (170, 425), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, str(total_fingers), (45, 375), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    10, (0 , 0, 255), 20)


    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    ##cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 3,
      ##          (255, 255, 255), 3)

    cv2.imshow("Image", img)
    # Exit the program if 'Esc' key is pressed
    if cv2.waitKey(1) == 27:  # 27 is the ASCII value of 'Esc'
        break

cap.release()
cv2.destroyAllWindows()
