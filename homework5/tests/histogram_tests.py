#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from homework5.char_frequency_histogram_maker import CharFrequencyHistogramMaker

# начало положено - хорошо.
# тесты лучше класть в отдельную папку-пакет tests
# а вот файлы для них - еще в одну поддиректорию data к примеру
# что бы тесты не перемешивались с данными для них


class CharFrequencyTest(unittest.TestCase):

    def assert_equal(self, textfile_1, testfile):
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name=textfile_1)
        with open(testfile, 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)

    def test_abc(self):
        # здесь вопрос - сколько тестов делать?
        # по крайней мере несколько на граничные условия - пустой файл, файл с одним символом, файл с пустыми строками, файл с непечатными символами
        # и один "главный" тест, который по максимуму проверяет функционал
        # в нашем случае, что бы было множество разных символов в файле + множество (>2) строк
        # так что еще 5 тестов как минимум :)
        self.assert_equal('data/text_abc.txt', 'data/test_abc.txt')

    # Первоначально пустой файл тест не проходил, так как функция вывода гистограмм всегда добавляла первод строки
    # (сделал проверку и у последнего растра не добавляю перенос строк )
    # !!!  но по условию задачи пустых файлов не бывает, минимум один непробельный (из разрешенных!) символ

    def test_null(self):
        self.assert_equal('data/text_null.txt', 'data/test_null.txt')

    # просится цикл для всех файлов начинающихся с text и test, но долго реализовывать

    def test_along_char(self):
        self.assert_equal('data/text_along_char.txt', 'data/test_along_char.txt')

    def test_only_empty_str(self):
        self.assert_equal('data/text_only_empty_str.txt', 'data/test_only_empty_str.txt')

    def test_nonprint_symbols(self):
        self.assert_equal('data/text_nonprint_symbols.txt', 'data/test_nonprint_symbols.txt')

    def test_big_text(self):
        self.assert_equal('data/text.txt', 'data/test_big_text.txt')


if __name__ == '__main__':
    unittest.main()
