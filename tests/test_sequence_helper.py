import unittest

from src.sequence_helper import SequenceHelper

class TestSequenceHelper(unittest.TestCase):

    cls: SequenceHelper
    
    def setUp(self):
        self.cls = SequenceHelper()

    def test_upper_seq(self):
        for c in [
            ['aaa', 'AAA'],
            ['aAa', 'AAA'],
            ['AAA', 'AAA'],
        ]:
            with self.subTest(i='{} -> {}'.format(c[0], c[1])):
                actual = self.cls.upper_seq(c[0])
                self.assertEqual(c[1], actual)
    
    def test_complement_nucleobase(self):
        for c in [
            ['A', 'T'],
            ['T', 'A'],
            ['G', 'C'],
            ['C', 'G'],
            ['N', 'N'],
            ['R', 'R'],
        ]:
            with self.subTest(i='{} -> {}'.format(c[0], c[1])):
                actual = self.cls.complement_nucleobase(c[0])
                self.assertEqual(c[1], actual)
    
    def test_complement_seq(self):
        actual = self.cls.complement_seq('ACGTCNNRGAT')
        self.assertEqual('TGCAGNNRCTA', actual)
    
    def test_reverse(self):
        actual = self.cls.reverse_seq('ABCD')
        self.assertEqual('DCBA', actual)

    def test_seq2kmer(self):
        actual = self.cls.seq2kmer('12345678', 6)
        self.assertEqual(
            [
                '123456',
                '234567',
                '345678',
            ],
            actual
        )

if __name__ == '__main__':
    unittest.main()
