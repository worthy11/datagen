import numpy as np
import csv

def ComputeDistances(arr: np.array) -> np.array:
    w = np.max(arr[:, 0]) - np.min(arr[:, 0])
    h = np.max(arr[:, 1]) - np.min(arr[:, 1])
    distances = np.zeros(441)
    for i in range(21):
        for j in range(21):
            dx = (arr[j][0] - arr[i][0]) / w
            dy = (arr[j][1] - arr[i][1]) / h
            distances[i*21+j] = np.sqrt(dx**2 + dy**2)
    return distances

def ParseLandmarks(hand_landmarks) -> np.array:
    coords = list()
    
    for landmark in hand_landmarks.landmark:
        coords.append([landmark.x, landmark.y])
    return np.array(coords)

def AddStaticSample(sample: np.array, label: str, filepath: str='dataset.csv') -> bool:
    sample = list([str(_) for _ in sample])
    with open(filepath, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([label] + sample)
    return 1

def AddDynamicSample(sample: np.array, label: str, filepath: str='dataset_dynamic.csv') -> bool:
    return 1

def ComputeDifferences(arr: list):
    differences = arr
    prev = differences[0]
    differences.pop(0)
    
    for idx in range(len(arr)):
        curr = differences[idx]
        differences[idx] -= prev
        prev = curr

    return differences
