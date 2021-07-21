# General Imports
import os
import cv2
import clipboard
import numpy as np
import mediapipe as mp
import hand_detector as htrack

# Python File Imports
import task_performer

# Copy an empty string to clipboard 
clipboard.copy('')

# Initialize hand_detector class
detector = htrack.hand_detector()

def run_gestures(landmarks):    
    thumb = True if (landmarks[4][1] > landmarks[3][1]) else False
    index = True if (landmarks[8][2] < landmarks[6][2]) else False
    middle = True if (landmarks[12][2] < landmarks[10][2]) else False
    ring = True if (landmarks[16][2] < landmarks[14][2]) else False
    pinky = True if (landmarks[20][2] < landmarks[18][2]) else False

    all_open = True if (thumb and index and middle and ring and pinky) else False

    ids = {
        # Single Open Finger
        'open_thumb': True if (thumb and not index and not middle and not ring and not pinky) else False, 
        'open_index': True if (index and not thumb and not middle and not ring and not pinky) else False,     
        'open_ring': True if (ring and not thumb and not index and not middle and not pinky) else False,     
        'open_pinky': True if (pinky and not thumb and not index and not middle and not ring) else False,       

        # Single Folded Finger
        'fold_thumb': True if (not thumb and index and middle and ring and pinky) else False, 
        'fold_index': True if (not index and thumb and middle and ring and pinky) else False, 
        'fold_middle': True if (not middle and thumb and index and ring and pinky) else False, 
        'fold_ring': True if (not ring and thumb and index and middle and pinky) else False, 
        'fold_pinky': True if (not pinky and thumb and index and middle and ring) else False, 

        # Touch thumb tip to finger tip
        'fold_thumb_and_index': True if (not thumb and not index and middle and ring and pinky) else False,
        'fold_index_and_middle': True if (not index and not middle and thumb and ring and pinky) else False,
        'fold_middle_and_ring': True if (not middle and not ring and thumb and index and pinky) else False,
        'fold_ring_and_pinky': True if (not ring and not pinky and thumb and index and middle) else False,
    }
    
    if len(ids) != 0:
        for id in ids:
            if ids[id]:
                x = task_performer.perform_task(id=id, all_fingers_open=all_open, landmarks=landmarks)
                x.run_actions()
                

def main_run():          
    cap = cv2.VideoCapture(0)
    cap.set(3, 1024)
    cap.set(4, 576)
    
    while True:      
        success, img = cap.read()

        img = detector.draw_landmarks(img)
        flipped_image = cv2.flip(img, 1)
        landmarks = detector.get_landmarks(img)
        
        if len(landmarks) != 0:
            run_gestures(landmarks)
                
        cv2.imshow("image", flipped_image)
        cv2.waitKey(1)

if __name__ == "__main__":
    main_run()