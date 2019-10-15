import unittest
import math
import random
import hash_functions as hf


class Test_Hash_Functions(unittest.TestCase):
    def test_h_ascii_basic(self):
        self.assertEqual(hf.h_ascii('test', 500), 447)

    def test_h_ascii_small_array(self):
        self.assertEqual(hf.h_ascii('test', 25), 24)

    def test_h_ascii_empty_string(self):
        with self.assertRaises(ValueError):
            hf.h_ascii('', random.randint(1, 100))

    def test_h_ascii_bad_array(self):
        with self.assertRaises(ValueError):
            hf.h_ascii('test', random.randint(0, -100))

    def test_h_ascii_none_string(self):
        with self.assertRaises(ValueError):
            hf.h_ascii(None, random.randint(1, 100))

    def test_h_ascii_wrong_type(self):
        with self.assertRaises(ValueError):
            hf.h_ascii(13, random.randint(1, 100))


if __name__ == '__main__':
    unittest.main()
