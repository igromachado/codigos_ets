import random as rd
from typing import List

def gen_peak(lines : int = 1000, columns : int = 1000, max_value : int = 4048) -> List[List[int]]:

    onion = [[0 for _ in range(columns)] for __ in range(lines)]

    l_secret = rd.randint(0, lines-1)
    c_secret = rd.randint(0, columns-1)

    onion[l_secret][c_secret] = max_value

    for i in range(l_secret-1, -1, -1):
        cap = onion[i+1][c_secret] 
        onion[i][c_secret] = rd.randint(int(cap-1-max_value*0.05), cap-1)

    for i in range(l_secret+1, lines):
        cap = onion[i-1][c_secret] 
        onion[i][c_secret] = rd.randint(int(cap-1-max_value*0.05), cap-1)


    for i in range(c_secret-1, -1, -1):
        cap = onion[l_secret][i+1]
        onion[l_secret][i] = rd.randint(int(cap-1-max_value*0.05),cap-1)

        for j in range(l_secret-1, -1, -1):
            cap1 = onion[j+1][i] 
            cap2 = onion[j][i+1] 
            cap = min(cap1,cap2)
            onion[j][i] = rd.randint(int(cap-1-max_value*0.05), cap-1)

        for j in range(l_secret+1, lines):
            cap1 = onion[j-1][i] 
            cap2 = onion[j][i+1] 
            cap = min(cap1,cap2)
            onion[j][i] = rd.randint(int(cap-1-max_value*0.05), cap-1)

    for i in range(c_secret+1, columns):
        cap = onion[l_secret][i-1]
        onion[l_secret][i] = rd.randint(int(cap-1-max_value*0.05),cap-1)

        for j in range(l_secret-1, -1, -1):
            cap1 = onion[j+1][i] 
            cap2 = onion[j][i-1] 
            cap = min(cap1,cap2)
            onion[j][i] = rd.randint(int(cap-1-max_value*0.05), cap-1)

        for j in range(l_secret+1, lines):
            cap1 = onion[j-1][i] 
            cap2 = onion[j][i-1] 
            cap = min(cap1,cap2)
            onion[j][i] = rd.randint(int(cap-1-max_value*0.05), cap-1)

    return onion