# counting the number of floors on the basis of windows coordinates
import numpy as np

def number_floors(wins):
    medium_h = 0
    for win in wins:
        medium_h += win[3]
    if len(wins) == 0:
        return 1
    medium_h = medium_h/len(wins)
    floors = np.zeros(163)
    dw = np.zeros(163)
    dw[0] = wins[0][1]
    for win in wins:
        for i in range (163):
            if abs(win[1] - dw[i]) < medium_h:
                floors[i] += 1
                break
            elif  dw[i+1] == 0:
                dw[i+1] = win[1]
                floors[i+1] += 1
                break
    n_floors = np.count_nonzero(floors)
    return n_floors






