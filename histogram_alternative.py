import numpy as np

def rectangular_density(samples, scale=1):
    N = len(samples)
    events_x = np.concatenate([samples-scale, samples+scale])
    events_dy = (1 / (N * 2 * scale)) * np.concatenate([np.ones_like(samples), -np.ones_like(samples)])

    events_idx = np.argsort(events_x)
    accum_x = events_x[events_idx]
    accum_y = np.cumsum(events_dy[events_idx])

    xs = np.stack([accum_x, accum_x], axis=-1).reshape((-1))
    ys = np.stack([np.pad(accum_y[:-1], [(1,0)]), accum_y], axis=-1).reshape((-1))

    return xs, ys

def triangular_density(samples, h=1):
    N = len(samples)
    events_x = np.concatenate([samples-h, samples, samples+h])
    events_dm = (1 / (N * h*h)) * np.concatenate([np.ones_like(samples), -2*np.ones_like(samples), np.ones_like(samples)])

    events_idx = np.argsort(events_x)
    accum_x = events_x[events_idx]

    accum_m = np.cumsum(events_dm[events_idx])[:-1]
    accum_dx = accum_x[1:] - accum_x[:-1]
    accum_dy = accum_m * accum_dx
    accum_y = np.cumsum(np.pad(accum_dy, [(1,0)]))
    
    return accum_x, accum_y
