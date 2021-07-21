import math
import cv2
import mediapipe as mp

class hand_detector:
    def __init__(self, mode=False, maxHands=1, detectionCon=0.9, trackCon=0.9):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(mode, maxHands, detectionCon, trackCon)

    def draw_landmarks(self, img):
        self.img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(self.img_rgb)
        
        if self.results.multi_hand_landmarks:
            for landmarks in self.results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(img, landmarks, self.mp_hands.HAND_CONNECTIONS)
        
        return img

    def get_landmarks(self, img):
        self.landmarks = []

        if self.results.multi_hand_landmarks:
            self.myHand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(self.myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                self.landmarks.append([id, cx, cy])
        
        return self.landmarks

    def find_distance(self, lm1, lm2):
        x1, y1 = self.landmarks[lm1][1], self.landmarks[lm1][2]
        x2, y2 = self.landmarks[lm2][1], self.landmarks[lm2][2]

        length = math.hypot(x2 - x1, y2 - y1)

        return length