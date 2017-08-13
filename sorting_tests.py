from unittest import TestCase

from sorting import *


LIST_ONE = [1, 2, 3, 4, 5]
LIST_TWO = [5, 4, 3, 2, 1]
LIST_THREE = [3, 8, 1, 5, 2, 1, 13, 0]
SORTED_LIST_ONE = LIST_ONE[:]
SORTED_LIST_TWO = SORTED_LIST_ONE[:]
SORTED_LIST_THREE = [0, 1, 1, 2, 3, 5, 8, 13]


class MergeSortTests(TestCase):

    def test_sort_1(self):
        self.assertEqual(merge_sort([]), [])

    def test_sort_2(self):
        self.assertEqual(merge_sort([2]), [2])

    def test_sort_3(self):
        self.assertEqual(merge_sort([1, 2]), [1, 2])

    def test_sort_4(self):
        self.assertEqual(merge_sort([2, 1]), [1, 2])

    def test_sort_5(self):
        self.assertEqual(merge_sort(LIST_ONE), SORTED_LIST_ONE)

    def test_sort_6(self):
        self.assertEqual(merge_sort(LIST_TWO), SORTED_LIST_TWO)

    def test_sort_7(self):
        self.assertEqual(merge_sort(LIST_THREE), SORTED_LIST_THREE)
