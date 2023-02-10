#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на экран только
# предложения, содержащие введенное с клавиатуры слово.

if __name__ == "__main__":
    print("Введите искомое слово")
    word = input()

    with open("ind1file.txt", "r", encoding='utf-8') as fileptr:
        for i in fileptr:
            if i.find(word) != -1:
                print(i)
