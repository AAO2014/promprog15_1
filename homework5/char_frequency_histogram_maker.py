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

from collections import defaultdict


class CharFrequencyHistogramMaker:
    IGNORE_SYM = ['\n', ' ']

    def __init__(self):
        self.frequency = defaultdict(int)
        self.print_matrix = []
        self.max_val = 0

    def read_file(self, filename):
        self.frequency = defaultdict(int)
        with open(filename, 'r') as input_file:
            for line in input_file:
                for char in line:
                    if char in self.IGNORE_SYM:
                        continue
                    self.frequency[char] += 1

    def calc_max_val(self):
        max_val = 0
        for k, v in self.frequency.items():
            if v > max_val:
                max_val = v
        return max_val

    def get_histogramm(self):
        sorted_chars = sorted(self.frequency)
        self.print_matrix = []

        for key in sorted_chars:
            spaces = ' ' * (self.max_val - self.frequency[key])
            self.print_matrix.append(key + '#' * self.frequency[key] + spaces)

    def print_histogramm(self):
        res = ''
        for num_of_line_of_raster in range(self.max_val + 1):
            line_of_raster = ''
            for n_str in range(len(self.frequency)):
                line_of_raster += self.print_matrix[n_str][self.max_val - num_of_line_of_raster]
            # print(line_of_raster)
            if self.max_val - num_of_line_of_raster > 0:
                end_of_str = '\n'
            else:
                end_of_str = ''
            res += line_of_raster + end_of_str
        return res

    def run(self, file_name):
        self.read_file(file_name)
        self.max_val = self.calc_max_val()
        self.get_histogramm()
        return self.print_histogramm()



if __name__ == '__main__':
    v = CharFrequencyHistogramMaker()

    print(v.run(file_name='tests/data/text.txt'))
    print(v.run(file_name='tests/data/text_2.txt'))
