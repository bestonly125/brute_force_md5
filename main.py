import os
from openpyxl import load_workbook

# Подключаемся к обезличенному набору данных
md5_list = open('md5_list.txt', "w")
wb = load_workbook("scoring_data_v.0.3.3.xlsx")
ws = wb["A2"]

# Набор обезличенных данных преобразуем виде текстова документа для быстрого перебора
for i in range(2,len(ws["A"])+1):
    md5_list.write(f"{ws['A' + str(i)].value}\n")
md5_list.close()

# Проверка текстового документа на наличия заполнения
read_md5_list = open("md5_list.txt", "r")
print(f"len = {bool(read_md5_list)}")

# Вызываем библиотеку hashcat. Перебор данных осуществляется с помощью масок с длиной 11 символов
if bool(read_md5_list) is True:
    os.system("./hashcat.bin -m0 -a3 md5_list.txt ?d?d?d?d?d?d?d?d?d?d?d")

# Деобезличенный набор данных хранится в scoring_data_v.1.0.xlsx
potfile = open("hashcat.potfile", "r")
dict_md5 = {}
for md5 in potfile:
    dict_md5[str(md5[:32])] = md5[33:44]
for row in range(2,len(ws["A"])+1):
    if dict_md5[str(ws['A' + str(row)].value)]:
          ws['A' + str(row)] = dict_md5[str(ws['A' + str(row)].value)]
wb.save(filename="scoring_data_v.1.0.xlsx")