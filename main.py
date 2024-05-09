import mediapipe as mp
import cv2
from data_parser import *
from config import *

capture = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hand_recognizer = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def main():
    list = 0
    label = 0
    detected = 0

    filepath = './img/{}.png'.format(LABELS[list][label])
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

        cv2.imshow('Webcam', img)

        key = cv2.waitKey(1)
        if key == 13:
            if detected == 0:
                print('No hand detected')

            elif detected > 1:
                print('Too many hands detected')

            else:
                str_label = LABELS[list][label]
                if str_label.isdigit():
                    str_label = LABELS[list][0]
                if AddSample(sample, str_label):
                    print('Saved sample successfully')
                    if len(LABELS[list]) == label + 1:
                        label = 0
                        list += 1
                    else:
                        label += 1

                else:
                    print('Failed to save sample')

            if list == len(LABELS):
                print('Data collection finished. Go again? (y/n)')
                key = cv2.waitKey(0)
                if key == 89 or key == 121:
                    list = 0
                    label = 0
                    filepath = './img/{}.png'.format(LABELS[list][label])
                    tip = cv2.imread(filepath)
                    tip = cv2.resize(tip, (0, 0), fx = 2, fy = 2)
                    cv2.imshow('Instruction', tip)
                else:
                    break
            else:
                filepath = './img/{}.png'.format(LABELS[list][label])
                tip = cv2.imread(filepath)
                tip = cv2.resize(tip, (0, 0), fx = 2, fy = 2)
                cv2.imshow('Instruction', tip)
        detected = 0

main()