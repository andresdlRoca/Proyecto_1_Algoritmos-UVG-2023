from DaC_LCS import *
from DP_LCS import *
import time
import random
import matplotlib.pyplot as plt

input_strings = {
    'Computer Science': 'Comp-Sci',
    'GeeksforGeeks': 'GeeksQuiz',
    'OldSite:GeeksforGeeks.org': 'NewSite:GeeksQuiz.com'
}

lcs_divide_and_conquer_runtimes = []
LCSubStr_runtimes = []

for x, y in input_strings.items():
    start_time = time.perf_counter()
    lcs_divide_and_conquer(x, y)
    end_time = time.perf_counter()
    lcs_divide_and_conquer_runtimes.append("{:.8f}".format(end_time - start_time))
    
    start_time = time.perf_counter()
    LCSubStr(x, y, len(x), len(y))
    end_time = time.perf_counter()
    LCSubStr_runtimes.append("{:.8f}".format(end_time - start_time))

    print("x: ", x)
    print("y: ", y)
    ("---------------------")
    print("substring: ", lcs_divide_and_conquer(x, y))
    print("DivideAndConquer Length: ", len(lcs_divide_and_conquer(x, y)))
    print("DynamicProgramming Length: ", LCSubStr(x, y, len(x), len(y)))
    print("===================")

plt.plot(input_strings.keys(), lcs_divide_and_conquer_runtimes, label='Divide and Conquer')
plt.plot(input_strings.keys(), LCSubStr_runtimes, label='Dynamic Programming')
plt.xlabel('Input String')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()

print(LCSubStr_runtimes)
print(lcs_divide_and_conquer_runtimes)