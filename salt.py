import numpy as np
import time
# s = [94003234569,94030788999]

t_num = np.arange(89011110000,89011119999)

potfile = open("hashcat.potfile", "r")
array_salts = []
for md5 in potfile:
     array_salts.append(int(md5[33:44]))
s = sorted(array_salts)[:2]

print(s)
print(t_num[0])
def arg_y(arg_a, arg_b):

    if ((s[0] - arg_a) == (s[1] - arg_b)):
        print(True, arg_a, arg_b)
        return s[0] - arg_a
    else:
        print(False, arg_a, arg_b)
        return False
array_y = []

start = time.time()
for i in range(len(t_num)):
    for j in range(len(t_num)):
        y = arg_y(t_num[i],t_num[j])
        if bool(y) == True:
            array_y.append(y)

                
print(array_y)
end = time.time()
print("time: ", end - start)