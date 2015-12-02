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

# изменения в ТЗ:
# 1) нужна поддержка юникода, см файл unicode.txt
# 2) нужно уметь фильтровать по минимальной и максимальной частоте повторений при выводе гистограмм,
# например для второго примера ставим 5 и 8 и получаем след гистограмму
#
#            #
#      #     #
#  #  ### ####
#  ###########
#  ###########
#  ###########
#  ###########
#  ###########
#  abghilmorst
#



class CharFrequencyHistogramMaker:
    IGNORE_SYM = ['\n', ' ', '\r']

    def __init__(self):
        self.frequency = defaultdict(int)
        self.max_frequency = 0
        self.num_chars = 0

    def _get_frequency(self, source_text):
        frequency = defaultdict(int)
        for char in source_text:
            if char in self.IGNORE_SYM:
                continue
            frequency[char] += 1
        return frequency

    def _calc_max_frequency(self):
        max_val = 0
        for k, v in self.frequency.items():
            if v > max_val:
                max_val = v
        return max_val

    def _get_histogram(self):
        sorted_chars = sorted(self.frequency)
        s = ''

        for j in range(self.max_frequency, 0, -1):
            for char in sorted_chars:
                s += '#' if self.frequency[char] >= j else ' '
            s = s.rstrip()
            s += '\n'

        for k in sorted_chars:
            s += k

        return s

    def _truncate_frequency(self, min_frq, max_frq):
        frequency = defaultdict(list)
        if not min_frq or not max_frq:
            return self.frequency
        for k, v in self.frequency.items():
            if v >= min_frq and v <= max_frq:
                frequency[k] = v
        return frequency

    def run(self, source_text, min_frequency=None, max_frequency=None):
        self.frequency = self._get_frequency(source_text)
        self.frequency = self._truncate_frequency(min_frequency, max_frequency)
        self.max_frequency = self._calc_max_frequency()
        return self._get_histogram()

if __name__ == '__main__':
    v = CharFrequencyHistogramMaker()

    print(v.run(source_text='У лукоморья дуб зеленый, а на дубу котэ ученый', min_frequency=1, max_frequency=1))
