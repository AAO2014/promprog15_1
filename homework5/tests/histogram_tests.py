#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from homework5.char_frequency_histogram_maker import CharFrequencyHistogramMaker

# начало положено - хорошо.
# тесты лучше класть в отдельную папку-пакет tests
# а вот файлы для них - еще в одну поддиректорию data к примеру
# что бы тесты не перемешивались с данными для них
# TODO удаляй мои коменты после реализации требований


class CharFrequencyTest(unittest.TestCase):

    def assert_equal(self, textfile_1, testfile):
        # название плохое - перекликается с self.assertEqual - я даже и не понял сразу %)
        # переименуй - что делает эта функция? запускает код и сверяет с шаблоном.
        # и параметры тоже переименовать бы - источник и результат
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

    # хорошо, тест на пустой файл опустим, пусть будет файл с одним пробелом

    def test_null(self):
        self.assert_equal('data/text_null.txt', 'data/test_null.txt')

    # циклы для тестов плохи в том плане, что из 25 вариантов входных файлов при рефакторе, предпложим,
    # у тебя один сломается один - и как ты его будешь искать? лучше не ленится и писать отдельные функции :)

    def test_along_char(self):
        self.assert_equal('data/text_along_char.txt', 'data/test_along_char.txt')
        # файлы называются тоже очень похоже te_xt и te_st - ты заставил меня подумать и поискать чем же они отличаются
        # лучше пусть они начинаются с названия теста, а завершаются _src и _result так будет легче оринтироваться

    def test_only_empty_str(self):
        self.assert_equal('data/text_only_empty_str.txt', 'data/test_only_empty_str.txt')

    def test_nonprint_symbols(self):
        self.assert_equal('data/text_nonprint_symbols.txt', 'data/test_nonprint_symbols.txt')

    def test_big_text(self):
        self.assert_equal('data/text.txt', 'data/test_big_text.txt')


if __name__ == '__main__':
    unittest.main()
