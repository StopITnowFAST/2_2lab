#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Написать программу которая удалит текущий файл, если в файле меньше 5 строк.
# Иначе переименнует файл в "проверен"

if __name__ == "__main__":
    sum = 0
    with open("ind3file.txt", "r", encoding="utf-8") as fileptr:
        for i in fileptr:
            sum += 1

    if sum < 5:
        os.remove("ind3file.txt")
    else:
        os.rename("ind3file.txt", "Проверен.txt")
