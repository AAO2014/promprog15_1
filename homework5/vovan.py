#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать,
# какие символы в секретных зашифрованных посланиях употребляются чаще других.
# Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов.
# Поэтому он хочет построить гистограмму количества символов в сообщении.
# Гистограмма – это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз,
# соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

# Формат входных данных
#
# Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы,
# цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), пробелы и переводы строк.
# Размер входного файла не превышает 104 байт. Текст содержит хотя бы один непробельный символ.
# Все строки входного файла не длиннее 200 символов.


# Формат выходных данных
#
# Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#»,
# количество которых должно быть равно количеству символов c в данном тексте.
# Под каждым столбиком напишите символ, соответствующий ему.
# Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке,
# первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга.
# Отсортируйте столбики в порядке увеличения кодов символов.


# Примеры
#    Hello, world!
#         #
#         ##
#    #########
#    !,Hdelorw


#    Twas brillig, and the slithy toves
#    Did gyre and gimble in the wabe;
#    All mimsy were the borogoves,
#    And the mome raths outgrabe.
#    	      #
#             #
#             #
#             #
#             #
#             #         #
#             #  #      #
#          #  # ###  ####
#          ## ###### ####
#          ##############
#          ##############  ##
#    #  #  ############## ###
#    ########################
#    ,.;ADTabdeghilmnorstuvwy

from collections import  defaultdict

<<<<<<< HEAD:homework5/vovan1.py

class Vovan:
    ignore_sym = ['\n', ' ']
    frequency = defaultdict(int)
    print_matrix = []

    def read_file(self, filename):
        with open(filename, 'r') as input_file:
            for line in input_file:
                for char in line:
                    if char in self.ignore_sym:
                        continue
                    self.frequency[char] += 1


    def calc_max_val(self):
        max_val = 0
        for k, v in self.frequency.items():
            if v > max_val:
                max_val = v
        return max_val

    def get_histogramm(self, max_val):
        sorted_chars = sorted(self.frequency)
        for key in sorted_chars:
            spaces = ' ' * (max_val - self.frequency[key])
            self.print_matrix.append(key + '#' * self.frequency[key] + spaces)
        return

    def print_histogramm(self, max_val):
        for num_of_line_of_raster in range(max_val + 1):
            line_of_raster = ''
            for n_str in range(len(self.frequency)):
                line_of_raster += self.print_matrix[n_str][max_val - num_of_line_of_raster]
            print(line_of_raster)
=======
IGNORE_SYMBOLS = ['\n', ' ']  # это глобальная константа, по соглашению должна быть В ВЕРХНЕМ РЕГИСТРЕ
print_matrix = []  # надо убрать, см ниже


def read_file(filename):
    # не нужно глобальных переменных, каждая функция возвращает результать своего труда,
    # который идет параметром в другие функции
    frequency = defaultdict(int)
    with open(filename, 'r') as input_file:
        for line in input_file:
            for char in line:
                if char in IGNORE_SYMBOLS:
                    continue
                frequency[char] += 1
    return frequency


def calc_max_val(frequency):
    max_val = 0
    for k, v in frequency.items():
        if v > max_val:
            max_val = v
    return max_val


def get_histogramm(frequency, max_val):
    # эта должна формировать print_matrix
    sorted_chars = sorted(frequency)
    for key in sorted_chars:
        spaces = ' ' * (max_val - frequency[key])
        print_matrix.append(key + '#' * frequency[key] + spaces)
    return


def print_histogramm(frequency, max_val):
    # здесь frequency нужна только для вычисления своего размера,
    # который зачем-то кстати вычисляется в цикле
    # вынеси размер в параметр и вычисляй вовне
    for num_of_line_of_raster in range(max_val + 1):
        line_of_raster = ''
        for n_str in range(len(frequency)):
            line_of_raster += print_matrix[n_str][max_val - num_of_line_of_raster]
        print(line_of_raster)
>>>>>>> de15e377828621742f697f319a988de9da87ff85:homework5/vovan.py


# как доп задание - сделай из этого скрипта несколько функций,
# каждая делающая своё- read_from_file, calc_frequency, get_histogramm и print_histogramm
# а в конце модуля - запуск их всех if __name__ == '__main__':

# это будет подготовкой к переходу к обьектному подходу в решении задачи

if __name__ == '__main__':
<<<<<<< HEAD:homework5/vovan1.py
    v = Vovan()

    v.read_file('text.txt')

    max_val = v.calc_max_val()
    
    v.get_histogramm(max_val)

    v.print_histogramm(max_val)
=======
    frequency = read_file('text.txt')
    max_val = calc_max_val(frequency=frequency)
    get_histogramm(frequency=frequency, max_val=max_val)
    print_histogramm(frequency=frequency, max_val=max_val)
>>>>>>> de15e377828621742f697f319a988de9da87ff85:homework5/vovan.py
