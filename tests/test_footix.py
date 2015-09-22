#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from footix import footix


class FootixTestCase(unittest.TestCase):

    def test_data_type(self):
        data = footix.get_data('today')
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
