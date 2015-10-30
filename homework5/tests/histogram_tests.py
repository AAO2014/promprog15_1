#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from homework5.char_frequency_histogram_maker import CharFrequencyHistogramMaker

# начало положено - хорошо.
# тесты лучше класть в отдельную папку-пакет tests
# а вот файлы для них - еще в одну поддиректорию data к примеру
# что бы тесты не перемешивались с данными для них


class CharFrequencyTest(unittest.TestCase):

    def test_abc(self):
        # здесь вопрос - сколько тестов делать?
        # по крайней мере несколько на граничные условия - пустой файл, файл с одним символом, файл с пустыми строками, файл с непечатными символами
        # и один "главный" тест, который по максимуму проверяет функционал
        # в нашем случае, что бы было множество разных символов в файле + множество (>2) строк
        # так что еще 5 тестов как минимум :)
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name='data/text_abc.txt')
        with open('data/test_abc.txt', 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)

    # Первоначально пустой файл тест не проходил, так как функция вывода гистограмм всегда добавляла первод строки
    # (сделал проверку и у последнего растра не добавляю перенос строк )
    # !!!  но по условию задачи пустых файлов не бывает, минимум один пробел

    def test_null(self):
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name='data/text_null.txt')
        with open('data/test_null.txt', 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)

    def test_along_char(self):
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name='data/text_along_char.txt')
        with open('data/test_along_char.txt', 'r') as input_file:
            mustberes = input_file.read()
        self.assertEqual(res, mustberes)




if __name__ == '__main__':
    unittest.main()
