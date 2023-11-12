import cv2
import mediapipe as mp
import time


class handDetector:
    def __init__(self, img_mode=False, max_hands=2, complexity=1, min_detection=0.5, min_tracking=0.5):
        self.img_mode = img_mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.min_detection = min_detection
        self.min_tracking = min_tracking

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.img_mode, self.max_hands, self.complexity,
                                        self.min_detection, self.min_tracking)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        multi_hand_result = self.results.multi_hand_landmarks

        if multi_hand_result:
            for hand_lms in multi_hand_result:   # we have 21 land_mark in the hand
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_lms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img


    def find_position(self, img, handNum=0, draw=True):
        lmList = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[handNum]

            for id, lm in enumerate(my_hand.landmark):
                # print(id, lm)
                height, width, c = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                # print(id + 1, ": ", cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    cap = cv2.VideoCapture(0)  # give access to video
    prevTime = 0
    currTime = 0

    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lmList = detector.find_position(img)

        if len(lmList) != 0:
            print(lmList[4])

        # id numbers
        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 255, 255), 3)

        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
