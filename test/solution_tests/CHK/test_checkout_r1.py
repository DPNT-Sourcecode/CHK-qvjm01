#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        test_vector = [
            # ('A', 50),
            # ('F', -1),
            # ('AAAAA', 230),
            # ('AAAAAA', 260),
            ('AAABB', 175),
            ('AABCD', 165)
        ]
        for skus, expected in test_vector:
            self.assertEqual(checkout(skus), expected)
