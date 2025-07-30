import numpy as np

def calculate(li):
    if len(li) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(li).reshape(3, 3)

    mean_ax0 = arr.mean(axis=0)
    mean_ax1 = arr.mean(axis=1)
    mean_flt = arr.mean()

    var_ax0 = arr.var(axis=0)
    var_ax1 = arr.var(axis=1)
    var_flt = arr.var()

    std_ax0 = arr.std(axis=0)
    std_ax1 = arr.std(axis=1)
    std_flt = arr.std()

    max_ax0 = arr.max(axis=0)
    max_ax1 = arr.max(axis=1)
    max_flt = arr.max()

    min_ax0 = arr.min(axis=0)
    min_ax1 = arr.min(axis=1)
    min_flt = arr.min()

    sum_ax0 = arr.sum(axis=0)
    sum_ax1 = arr.sum(axis=1)
    sum_flt = arr.sum()

    calculations = {
        'mean': [
            mean_ax0.tolist(),
            mean_ax1.tolist(),
            float(mean_flt)
            ],
        'variance': [
            var_ax0.tolist(),
            var_ax1.tolist(),
            float(var_flt)
            ],
        'standard deviation': [
            std_ax0.tolist(),
            std_ax1.tolist(),
            float(std_flt)
            ],
        'max': [
            max_ax0.tolist(),
            max_ax1.tolist(),
            float(max_flt)
            ],
        'min': [
            min_ax0.tolist(),
            min_ax1.tolist(),
            float(min_flt)
            ],
        'sum': [
            sum_ax0.tolist(),
            sum_ax1.tolist(),
            float(sum_flt)
            ]
        }

    return calculations