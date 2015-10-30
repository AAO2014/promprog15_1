#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from char_frequency_histogram_maker import CharFrequencyHistogramMaker

# начало положено - хорошо.
# тесты лучше класть в отдельную папку-пакет tests
# а вот файлы для них - еще в одну поддиректорию data к примеру
# что бы тесты не перемешивались с данными для них


class char_frequency_test(unittest.TestCase):  # НазваниеДолжноБытьCamelCase

    def test_abc(self):
        # здесь вопрос - сколько тестов делать?
        # по крайней мере несколько на граничные условия - пустой файл, файл с одним символом, файл с пустыми строками, файл с непечатными символами
        # и один "главный" тест, который по максимуму проверяет функционал
        # в нашем случае, что бы было множество разных символов в файле + множество (>2) строк
        # так что еще 5 тестов как минимум :)
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name='text1.txt')
        with open('test1.txt', 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)


if __name__ == '__main__':
    unittest.main()
