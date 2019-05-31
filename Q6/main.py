from GaussSolver import GaussSolver
from time import time as epochTime
import numpy as np
import subprocess 
import os
import matplotlib.pyplot as plt

def func(x):
    xN = 0.5 * x + 0.5
    return xN**3 * np.cos(xN**2) / (1 + xN)

def PythonSolve(i):
    gs = GaussSolver(func, 0, 1, i)
    gs.exec()
    return gs.getResult()

def CSolve(i): 
    data, temp = os.pipe()
    os.write(temp, bytes(f'{i}\n', 'utf-8'))
    os.close(temp) 
    s = subprocess.check_output('./main', stdin = data, shell = True)  
    return s.decode('utf-8')


if __name__ == "__main__":
    max_N = int(input('Enter max_N(Less than 20 is recommended!):'))
    print(f'\nAnswer(N={max_N}) : {PythonSolve(max_N)}\n')

    # Execute and show:
    print('N \t Python(ms) \t C++(ms)')
    pythonTime_list = []
    cppTime_list = []
    for i in range(1, max_N + 1):
        start = epochTime()
        PythonSolve(i)
        pythonTime = 1000 * (epochTime() - start)
        pythonTime_list.append(pythonTime)

        start = epochTime()
        CSolve(i)
        cppTime = 1000 * (epochTime() - start)
        cppTime_list.append(cppTime)

        print(f'{i} \t {pythonTime:.5f} \t {cppTime:.5f}')

    # Plot:
    N_list = [i for i in range(1, max_N + 1)]
    plt.plot(N_list, pythonTime_list, 'r', label = 'Python')
    plt.plot(N_list, cppTime_list, 'g', label = 'C++')
    plt.title('Python Gauss Solver vs. C++ Gauss Solver')
    plt.xlabel('N (Degree of polynomial)')
    plt.ylabel('Execution time(ms)')
    plt.legend(loc='upper left')
    plt.savefig('result.pdf')
    plt.show()

