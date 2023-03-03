#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Реализуйте программу, которая будет отображать последние десять строк содержимого файла, имя
# которого будет передеваться в качестве аргумента командной строки. В случае отсутствия файла,
# вам нужно вывести соответствующее сообщение.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ошибка в количестве аргументов", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r", encoding="utf-8") as fileptr:
            lines = fileptr.readlines()
            print(" ".join(lines[-10:]))

    except FileNotFoundError:
        print("Такого файла не существует!", file=sys.stderr)
        sys.exit(1)
