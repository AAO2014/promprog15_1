#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from homework5.char_frequency_histogram_maker import CharFrequencyHistogramMaker


class CharFrequencyTest(unittest.TestCase):

    def compare_histogram_and_answer(self, source_file, answer_file, min_frequency=0, max_frequency=0):
        v = CharFrequencyHistogramMaker()
        res = v.run(source_file, min_frequency, max_frequency)
        with open(answer_file, 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)

    def test_abc(self):   # простой тест на 3 символа
       self.compare_histogram_and_answer('data/abc_src.txt', 'data/abc_ans.txt')

    def test_null(self):  # абсолютно пустой файл, ни одного символа
        self.compare_histogram_and_answer('data/null_src.txt', 'data/null_ans.txt')

    def test_alone_space_char(self):
        #  содержит один симвом пробела.
        self.compare_histogram_and_answer('data/alone_space_char_src.txt', 'data/alone_space_char_ans.txt')

    def test_along_char(self):
        self.compare_histogram_and_answer('data/alone_char_src.txt', 'data/alone_char_ans.txt')

    def test_only_empty_str(self):
        # содержит одни только перводы каретки
        self.compare_histogram_and_answer('data/only_empty_str_src.txt', 'data/only_empty_str_ans.txt')

    def test_nonprint_symbols(self):
        # содержит непечатаемые символы (табуляции, перводы каретки)
        self.compare_histogram_and_answer('data/nonprint_symbols_src.txt', 'data/nonprint_symbols_ans.txt')

    def test_big_text(self):
        self.compare_histogram_and_answer('data/big_text_src.txt', 'data/big_text_ans.txt')

    def test_german(self): # юникод
        self.compare_histogram_and_answer('data/german_src.txt', 'data/german_ans.txt')

    def test_big_2_12_text(self): #проверяем граничные условия фильтрации частоты -1 слева и -1 справа
        self.compare_histogram_and_answer('data/big_text_src.txt', 'data/big_text_2_12_ans.txt', 2, 12)


if __name__ == '__main__':
    unittest.main()
