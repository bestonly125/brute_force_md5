import cupy as cp
import time


kernel = cp.ElementwiseKernel(
     'int64 t_num1, int64 t_num2, int64 arg_s1, int64 arg_s2 ', 'int64 salt',
     '''
     if ((arg_s1 - t_num1) == (arg_s2 - t_num2))
        {
               salt = arg_s1 - t_num1;
        }
        else{ 
               salt=0;
        }''')

potfile = open("hashcat.potfile", "r")
array_salts = []
for md5 in potfile:
     array_salts.append(int(md5[33:44]))
sort_salts = sorted(array_salts)[:2]
cp_salts = cp.array(sort_salts)

def result_salt(t_number,cp_salt):
     arg_s1 = cp.repeat(cp_salt[0], len(t_number))
     arg_s2 = cp.repeat(cp_salt[1], len(t_number))
     array_result = []
     for i in range(len(t_number)):
          arg_x = cp.repeat(t_number[i],len(t_number))
          arg_result = kernel(arg_x,t_number,arg_s1,arg_s2)
          arg_result = cp.trim_zeros(arg_result)
          array_result.append(list(cp.asnumpy(arg_result)))
     return array_result

array_result =[]
start = time.time()
for i in range(1):
     t_num = cp.arange(89011110000+(i*10000), 89011119999+(i*10000))
     array_result.append(result_salt(t_num, cp_salts))
end = time.time()
print(array_result)
print("time: ", end - start)

