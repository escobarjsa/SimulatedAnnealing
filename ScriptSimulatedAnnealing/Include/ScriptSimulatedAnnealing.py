import numpy as np
import math
import matplotlib.pyplot as plt

matriz = [
    [1, 3, 3, 2, 2, 1],
    [2, 3, 4, 6, 4, 3],
    [2, 1, 3, 3, 2, 2],
    [2, 4, 3, 5, 4, 2],
    [1, 3, 2, 1, 3, 2],
    [2, 2, 1, 2, 1, 2],
    [3, 1, 1, 3, 1, 2]
]

alpha = 0.995
# maximos = [110, 200, 122, 185, 105, 96, 110]
tempFin = 0.1
initialTemp = 1000
maxIterations = 5
Z_max = [25, 35, 40, 55, 38, 30]
size = len(matriz)


def solucionAleatoria():
    x_len = len(matriz)
    y_len = len(matriz[0])
    state = []
    for t in range(y_len):
        w = np.random.randint(x_len)
        while (matriz[w][t] == 0.0):
            ++w
            if (w > x_len - 1):
                w = 0
        state.append(w)
    return state


def generarVecinoAleatorio(solution):
    x_len = len(matriz)
    y_len = len(matriz[0])
    task = np.random.randint(y_len)
    worker = np.random.randint(x_len)
    while (matriz[worker][task] == 0.0):
        ++worker
        if (worker > x_len - 1):
            worker = 0
    state = solution.copy()
    state[task] = worker
    return state


def costo(solution):
    result = 0.0
    for t in range(len(solution)):
        worker = solution[t]
        time = matriz[worker][t]
        result += time
    return result


def euler(delta, temp):
    return math.exp(-delta / temp)


def init():
    x = []
    y = []
    step = 0

    # principal proccess
    for itr in range(maxIterations):
        tempActual = initialTemp
        currentSolution = solucionAleatoria()
        currentCosto = costo(currentSolution)

        while tempActual > tempFin:
            newSolution = generarVecinoAleatorio(currentSolution)
            newCosto = costo(newSolution)
            delta = newCosto - costo(currentSolution)
            if np.random.rand() < euler(delta, tempActual) or delta < 0:
                currentSolution = newSolution[:]
                currentCosto = newCosto

            tempActual = tempActual * alpha
            step = step + 1
            x.append(step)
            y.append(currentCosto)

    print(x)
    print(y)
    plt.figure("Simulated annealing algorithm")
    plt.plot(x, y)
    plt.xlabel("Iteraciones")
    plt.ylabel("Costos")
    plt.show()


init()


