#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from homework5.char_frequency_histogram_maker import CharFrequencyHistogramMaker


class CharFrequencyTest(unittest.TestCase):

    # отлично! мы научились делать обработчиков и функциональные тесты к ним :)
    def compare_histogram_and_answer(self, source_file, answer_file):
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name=source_file)
        with open(answer_file, 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)

    def test_abc(self):
       self.compare_histogram_and_answer('data/abc_src.txt', 'data/abc_ans.txt')

    def test_null(self):
        self.compare_histogram_and_answer('data/null_src.txt', 'data/null_ans.txt')

    def test_alone_space_char(self):
        # чем это от test_null отличается? не понял. входные файлы одинаковы...
        self.compare_histogram_and_answer('data/alone_space_char_src.txt', 'data/alone_space_char_ans.txt')

    def test_along_char(self):
        self.compare_histogram_and_answer('data/alone_char_src.txt', 'data/alone_char_ans.txt')

    def test_only_empty_str(self):
        # чем это от test_null отличается? не понял. входные файлы одинаковы...
        self.compare_histogram_and_answer('data/only_empty_str_src.txt', 'data/only_empty_str_ans.txt')

    def test_nonprint_symbols(self):
        # чем это от test_null отличается? не понял. входные файлы одинаковы...
        self.compare_histogram_and_answer('data/nonprint_symbols_src.txt', 'data/nonprint_symbols_ans.txt')

    def test_big_text(self):
        self.compare_histogram_and_answer('data/big_text_src.txt', 'data/big_text_ans.txt')

    # не нужно гнаться за количеством тестов - при доработке придется все их проходить...
    # главое что бы проверилось как скрипт работает при "Он содержит строчные и прописные латинские буквы,
    #   цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), пробелы и переводы строк." - из ТЗ
    # кстати знаки препинания мы не проверили...



if __name__ == '__main__':
    unittest.main()
