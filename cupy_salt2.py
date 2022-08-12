
t_num = [89106881090,89057801765,89809229343]

potfile = open("hashcat.potfile", "r")
array_salts_num = []
for md5 in potfile:
     array_salts_num.append(int(md5[33:44]))


def salts(t_num:int,array_salts_num):
    salt = []
    for salts_num in array_salts_num:
        salt.append(salts_num-t_num)
    return salt

salts1 = salts(t_num[0],array_salts_num)
salts2 = salts(t_num[1],array_salts_num)
salts3 = salts(t_num[2],array_salts_num)

salt_res = set(salts1) & set(salts2) & set(salts3)

print(f"salt[{len(salt_res)}] = {list(salt_res)}")


