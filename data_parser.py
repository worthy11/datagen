import numpy as np
import csv
import os

def ComputeDistances(arr: np.array) -> np.array:
    w = np.max(arr[:, 0]) - np.min(arr[:, 0])
    h = np.max(arr[:, 1]) - np.min(arr[:, 1])
    distances = np.empty((21, 21))
    for i in range(21):
        for j in range(21):
            dx = (arr[j][0] - arr[i][0]) / w
            dy = (arr[j][1] - arr[i][1]) / h
            distances[i][j] = np.sqrt(dx**2 + dy**2)
    return distances

def ParseLandmarks(hand_landmarks) -> np.array:
    coords = list()
    
    for landmark in hand_landmarks.landmark:
        coords.append([landmark.x, landmark.y])
    received = np.array(coords)
    observed = ComputeDistances(received)
    observed = observed.reshape(21*21)
    return observed

def AddSample(sample: np.array, label: str, filepath: str='dataset.csv') -> bool:
    sample = list([str(_) for _ in sample])
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([label] + sample)
    return 1

