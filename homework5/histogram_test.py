#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from char_frequency_histogram_maker import CharFrequencyHistogramMaker


class char_frequency_test(unittest.TestCase):

    def test_abc(self):
        v = CharFrequencyHistogramMaker()
        res = v.run(file_name='text1.txt')
        with open('test1.txt', 'r') as input_file:
            mustberes = input_file.read()

        self.assertEqual(res, mustberes)


if __name__ == '__main__':
    unittest.main()
