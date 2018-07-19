#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        test_vector = [
            ('A', 50),
            ('123', -1),
            ('AAAA', 180),
            ('AAAAA', 200),
            ('AAAAAA', 250),
            ('A' * 9, 380),
            ('EEEEEBB', 200),
            ('AAABB', 175),
            ('AABCD', 165),
            ('F' * 6, 40),
            ('STXYZ', 45 + 17 + 20),
            ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 853 - 21 - 20 - 20 + 45),
        ]
        for skus, expected in test_vector:
            self.assertEqual(checkout(skus), expected)
