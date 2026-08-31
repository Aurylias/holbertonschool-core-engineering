#!/usr/bin/env python3
numList = []
for num in range(1, 100):
    if str(num)[::-1] in numList or "{:02d}".format(num)[0] == \
"{:02d}".format(num)[1]:
        pass
    else:
        numList.append("{:02d}".format(num))
print(", ".join(numList))
