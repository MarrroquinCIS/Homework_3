# luis Marroquin
# 1975448
# CIS-2348
# 11.18 Filter and sort a list
inputList = input()
lst = []
for val in inputList.split(" "):
    if int(val)>=0:
        lst.append(int(val))
lst.sort()
for val in lst:
    print(val, end=" ")