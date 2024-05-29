import mediapipe as mp
import cv2
from data_parser import *
from config import *

capture = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hand_recognizer = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def pjm_static():
    list = 0
    label = 0
    detected = 0
    prev = np.zeros(441)

    filepath = './img/{}.png'.format(STATIC_LABELS[list][label])
    tip = cv2.imread(filepath)
    tip = cv2.resize(tip, (0, 0), fx = 2, fy = 2)
    cv2.imshow('Instruction', tip)

    while 1:
        not_empty, img = capture.read()
        if not_empty:
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hand_recognizer.process(imgRGB)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    detected += 1
                    sample = ParseLandmarks(hand_landmarks)
                    distances = ComputeDistances(sample)
                    mean = np.sum(distances - prev) ** 2
                    prev = np.copy(distances)
                    print(distances)

        cv2.imshow('Webcam', img)

        key = cv2.waitKey(1)
        
        if key == 27:
            cv2.destroyAllWindows()
            return
        
        if key == 13:
            if detected == 0:
                print('No hand detected')

            elif detected > 1:
                print('Too many hands detected')

            else:
                str_label = STATIC_LABELS[list][label]
                if str_label.isdigit():
                    str_label = STATIC_LABELS[list][0]
                if AddStaticSample(sample, str_label):
                    print('Saved sample successfully')
                    if len(STATIC_LABELS[list]) == label + 1:
                        label = 0
                        list += 1
                    else:
                        label += 1

                else:
                    print('Failed to save sample: unknown error')

            if list == len(STATIC_LABELS):
                print('Data collection finished. Go again? (y/n)')
                key = cv2.waitKey(0)
                if key == 89 or key == 121:
                    list = 0
                    label = 0
                    filepath = './img/{}.png'.format(STATIC_LABELS[list][label])
                    tip = cv2.imread(filepath)
                    tip = cv2.resize(tip, (0, 0), fx = 2, fy = 2)
                    cv2.imshow('Instruction', tip)
                else:
                    break
            else:
                filepath = './img/{}.png'.format(STATIC_LABELS[list][label])
                tip = cv2.imread(filepath)
                tip = cv2.resize(tip, (0, 0), fx = 2, fy = 2)
                cv2.imshow('Instruction', tip)
        detected = 0

def pjm_dynamic():
    record = False
    landmarks = []
    distances = []
    sample = []
    label = 0

    while 1:
        not_empty, img = capture.read()
        if not_empty and record:
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hand_recognizer.process(imgRGB)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    np_landmarks = ParseLandmarks(hand_landmarks)
                    np_distances = ComputeDistances(np_landmarks)
                    landmarks.append(np_landmarks)
                    distances.append(np_distances)
                    break

        cv2.imshow('Webcam', img)

        key = cv2.waitKey(1)
        if key == 13:
            if not record:
                record = True
                print('Recording started')

            else:
                record = False
                print('Recording ended')

                if landmarks and distances:
                    # landmarks = ComputeDifferences(landmarks)
                    # distances = ComputeDifferences(distances)
                    for l in landmarks:
                        sample.append([coord for landmark in l for coord in landmark])
                
                    if AddDynamicSample(sample, str(label)):
                        print(F'Saved {len(landmarks)}-frame sample successfully')
                        if label < len(TEST_LABELS) - 1:
                            label += 1
                        else:
                            label = 0
                        print(F'Current label: {TEST_LABELS[label]}')
                    else:
                        print('Failed to save sample')
                else:
                    print('No data recorded')

                landmarks.clear()
                distances.clear()
                sample.clear()
            
pjm_static()
# pjm_dynamic()