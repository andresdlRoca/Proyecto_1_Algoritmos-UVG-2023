from DaC_LCS import *
from DP_LCS import *
import time
import random
import string
import matplotlib.pyplot as plt

def generate_random_string(length):
    return ''.join(random.choice('ABCDEF') for _ in range(length))

def insert_substring(string1, string2, substring):
    index1 = random.randint(0, len(string1))
    index2 = random.randint(0, len(string2))
    return string1[:index1] + substring + string1[index1:], string2[:index2] + substring + string2[index2:]

string_range = [10,20,40,80,160,320,640]
input_strings = {}
for i in string_range:
    x = generate_random_string(i)
    y = generate_random_string(i)
    common_substring = generate_random_string(random.randint(1, i//2))
    x, y = insert_substring(x, y, common_substring)
    input_strings[x] = y

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

plt.plot(string_range, lcs_divide_and_conquer_runtimes, label='Divide and Conquer')
plt.plot(string_range, LCSubStr_runtimes, label='Dynamic Programming')
plt.xlabel('Input String Length')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()

print(lcs_divide_and_conquer_runtimes)
print(LCSubStr_runtimes)
    
