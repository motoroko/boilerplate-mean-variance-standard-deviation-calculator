import numpy as np

def calculate(list):
    try:
        list = np.array(list).reshape(3,3)
        calculations = {
            'mean':[np.mean(list, axis=0).tolist(), np.mean(list, axis=1).tolist(), np.mean(list.flatten())],
            'variance':[np.var(list, axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list.flatten())],
            'standard deviation':[np.std(list, axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list.flatten())],
            'max':[np.max(list, axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list.flatten())],
            'min':[np.min(list, axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list.flatten())],
            'sum':[np.sum(list, axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list.flatten())],
        }
        return calculations
    except ValueError:
        raise ValueError('List must contain nine numbers.')